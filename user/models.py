from datetime import datetime
import imp
from django.db import models
from django.utils import timezone
from bakery_shop.models import Bakery_Tb
from home_bakers.models import Home_Tb

# Create your models here.
class User_Tb(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Usernames=models.CharField(max_length=50)
    Address=models.CharField(max_length=100,default='none')
    Phone=models.CharField(max_length=10,default='none')
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=10)
    Gender=models.CharField(max_length=50,default='none')
    Userimage=models.ImageField(upload_to='img',default='none')

    def __str__(self):
        return self.Firstname

class HCart(models.Model):
    home=models.ForeignKey(Home_Tb,on_delete=models.CASCADE)
    user=models.ForeignKey(User_Tb,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    image=models.ImageField(upload_to='img',default='none')
    pname=models.CharField(max_length=50)
    price=models.IntegerField()
    status=models.BooleanField(default="False")
    paystatus=models.BooleanField(default="False")


    def __str__(self):
        return self.pname

class BCart(models.Model):
    bakers=models.ForeignKey(Bakery_Tb,on_delete=models.CASCADE)
    user=models.ForeignKey(User_Tb,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    image=models.ImageField(upload_to='img',default='none')
    pname=models.CharField(max_length=50)
    price=models.IntegerField()
    status=models.BooleanField(default="False")
    paystatus=models.BooleanField(default="False")


    def __str__(self):
        return self.pname