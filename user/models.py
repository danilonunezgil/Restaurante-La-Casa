from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=150)
    active =models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    id_person = models.ForeignKey('person', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class person(models.Model):
    cc = models.IntegerField(default=0)
    names = models.CharField(max_length=150)
    last_names = models.CharField(max_length=150)
    celphone = models.IntegerField(default=0)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    rol = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.names}, {self.rol}, {self.celphone}, {self.email} "
    


