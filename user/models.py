from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cc = models.IntegerField(default=0, blank=True)
    celphone = models.IntegerField(default=0, blank=True)
    address = models.CharField(max_length=150, blank=True)
    rol = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username 