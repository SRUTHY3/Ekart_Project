from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('regas', views.regas, name='regas'),
   path('logas', views.logas, name='logas')
]
