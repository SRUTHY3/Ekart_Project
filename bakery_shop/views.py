from django.shortcuts import render,redirect
from . models import *
from user. models import *

from django.contrib import messages
from . forms import *
from delivery_boy . models import *
# Create your views here.
#create html pages for bakery shop

def Bpage(request):
    return render(request,'bakeryfolder/Bpage.html')   




#bakery shop register page is connected to database
def Breg(request):
    if request.method=="POST":
       firstname=request.POST.get("First_Name")
       lastname=request.POST.get("last_Name")
       Businessname=request.POST.get("Business_Name")
       businesstype=request.POST.get("Business_Type")
       panno=request.POST.get("Pan_Number")
       address=request.POST.get("address")
       phone=request.POST.get("phoneNumber")
       email=request.POST.get("email")
       p1=request.POST.get("password")
       p2=request.POST.get("Conform_Password")
       aadharcard=request.FILES["img"]
       busimg=request.FILES["bimg"]
       
       if p1==p2:
            if Bakery_Tb.objects.filter(Businessname=Businessname).exists():
                messages.info(request,'Businessname already exists')
            elif Bakery_Tb.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            elif Bakery_Tb.objects.filter(Pannumber=panno).exists():
                messages.info(request,'Pannumber already exists')
            elif Bakery_Tb.objects.filter(Phone=phone).exists():
                messages.info(request,'Phonenumber already exists')
            else:
                userdata=Bakery_Tb(Firstname=firstname,Lastname=lastname,Businessname=Businessname,Businesstype=businesstype,Pannumber=panno,Address=address,
                Phone=phone, Email= email, Password= p1,Aadharcard=aadharcard,Businessimage=busimg)
                userdata.save()
                return redirect("Blog")
       else:
             messages.info(request,'password not match') 
    return render(request,"bakeryfolder/Breg.html")   


#bakery shop login page is connected to database
def Blog(request):
    if request.method=="POST":
       try: 
            uname=request.POST.get("uname")
            password=request.POST.get("pwd")
            blogin=Bakery_Tb.objects.get(Businessname=uname,Password=password)
            request.session['uname']=blogin.Businessname
            request.session['id']=blogin.id
            return redirect("Bpage")

       except Bakery_Tb.DoesNotExist as e:

           messages.info(request,'invalid username/password')  
    return render(request,'bakeryfolder/Blog.html')

def Addcateg(request):
    if request.method=="POST":
       cname=request.POST.get("cname")
       categsave=categ(name=cname)
       categsave.save()
       return redirect("Bpage")
    return render(request,'bakeryfolder/Addcateg.html')

def AddproB(request):
    if request.method=='POST':
       name=request.POST.get("Name")
       descrption=request.POST.get("Desc")
       price=request.POST.get("Price")
    #    quality=request.POST.get("Quality")
       avail=request.POST.get("avail")
       img=request.FILES.get('img')
       cid=request.POST.get("cid")
       bid=request.POST.get("bid")
       addsave=Product(name=name,desc=descrption,price=price,
       img=img,category_id=cid,BakeryId_id=bid,available=avail)
       addsave.save()
       return redirect("Bpage")
    categid=categ.objects.filter(BakeryId=request.session['id'])
    return render(request,'bakeryfolder/AddproB.html',{'cid':categid})

#view product
def ViewpageB(request):
    proview=Product.objects.filter(BakeryId=request.session['id'])
    return render(request,'bakeryfolder/ViewpageB.html',{'prod':proview})


def produpdate(request,id):
    prod=Product.objects.get(id=id)
    form = Pforms(request.POST or None , instance=prod)
    if form.is_valid():
        form.save()
        return render(request,'bakeryfolder/prodD.html',{'det':prod})
    return render(request,'bakeryfolder/produpdate.html',{'prod':prod,'form':form})

def proddetail(request,prodid):
    detail=Product.objects.get(id=prodid)
    return render(request,'bakeryfolder/prodD.html',{'det':detail})

def delete(request,pid):
    prod = Product.objects.get(id=pid)
    if request.method == "POST":
        prod.delete()
        pro=Product.objects.filter(BakeryId=request.session['id'])
        return render(request,'bakeryfolder/ViewpageB.html',{'prod':pro})
    return render(request,'bakeryfolder/delete.html',{'prod':prod})


def profile(request):
    hid=request.session['id']
    prof=Bakery_Tb.objects.get(id=hid)
    return render(request,'bakeryfolder/profile.html', {'prof':prof})


def logout(request):
    return redirect('/')


def categorys(request):
    caty=categ.objects.filter(BakeryId=request.session['id'])
    return render(request,'bakeryfolder/categorys.html',{'caty':caty})


def deletecat(request,ctyid):
    catb = categ.objects.get(id=ctyid)
    if request.method == "POST":
        catb.delete()
        return redirect("Bpage")
    return render(request,'bakeryfolder/deletecat.html',{'catb':catb})

def vieworders(request,pk):
    bcrt=BCart.objects.filter(bakers=pk)
    delivery=notification.objects.filter(home=request.session['id'])
    return render(request,'bakeryfolder/vieworders.html',{'bcrt':bcrt,'d':delivery})

def confirmpayment(request,pk):
    BCart.objects.filter(id=pk).update(status=True)
    bcrt=BCart.objects.filter(bakers=request.session['id'])
    return render(request,'bakeryfolder/vieworders.html',{'bcrt':bcrt})


def editpro(request,id):
    edit=Bakery_Tb.objects.get(id=id)
    eform = Bforms(request.POST or None , instance=edit)
    if eform.is_valid():
        eform.save()
        return redirect("Bpage")
    return render(request,'bakeryfolder/editpro.html',{'pro':edit,'forms':eform})

def deliveryD(request):
    if request.method == 'POST':
       name=request.POST.get("name")
       phno=request.POST.get("phno")
       adr=request.POST.get("adr") 
       pname=request.POST.get("pname") 
       price=request.POST.get("price") 
       bakery=request.POST.get("bid") 
       user=request.POST.get("uid") 
       ds=notification(username=name,contactno=phno,address=adr,
       prdname=pname,price=price,bakey_id=bakery,user_id=user)
       ds.save()
    bcart=BCart.objects.filter(bakers=request.session['id'])
    return render(request,'bakeryfolder/deliverydetails.html',{'d':bcart})