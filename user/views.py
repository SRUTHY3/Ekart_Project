from django.shortcuts import render,redirect
from demo.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
from bakery_shop.models import *
from home_bakers.models import *
from . models import *
from itertools import chain
from django.contrib import messages
import razorpay
from . forms import *
from delivery_boy . models import notification
# Create your views here.
global amount
amount=0
def userpage(request):
    return render(request,'userfolder/userpage.html')

def hbprod(request):
    return render(request,'userfolder/home/hbprod.html')
def bsprod(request):
    return render(request,'userfolder/bakery/bsprod.html')
  
   
def Ureg(request):
    global p2
    if request.method=="POST":
       firstname=request.POST.get("First_Name")
       lastname=request.POST.get("last_Name")
       username=request.POST.get("User_Name")
       address=request.POST.get("address")
       phone=request.POST.get("phoneNumber")
       email=request.POST.get("email")
       p1=request.POST.get("password")
       p2=request.POST.get("Conform_Password")
       gender=request.POST.get("gender")
       
       if p1==p2:
            if User_Tb.objects.filter(Usernames=username).exists():
                messages.info(request,'Username already exists')
            elif User_Tb.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            elif User_Tb.objects.filter(Phone=phone).exists():
                messages.info(request,'Phone Number already exists')
            else:
                userdata=User_Tb(Firstname=firstname,Lastname=lastname,Usernames=username,Address=address,Phone=phone,Email=email,Password= p1,Gender=gender)
                userdata.save()
                return redirect("Ulog")
       else:
             messages.info(request,'password not match') 
    return render(request,"userfolder/Ureg.html")   


def Ulog(request):
    if request.method=="POST":
       try: 
            uname=request.POST.get("uname")
            password=request.POST.get("pwd")
            ulogin=User_Tb.objects.get(Usernames=uname,Password=password)
            request.session['uname']=ulogin.Usernames
            request.session['id']=ulogin.id
            return redirect("userpage")

       except User_Tb.DoesNotExist as e:

            messages.info(request,'invalid username/password') 

    return render(request,'userfolder/Ulog.html')

def logout(request):
    return redirect('/')
    
#
def profile(request):
    uid=request.session['id']
    prof=User_Tb.objects.get(id=uid)
    return render(request,'userfolder/profile.html', {'prof': prof})
#BAKER SHOP

def bslist(request):
    bs=Bakery_Tb.objects.all()
    return render(request,'userfolder/bakery/bslist.html',{'bs':bs})   

def bsview(request,id):
    bsv=Bakery_Tb.objects.get(id=id)
    return render(request,'userfolder/bakery/bkDview.html',{'bsv':bsv})   

def bsprodV(request,pk):
    bsprdv=Product.objects.filter(BakeryId=pk)
    return render(request,'userfolder/bakery/bsprodV.html',{'bsprdv':bsprdv})  

#Home Bakers
def hblist(request):
    hb=Home_Tb.objects.all()
    return render(request,'userfolder/home/hblist.html',{'hb':hb})

def hbview(request,id):
    hbv=Home_Tb.objects.get(id=id)
    return render(request,'userfolder/home/hbDview.html',{'hbv':hbv})   
    

def hbprodV(request,pk):
    hbprdv=Products.objects.filter(BakeryId=pk)
    return render(request,'userfolder/home/hbprodV.html',{'hbprdv':hbprdv})  

def Bprodview(request,id):
    if request.method=="POST":
       pname=request.POST.get("pname")
       price=request.POST.get("price")
       img=request.POST.get("img")
       bid=request.POST.get("bid")
       uid=request.POST.get("uid")
       cart=BCart(pname=pname,price=price,image=img,bakers_id=bid,user_id=uid)
       cart.save()
       messages.info(request,'Item Added Successfully') 
       return redirect('userpage')
    prodv=Product.objects.get(id=id)
    return render(request,'userfolder/bakery/prodDV.html',{'pv':prodv})  

def hprodview(request,id):
    if request.method=="POST":
       pname=request.POST.get("pname")
       price=request.POST.get("price")
       img=request.POST.get("img")
       bid=request.POST.get("bid")
       uid=request.POST.get("uid")
       cart=HCart(pname=pname,price=price,image=img,home_id=bid,user_id=uid)
       cart.save()
       return redirect('userpage')
    prodv=Products.objects.get(id=id)
    return render(request,'userfolder/home/prodDV.html',{'hv':prodv})   

def cart(request,pk):
    hcrt=HCart.objects.filter(user=pk,paystatus=False)
    bcrt=BCart.objects.filter(user=pk,paystatus=False)
    add=0
    temp1=0
    temp2=0
    tot=0
    global amount
    both=list(chain(hcrt , bcrt))
    if both:
        for i in hcrt:
            temp1 += i.price
        for j in bcrt:
            temp2 += j.price
        tot= temp1 + temp2
        amount=tot
    elif bcrt:
        for i in bcrt:
            add += i.price
        tot=add
        amount=tot
        # return redirect("pay")
    elif hcrt:
        for i in hcrt:
            add += i.price
        tot=add
        amount=tot
    return render(request,'userfolder/home/cart.html',{'hcrt':hcrt,'bcrt':bcrt,'sum':tot})

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def pay(request):
      global amount
      print(amount)
      currency ="INR"
      api_key=RAZORPAY_API_KEY
      amt=int(amount)*100
      payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
      payment_order_id= payment_order['id'] 
      return render(request,'userfolder/home/pay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})


def cartdel(request,id):
    cath = HCart.objects.get(id=id)
    if request.method == "POST":
        cath.delete()
        return redirect("userpage")
    return render(request,'userfolder/cartdel.html')


def cdel(request,id):
    cath = BCart.objects.get(id=id)
    if request.method == "POST":
        cath.delete()
        return redirect("userpage")
    return render(request,'userfolder/cartdel.html')

def thank(request):
    return render(request,'userfolder/home/hbthank.html')

def vieworders(request,pk):
    hcrt=HCart.objects.filter(user=pk)
    bcrt=BCart.objects.filter(user=pk)
    return render(request,'userfolder/home/vieworders.html',{'hcrt':hcrt,'bcrt':bcrt,})


def editpro(request,id):
    edit=User_Tb.objects.get(id=id)
    eform = Uforms(request.POST or None , instance=edit)
    if eform.is_valid():
        eform.save()
        return redirect("userpage")
    return render(request,'userfolder/home/editpro.html',{'pro':edit,'forms':eform})

def afterpayment(request):
    h=HCart.objects.filter(user=request.session['id'])
    b=BCart.objects.filter(user=request.session['id'])
    return render(request,'userfolder/afterpayment.html',{'h':h,'b':b})

def generatebill(request):
    if request.method=="POST":
         HCart.objects.filter(user=request.session['id']).update(paystatus=True)
         BCart.objects.filter(user=request.session['id']).update(paystatus=True)
         h=HCart.objects.filter(user=request.session['id'])
         b=BCart.objects.filter(user=request.session['id'])
    return render(request,'userfolder/afterpayment.html',{'h':h,'b':b})

def deliveryD(request):
    delivery=notification.objects.filter(user=request.session['id'])
    return render(request,'userfolder/deliveryD.html',{'d':delivery})
