import imp
from . models import *
from django import forms

class Pforms(forms.ModelForm):
    class Meta:
        model = Products
        fields =  ['name','desc','price','img','category','available']


class Eforms(forms.ModelForm):
    class Meta:
        model = Home_Tb
        fields =  ['Firstname','Lastname','Businessname','Pannumber','Address','Phone','Email','Password']