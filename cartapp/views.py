from django.shortcuts import render

# Create your views here.
def hbcart(request):
    return render(request,'hbcart.html')
def hbpay(request):
    return render(request,'hbpay.html')
def hbthank(request):
    return render(request,'hbthank.html')
def bscart(request):
    return render(request,'bscart.html')
def bspay(request):
    return render(request,'bspay.html')
def bsthank(request):
    return render(request,'bsthank.html')
