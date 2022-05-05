from django.urls import path
from . import views

urlpatterns = [
   path('hbcart', views.hbcart, name='hbcart'),
   path('hbpay', views.hbpay, name='hbpay'),
   path('hbthank', views.hbthank, name='hbthank'),
   path('bscart', views.bscart, name='bscart'),
   path('bspay', views.bspay, name='bspay'),
   path('bsthank', views.bsthank, name='bsthank')

   
]
