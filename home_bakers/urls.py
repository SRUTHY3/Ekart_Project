from django.urls import path
from . import views

urlpatterns = [
   path('Hreg',views.Hreg, name='Hreg'),
   path('Hlog',views.Hlog, name='Hlog'),
   path('hblist',views.hblist,name='hblist'),
   path('Hpage',views.Hpage,name='Hpage'),
   path('Addpro',views.Addpro,name='Addpro'),
   path('Viewpage',views.Viewpage,name='Viewpage'),
   path('prodD/<int:prodid>',views.proddetail,name='prodh'),
   path('addcategh',views.Addcategh,name='addcategh'),
   path('produph/<int:id>',views.produpdate,name='produph'), 
   path('deleteh/<int:pid>',views.delete,name='deleteh'), 
   path('profile',views.profile,name='profile'), 
   path('logout', views.logout, name='logout'),
   path('category', views.category, name='category'),
   path('deletec/<int:ctid>',views.deletec,name='deletec'),

   path('Vorder/<str:pk>',views.vieworders,name='Vorder'),
   path('Cpay/<str:pk>',views.confirmpayment,name='Cpay'),

   path('editproh/<int:id>', views.editpro, name='editproh'),

   path('hdeliveryD', views.deliveryD, name='hdeliveryD'),




     
]
