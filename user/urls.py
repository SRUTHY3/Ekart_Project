from django.urls import path
from . import views

urlpatterns = [
   path('Ureg', views.Ureg, name='Ureg'),
   path('Ulog', views.Ulog, name='Ulog'),
   path('logout', views.logout, name='logout'),
   path('userpage', views.userpage, name='userpage'),


   path('bslist', views.bslist, name='bslist'),
   path('bsv/<int:id>', views.bsview, name='bsv'),
   path('bsp/<str:pk>', views.bsprodV, name='bsprodV'),
   path('bprdview/<int:id>', views.Bprodview, name='bprdview'),
   path('hprdview/<int:id>', views.hprodview, name='hprdview'),


   path('cart/<str:pk>',views.cart,name='cart'),
   path('cartdel<int:id>',views.cartdel,name='cartdel'),
   path('cdel<int:id>',views.cdel,name='cdel'),


   path('hblist', views.hblist, name='hblist'),
   path('hbv/<int:id>', views.hbview, name='hbv'),
   path('hbp/<str:pk>', views.hbprodV, name='hbprodV'),

   
   path('hbprod', views.hbprod, name='hbprod'),
   path('bsprod', views.bsprod, name='bsprod'),
   path('pay', views.pay, name='pay'),
   path('thank', views.thank, name='thank'),
   path('profile',views.profile,name='profile'),

   
   path('Vorders/<str:pk>',views.vieworders,name='Vorders'),
   path('ueditpro/<int:id>', views.editpro, name='ueditpro'),
   path('afterpayment', views.afterpayment, name='afterpayment'),
   path('generatebill', views.generatebill, name='generatebill'),
   path('deliveryD', views.deliveryD, name='deliveryD'),






]
  
  
