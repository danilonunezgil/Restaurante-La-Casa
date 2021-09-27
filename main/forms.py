from django import forms

#contact form class
class Contactf(forms.Form):
    Name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Tu nombre"
    }))
    Last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Tu Apellido"
    }))
    Email = forms.EmailField( widget=forms.TextInput(attrs={
        'placeholder': "Tu Correo Electronico"
    }))
    Message = forms.CharField( widget=forms.Textarea(attrs={
        'placeholder': "Tu mensaje"
    }))