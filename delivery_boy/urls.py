from django.urls import path
from . import views

urlpatterns = [
   path('Dreg', views.Dreg, name='Dreg'),
   path('Dlog', views.Dlog, name='Dlog'),
   path('Dpage', views.Dpage, name='Dpage'),
   path('profile',views.profile,name='profile'), 
   path('logout', views.logout, name='logout'),
   path('Detail<str:pk>', views.detailsD, name='Detail'),
   path('editpro/<int:id>', views.editpro, name='editpro'),

   path('neworder<str:pk>',views.neworder,name="neworder"),
   path('ordrstat<str:pk>',views.orderstat,name="ordrstat"),

    
   
]
