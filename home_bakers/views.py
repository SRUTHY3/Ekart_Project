from django.shortcuts import render,redirect

from delivery_boy.models import notification

from . models import *
from user . models import *

from django.contrib import messages
from . forms import *
# from home_bakers.models import *

# Create your views here.

def hblist(request):
    return render(request,'userfolder/hblist.html')
def Hpage(request):
    return render(request,'homefolder/Hpage.html')



def Viewpage1(request):
    return render(request,'homefolder/Viewpage1.html')

#home bakers register page is connected to database
def Hreg(request):
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
            if Home_Tb.objects.filter(Businessname=Businessname).exists():
                messages.info(request,'Businessname already exists')
            elif Home_Tb.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            elif Home_Tb.objects.filter(Pannumber=panno).exists():
                messages.info(request,'Pannumber already exists')
            elif Home_Tb.objects.filter(Phone=phone).exists():
                messages.info(request,'Phonenumber already exists')
            else:
                userdata=Home_Tb(Firstname=firstname,Lastname=lastname,Businessname=Businessname,Businesstype=businesstype,
                Pannumber=panno,Address=address,Phone=phone,Email=email,Password= p1,Aadharcard=aadharcard,Businessimage=busimg)
                userdata.save()
                return redirect("Hlog")
       else:
             messages.info(request,'password not match') 
    return render(request,"homefolder/Hreg.html")   


#home bakers login page is connected to database
def Hlog(request):
    if request.method=="POST":
       try: 
            uname=request.POST.get("uname")
            password=request.POST.get("pwd")
            hlogin=Home_Tb.objects.get(Businessname=uname,Password=password)
            request.session['uname']=hlogin.Businessname
            request.session['id']=hlogin.id
            return redirect("Hpage")

       except Home_Tb.DoesNotExist as e:

            messages.info(request,'invalid username/password') 
    return render(request,'homefolder/Hlog.html')

#
def Addcategh(request):
    if request.method=="POST":
       cname=request.POST.get("cname")
       hid=request.POST.get("hid")
       categsave=categ(name=cname,BakeryId_id=hid)
       categsave.save()
       return redirect("Hpage")
    return render(request,'homefolder/Addcategh.html')

#
def Addpro(request):
    if request.method=="POST":
       name=request.POST.get("Name")
       descrption=request.POST.get("Desc")
       price=request.POST.get("Price")
       avail=request.POST.get("avail")
       img=request.FILES.get("img")  
       cid=request.POST.get("cid")
       bid=request.POST.get("bid")
       addsave=Products(name=name,desc=descrption,price=price,
       img=img,category_id=cid,BakeryId_id=bid,available=avail)
       addsave.save()
       return redirect("Hpage")
    categid=categ.objects.filter(BakeryId=request.session['id'])
    return render(request,'homefolder/Addpro.html',{'cid':categid})


def Viewpage(request):
    proview=Products.objects.filter(BakeryId=request.session['id'])
    return render(request,'homefolder/Viewpage.html',{'prodh':proview})

def proddetail(request,prodid):
    detail=Products.objects.get(id=prodid)
    return render(request,'homefolder/prodD.html',{'det':detail})

def produpdate(request,id):
    prodh=Products.objects.get(id=id)
    form = Pforms(request.POST or None , instance=prodh)
    if form.is_valid():
        form.save()
        return render(request,'homefolder/prodD.html',{'det':prodh})
    return render(request,'homefolder/produpdate.html',{'prod':prodh,'form':form})

def delete(request,pid):
    prodh = Products.objects.get(id=pid)
    if request.method == "POST":
        prodh.delete()
        pro=Products.objects.filter(BakeryId=request.session['id'])
        return render(request,'homefolder/Viewpage.html',{'prodh':pro})
    return render(request,'homefolder/delete.html',{'prodh':prodh})



def profile(request):
    hid=request.session['id']
    prof=Home_Tb.objects.get(id=hid)
    return render(request,'homefolder/profile.html', {'prof':prof})

def logout(request):
    return redirect('/')


def category(request):
    cat=categ.objects.filter(BakeryId=request.session['id'])
    return render(request,'homefolder/category.html',{'cat':cat})


def deletec(request,ctid):
    cath = categ.objects.get(id=ctid)
    if request.method == "POST":
        cath.delete()
        return redirect("Hpage")
    return render(request,'homefolder/deletec.html',{'cath':cath})

def vieworders(request,pk):
    hcrt=HCart.objects.filter(home=pk)
    delivery=notification.objects.filter(home=request.session['id'])
    return render(request,'homefolder/vieworders.html',{'hcrt':hcrt,'d':delivery})

def confirmpayment(request,pk):
    HCart.objects.filter(id=pk).update(status=True)
    hcrt=HCart.objects.filter(home=request.session['id'])
    return render(request,'homefolder/vieworders.html',{'hcrt':hcrt})

def editpro(request,id):
    edit=Home_Tb.objects.get(id=id)
    eform = Eforms(request.POST or None , instance=edit)
    if eform.is_valid():
        eform.save()
        return redirect("Hpage")
    return render(request,'homefolder/editproh.html',{'pro':edit,'forms':eform})

def deliveryD(request):
    if request.method == 'POST':
       name=request.POST.get("name")
       phno=request.POST.get("phno")
       adr=request.POST.get("adr") 
       pname=request.POST.get("pname") 
       price=request.POST.get("price") 
       hid=request.POST.get("hid") 
       user=request.POST.get("uid") 
       ds=notification(username=name,contactno=phno,address=adr,
       prdname=pname,price=price,home_id=hid,user_id=user)
       ds.save()
    hcart=HCart.objects.filter(home=request.session['id'])
    return render(request,'homefolder/deliverydetails.html',{'d':hcart})



