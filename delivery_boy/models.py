from django.db import models
from user . models import User_Tb
from home_bakers . models import Home_Tb
from bakery_shop . models import Bakery_Tb
from django.utils import timezone



# Create your models here.
class Delivery_Tb(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Usernames=models.CharField(max_length=50)
    Phone=models.CharField(max_length=10,default='none')
    Vehiclenumber=models.CharField(max_length=20,default='none')
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=10)
    Gender=models.CharField(max_length=50,default='none')
    Drivinglicense=models.ImageField(upload_to='img')
    Address=models.CharField(max_length=100,default='none')
    def __str__(self):
        return self.Firstname

class notification(models.Model):
    username=models.CharField(max_length=50)
    contactno=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    prdname=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    neworderstatus=models.BooleanField(default=False)
    orderStatus=models.BooleanField(default=False)
    boy=models.ForeignKey(Delivery_Tb,on_delete=models.CASCADE,null=True)
    home=models.ForeignKey(Home_Tb,on_delete=models.CASCADE,null=True)  
    bakey=models.ForeignKey(Bakery_Tb,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User_Tb,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.username                                                                                                                                                                                                                                                                                                                         
    
