from django.urls import path
from . import views

urlpatterns =[
   path('Breg', views.Breg, name='Breg'),
   path('Blog', views.Blog, name='Blog'),
   path('Bpage',views.Bpage,name='Bpage'),
   path('AddproB',views.AddproB,name='AddproB'),
   path('ViewpageB',views.ViewpageB,name='ViewpageB'),
   path('prodD/<int:prodid>',views.proddetail,name='prod'),
   path('addcateg',views.Addcateg,name='addcateg'),
   path('produp/<int:id>',views.produpdate,name='produp'), 
   path('delete/<int:pid>',views.delete,name='delete'), 
   path('bprofile',views.profile,name='bprofile'),  
   path('logout', views.logout, name='logout'), 
   path('categorys', views.categorys, name='categorys'),
   path('deletecat/<int:ctyid>',views.deletecat,name='deletecat'),
   path('Vorder/<str:pk>',views.vieworders,name='Vordr'),
   path('conpay/<str:pk>',views.confirmpayment,name='conpay'),

   path('beditpro/<int:id>', views.editpro, name='beditpro'),

   path('deliveryD', views.deliveryD, name='deliveryD'),


]


