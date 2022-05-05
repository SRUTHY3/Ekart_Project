from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User_Tb)

class Hadmin(admin.ModelAdmin):
    list_display=['user','date','pname','price','status','home']
admin.site.register(HCart,Hadmin)

class Badmin(admin.ModelAdmin):
    list_display=['user','date','pname','price','status','bakers']
admin.site.register(BCart,Badmin)