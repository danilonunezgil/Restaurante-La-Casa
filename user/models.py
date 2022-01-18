from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, default=1, null=True, on_delete=models.CASCADE,help_text="Enter a user name ")
    cc = models.CharField(max_length=11, blank=True, help_text="Enter your ID number ")
    celphone = models.CharField(max_length=11, blank=True, help_text="Enter your cell phone number ")
    home_address = models.CharField(max_length=150, blank=True, help_text="Enter your home address")
    edad=models.IntegerField(default=0)
    rol = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username 