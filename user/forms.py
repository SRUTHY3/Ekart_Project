from . models import *
from django import forms

class Uforms(forms.ModelForm):
    class Meta:
        model = User_Tb
        fields =  ['Firstname','Lastname','Usernames','Address','Phone','Email','Password']