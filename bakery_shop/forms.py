from . models import *
from django import forms

class Pforms(forms.ModelForm):
    class Meta:
        model = Product
        fields =  ['name','desc','price','img','category','available']

class Bforms(forms.ModelForm):
    class Meta:
        model = Bakery_Tb
        fields =  ['Firstname','Lastname','Businessname','Pannumber','Address','Phone','Email','Password']