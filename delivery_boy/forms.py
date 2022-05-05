import imp
from . models import *
from django import forms




class Dforms(forms.ModelForm):
    class Meta:
        model = Delivery_Tb
        fields =  ['Firstname','Lastname','Usernames','Phone','Vehiclenumber','Email','Password','Address']

       