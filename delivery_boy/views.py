from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from . forms import *

# Create your views here.


def Dpage(request):
    return render(request,'deliveryfolder/Dpage.html')


#delivery boy register page is connected to database
def Dreg(request):
    if request.method=="POST":
       firstname=request.POST.get("First_Name")
       lastname=request.POST.get("last_Name")
       username=request.POST.get("User_Name")
       phone=request.POST.get("phoneNumber")
       vehiclenumber=request.POST.get("VehicleNumber")
       email=request.POST.get("email")
       p1=request.POST.get("password")
       p2=request.POST.get("Conform_Password")
       gender=request.POST.get("gender")
       drivinglicense=request.POST.get("img")
       
       if p1==p2:
            if Delivery_Tb.objects.filter(Usernames=username).exists():
                messages.info(request,'Username already exists')
            elif Delivery_Tb.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            elif Delivery_Tb.objects.filter(Phone=phone).exists():
                messages.info(request,'Phonenumber already exists')
            elif Delivery_Tb.objects.filter(Vehiclenumber=vehiclenumber).exists():
                messages.info(request,'Vehiclenumber already exists')
            else:
                userdata=Delivery_Tb(Firstname=firstname,Lastname=lastname,Usernames=username,Phone=phone,Vehiclenumber=vehiclenumber,Email=email,Password=p1,Gender=gender,Drivinglicense=drivinglicense)
                userdata.save()
                return redirect("Dlog")
       else:
            messages.info(request,'password not match') 
    return render(request,"deliveryfolder/Dreg.html")   


#delivery boy login page is connected to database
def Dlog(request):
   if request.method=="POST":
       try: 
            uname=request.POST.get("uname")
            password=request.POST.get("pwd")
            dlogin=Delivery_Tb.objects.get(Usernames=uname,Password=password)
            request.session['uname']=dlogin.Usernames
            request.session['id']=dlogin.id
            return redirect("Dpage")

       except Delivery_Tb.DoesNotExist as e:

            messages.info(request,'invalid username/password') 

   return render(request,'deliveryfolder/Dlog.html')


def profile(request):
    hid=request.session['id']
    prof=Delivery_Tb.objects.get(id=hid)
    return render(request,'deliveryfolder/profile.html', {'prof':prof})

def logout(request):
    return redirect('/')

def detailsD(request,pk):
    D=notification.objects.filter(boy=pk)
    return render(request,'deliveryfolder/details.html',{'d':D})

def editpro(request,id):
    edit=Delivery_Tb.objects.get(id=id)
    eform = Dforms(request.POST or None , instance=edit)
    if eform.is_valid():
        eform.save()
        return redirect("Dpage")
    return render(request,'deliveryfolder/editpro.html',{'pro':edit,'forms':eform})


def neworder(request,pk):
    notification.objects.filter(id=pk).update(neworderstatus=True)
    D=notification.objects.filter(boy=request.session['id'])
    return render(request,'deliveryfolder/details.html',{'d':D})

def orderstat(request,pk):
    notification.objects.filter(id=pk).update(orderStatus=True)
    D=notification.objects.filter(boy=request.session['id'])
    return render(request,'deliveryfolder/details.html',{'d':D})
