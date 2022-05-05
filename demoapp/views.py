from django.shortcuts import render
from.models import food

# Create your views here.
def home(request):
    return render(request,'index.html')
def regas(request):  
    return render(request,"reg.html")
def logas(request):  
    return render(request,"log.html")


