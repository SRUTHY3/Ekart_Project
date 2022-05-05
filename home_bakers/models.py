from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.template.defaultfilters import slugify
from signal import default_int_handler

# Create your models here.
class Home_Tb(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Businessname=models.CharField(max_length=50)
    Businesstype=models.CharField(max_length=50,default='none')
    Businessimage=models.ImageField(upload_to='img',default='none')
    Pannumber=models.CharField(max_length=12,default='none')
    Address=models.CharField(max_length=100,default='none')
    Phone=models.CharField(max_length=10,default='none')
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=10)
    Aadharcard=models.ImageField(upload_to='img')
    
    def __str__(self):
        return self.Firstname

#category table
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    BakeryId=models.ForeignKey(Home_Tb,on_delete=models.CASCADE,default='1')


    def save(self):
        self.slug=slugify(self.name)
        super(categ,self).save()

    def __str__(self):
        return self.name

#product table
class Products(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField()
    price=models.IntegerField()
    # stock=models.IntegerField()
    img=models.ImageField(upload_to='product',default='delivery_boy.jpg')
    category=models.ForeignKey(categ,on_delete=models.CASCADE,default='1')
    BakeryId=models.ForeignKey(Home_Tb,on_delete=models.CASCADE,default='1')
    available=models.BooleanField(default='True')

    def save(self):
        self.slug=slugify(self.name)
        super(Products,self).save()

    def __str__(self):
        return self.name
   
   


