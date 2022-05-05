from django.contrib import admin
from .models import Delivery_Tb, notification

# Register your models here.
admin.site.register(Delivery_Tb)

class Nadmin(admin.ModelAdmin):
    list_display=['username','contactno','address','prdname','price','neworderstatus','orderStatus']
admin.site.register(notification,Nadmin)





