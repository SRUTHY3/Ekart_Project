from django.contrib import admin
from .models import *

# Register your models here.
class Badmin(admin.ModelAdmin):
    list_display=['Firstname','Email']
admin.site.register(Bakery_Tb,Badmin)

class Cadmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,Cadmin)

class Padmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Product,Padmin)




