from typing import Generic
from django.shortcuts import reverse 
from django.views import generic
from .forms import Contactf
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib import messages 
from .models import Product
from django.db.models import Q



# Create your views here.


class ContactView(generic.FormView):
    form_class = Contactf
    template_name = "contact.html"

    def get_success_url(self):        
        return reverse("contact")
    
    def form_valid(self, form):
        messages.info(
            self.request, "Hemos recibido tu mensaje")
        Name = form.cleaned_data.get('Name')
        Last_name = form.cleaned_data.get('Last_name')
        Email = form.cleaned_data.get('Email')
        Message = form.cleaned_data.get('Message')

        full_message = f"""
            Mensaje recibibo de {Name},{Last_name}, {Email}
            ___________________________________


            {Message}
            """
        send_mail(
            subject="Mensaje recibido por Contact Form",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)



class ProductListView(generic.ListView):
    template_name='product_list.html'
    queryset = Product.objects.all()
    

   