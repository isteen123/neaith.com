from django.contrib import admin
from .models import *
# Register your models here.


class Scategory(admin.ModelAdmin):
    list_display = ('id','name','buyer', 'photo')

class Sproduct(admin.ModelAdmin):
    list_display = ('id','name','buyer','category','image','description','price','off','posted_by','availability')

class SPhotos(admin.ModelAdmin):
    list_display = ('id','p_id','images')

class Sbuyer(admin.ModelAdmin):
    list_display = ('id','name','photo')

class Scolor(admin.ModelAdmin):
    list_display = ('id','name')

class Ssize(admin.ModelAdmin):
    list_display = ('id','name')


class Savailability(admin.ModelAdmin):
    list_display = ('id','name')
class swhishlist(admin.ModelAdmin):
    list_display = ('user','Product')
class sShopingCart(admin.ModelAdmin):
    list_display = ('user','Product','quntity','color','size','price','total_price','image')

class SOrderiteam(admin.ModelAdmin):
    list_display = ('order','product','image','quantity','price','total')
class SOrder(admin.ModelAdmin):
    list_display = ('user','firstname','lastname','contry','address','city','state','postcode','phone','email','additional_info','amount','payment_id','paid','date')


admin.site.register(category, Scategory)
admin.site.register(Product, Sproduct)
admin.site.register(Photos, SPhotos)
admin.site.register(buyer, Sbuyer)
admin.site.register(color, Scolor)
admin.site.register(size, Ssize)
admin.site.register(wish_list, swhishlist)
admin.site.register(shopingCart, sShopingCart)
admin.site.register(availability, Savailability)
admin.site.register(Orderiteam, SOrderiteam)
admin.site.register(Order, SOrder)
