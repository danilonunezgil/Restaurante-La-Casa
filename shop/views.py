from re import template
from typing import Generic
from django.db.models.query import InstanceCheckMeta
from django.http import request
from django.shortcuts import reverse, get_object_or_404, redirect
from django.views import generic
from .forms import Contactf, AddToCartForm
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages 
from .models import Product, OrderItem
from django.db.models import Q
from .utils import get_or_set_order_session
from django.urls import resolve


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



class ProductListView(generic.ListView):
    template_name='product_list.html'
    queryset = Product.objects.all()
    
class ProductDetailView(generic.FormView):
    template_name='product_detail.html'
    form_class = AddToCartForm
    
    def get_object(self):
        print('get_object')
        return get_object_or_404(Product, slug = self.kwargs["slug"])
    
    def get_success_url(self):
         print('get_succes')
         return reverse('Home')

    def form_valid(self, form):
        print('form valid')
        order = get_or_set_order_session(self.request)
        product = self.get_object()
        item_filter = order.items.filter(product = product)
        if item_filter.exists():
            item = item_filter.first()
            item.quantity += int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()

        return super(ProductDetailView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        print('get_context')
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
