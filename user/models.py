from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cc = models.IntegerField(default=0)
    celphone = models.IntegerField(default=0)
    address = models.CharField(max_length=150)
    rol = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.names}, {self.rol}, {self.celphone}, {self.email} "
   