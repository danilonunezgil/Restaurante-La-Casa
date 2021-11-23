from django import forms
from django.forms import fields

from shop.models import OrderItem

#contact form class
class Contactf(forms.Form):
    Name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your Name"
    }))
    Last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your Last Name"
    }))
    Email = forms.EmailField( widget=forms.TextInput(attrs={
        'placeholder': "Your e-mail"
    }))
    Message = forms.CharField( widget=forms.Textarea(attrs={
        'placeholder': "Your Message"
    }))

class AddToCartForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['quantity']