from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('product_view/<int:id>/<int:choice>', product_view,name='product_view'),
    path('add_product/', add_product,name='add_product'),
    path('view_product/<str:pid>', view_product,name='view_product'),
    path('Loginpage', Loginpage,name='Loginpage'),
    path('Signuppage', Signuppage,name='Signuppage'),
    path('handllogout', handllogout,name='handllogout'),
    
    path('', index,name='index'),

    #shopincart manullay

    path('cartadd/', cartadd, name='cartadd'),
    path('cartdetail/',cartdetail,name='cartdetail'),
    path('itemincrement/',itemincrement, name='itemincrement'),
    path('itemdecrement/',itemdecrement, name='itemdecrement'),
    path('itemclear/',itemclear, name='itemclear'),
    # whishlist------

    path('wishlistdetail/', wishlistdetail, name='wishlistdetail'),
    path('whishlistadd/', whishlistadd, name='whishlistadd'),
    path('whis_itemclear/', whis_itemclear, name='whis_itemclear'),

    # place order-----

    path('checkout/', checkout, name='checkout'),
    path('orderupdate/', orderupdate, name='orderupdate'),
    path('success/', success, name='success'),

    # seller------
    path('sellerhome/<int:id>/', sellerhome, name='sellerhome'),
    path('seller_home/', seller_home, name='seller_home'),
    path('seller_reg/', seller_reg, name='seller_reg'),
    path('update_profile', update_profile, name='update_profile'),
    
    path('updateproduct/<str:pid>', updateproduct, name='updateproduct'),
    path('update_product/', update_product, name='update_product'),
    path('delete_product/<str:pid>', delete_product, name='delete_product'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)