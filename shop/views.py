#from re import template
#from django.contrib.messages.api import error
#from typing import Generic
from django.core import paginator
from django.db.models.query import InstanceCheckMeta
from django.http import request, JsonResponse, response, Http404
from django.shortcuts import reverse, get_object_or_404, redirect, render
from django.views import generic
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages 
#from django.db.models import Q
#from django.urls import resolve
from django.core.paginator import Paginator

from shop.forms import Contactf, AddToCartForm
from shop.models import Product, OrderItem
from shop.utils import get_or_set_order_session



# Create your views here.


class ContactView(generic.FormView):
    form_class = Contactf
    template_name = "contact.html"

    def get_success_url(self):        
        return reverse("shop:contact")
    
    def form_valid(self, form):
        messages.info(
            self.request, "We have received your message ")
        Name = form.cleaned_data.get('Name')
        Last_name = form.cleaned_data.get('Last_name')
        Email = form.cleaned_data.get('Email')
        Message = form.cleaned_data.get('Message')

        full_message = f"""
            Message received from {Name},{Last_name}, {Email}
            ___________________________________


            {Message}
            """
        send_mail(
            subject="Message received by Contact Form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        product = Product.objects.filter(title__icontains=search)
        return render(request, 'product_list.html', {'search':search, 'product':product})
    else:
        return render(request, 'product_list.html', {})

class ProductListView(generic.ListView):
    template_name='product_list.html'
    model = Product
    paginate_by = 12
    context_object_name = 'product'
    
class ProductDetailView(generic.FormView):
    template_name='product_detail.html'
    form_class = AddToCartForm
    
    def get_object(self):
        return get_object_or_404(Product, slug = self.kwargs["slug"])

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            order = get_or_set_order_session(self.request)
            product = self.get_object()
            form = self.form_class(request.POST)
            item_filter = order.items.filter(product = product)

            if form.is_valid():
                if item_filter.exists():
                    item = item_filter.first()
                    item.quantity += int(form.cleaned_data['quantity'])
                    item.save()
                    msg = "sumar item"
                    error = form.errors
                else:
                    new_item = form.save(commit=False)
                    new_item.product = product
                    new_item.order = order
                    new_item.save()
                    msg = "nuevo item"
                    error = form.errors
                response = JsonResponse({'mensaje':msg,'error':error})
                return response    
            else:
                msg = "form no valido"
                error = form.errors
                response = JsonResponse({'mensaje':msg,'error':error})
                print(form.errors)
                return response
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context

class CartView(generic.TemplateView):
    template_name = "cart.html"
    def get_context_data(self, *args,**kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context["order"] = get_or_set_order_session(self.request)
        return context

class IncreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.quantity += 1
        order_item.save()
        return redirect("shop:summary")

class DecreaseQuantityView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])

        if order_item.quantity <= 1:
            order_item.delete()
        else:
            order_item.quantity -= 1
            order_item.save()
        return redirect("shop:summary")

class RemoveFromCartView(generic.View):
    def get(self, request, *args, **kwargs):
        order_item = get_object_or_404(OrderItem, id=kwargs['pk'])
        order_item.delete()
        return redirect("shop:summary")
