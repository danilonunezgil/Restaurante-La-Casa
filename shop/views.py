from typing import Generic
from django.http import request
from django.shortcuts import reverse, get_object_or_404
from django.views import generic
from .forms import Contactf, AddToCartForm
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages 
from .models import Product
from django.db.models import Q
from .utils import get_or_set_order_session



# Create your views here.


class ContactView(generic.FormView):
    form_class = Contactf
    template_name = "contact.html"

    def get_success_url(self):        
        return reverse("contact")
    
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
        return get_object_or_404(Product, slug = self.kwargs["slug"])
    
    def get_success_url(self):
        return reverse('Home') #TODO: shop

    def form_valid(self, form):
        order = get_or_set_order_session(self.request)
        product = self.get_object
        item_filter = order.items.filter(product = product)
        if item_filter.exists():
            item = item_filter.first()
            item.quantity = int(form.cleaned_data['quantity'])
            item.save()

        else:
            new_item = form.save(commit=False)
            new_item.product = product
            new_item.order = order
            new_item.save()

        return super(ProductDetailView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = self.get_object()
        return context