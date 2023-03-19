from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError


from .filters import ListingFilter


client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# Create your views here.
def index(request):
    category_name=category.objects.all()
    buyer_name=buyer.objects.all()
    listing=Product.objects.all()
    listing.reverse()
    Z=listing[0:5]
    context={
        "cat_name":category_name,
        'buyer':buyer_name,
        'product':Z

        }
    return render(request, "home.html",context)



def view_product(request,pid):
    iteam=Product.objects.get(id=pid)
    photos=Photos.objects.filter(p_id=pid)
    Size=iteam.size.all()
    Color=iteam.color.all()
    curent_price=iteam.price-(iteam.price*(iteam.off/100))
    context={
        "product":iteam,
        'Photos':photos,
        'price':curent_price,
        'S':Size,
        'C':Color,
        

        }
    return render(request,'productdetails.html',context)



def add_product(request):
    category_name=category.objects.all()
    buyer_name=buyer.objects.all()
    color_name=color.objects.all()
    size_name=size.objects.all()
    Availability=availability.objects.all()
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    if request.method == 'POST':
        product_id=request.POST['pid']+'_'+str(user_id)
        name= request.POST['productname']
        Type= buyer.objects.get(id=request.POST['Buyer_Type'])
        Category= category.objects.get(id=request.POST['Catgoery'])
        profile_photo=request.FILES.get('profilephoto')
        Size=request.POST.getlist('size')
        Color=request.POST.getlist('Color')
        description=request.POST['Specification']
        price=request.POST['Price']
        off=request.POST['Offer']
        posted_by=user
        stock= availability.objects.get(id=request.POST['Avalibility'])
        
        try:
            p=Product.objects.create(id=product_id,name= name,buyer=Type,category=Category,image=profile_photo,description=description,price=price,off=off,posted_by=posted_by,availability=stock)
                
            size_list=[]
            color_list=[]
            aproduct = Product.objects.get(id=product_id)
            for i in Size:
                x= size.objects.get(id=i)
                aproduct.size.add(x)

            for i in Color:
                x= color.objects.get(id=i)
                aproduct.color.add(x)
                
                
                
            imges = request.FILES.getlist('photos')
                
            for image in imges:
                Photos.objects.create(images=image,p_id= aproduct)

                return redirect('seller_home')
        except IntegrityError:
            return render(request,'addproduct.html',{'message':'That product ID already exists'})
    
    context={
        "cat_name":category_name,
        'Size':size_name,
        'buyer':buyer_name,
        'color':color_name,
        'Availability':Availability

        }
    return render(request, "addproduct.html",context)


def product_view(request,id=0,choice=0):
    if choice==1:
        B = buyer.objects.filter(id=id)
        listing=Product.objects.filter(buyer=B[0])
    elif choice==2:
        B = category.objects.filter(id=id)
        listing=Product.objects.filter(category=B[0])
    elif choice==3:
        listing=Product.objects.all()
    
    listing_filter=ListingFilter(request.GET,queryset=listing)
    
    context={
        'listing_filter':listing_filter
        
        }
    return render(request,'productgallary.html',context)


def Loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            if request.user.is_staff:
                return redirect('seller_home')
            else:
                return redirect('index')
        else:
            return redirect('Loginpage')
    return render(request,'auth.html')


def Signuppage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('con_password')
        as_a=request.POST.get('as_a')
        if pass1 != pass2:
            return render(request,'auth.html',{'message':'password and confirm password does not match'})


        try:
            if as_a=='Seller':
                customer = User.objects.create_user(username,email,pass1,is_staff=True)
                customer.save()
                return redirect('Loginpage')
            else:
                customer = User.objects.create_user(username,email,pass1)
                customer.save()
                return redirect('Loginpage')
        except IntegrityError:
            return render(request,'auth.html',{'message':'The User already exists'})
        

        
    
    return render(request,'auth.html')

def handllogout(request):
    logout(request)
    return redirect('index')

# cart------------------------
@login_required(login_url="Loginpage")
def cartadd(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    if request.method == 'POST':
        pro_id=request.POST['pid']
        color=request.POST['color']
        size=request.POST['size']
        price=request.POST['price']
        profile_photo=request.POST['pic']
        product = Product.objects.get(id=pro_id)
        cart_iteam=shopingCart.objects.filter(user=user,Product=product)

        if len(cart_iteam)==0:
            shopingCart(user=user,Product=product,quntity=1,color=color,size=size,price=price,total_price=price,image=profile_photo).save()
        else:
            x=cart_iteam[0].quntity+1
            t_price=cart_iteam[0].price*x
            cart_iteam[0].quntity=x
            cart_iteam[0].total_price=t_price
            cart_iteam[0].save()
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="Loginpage")
def cartdetail(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    cart_iteam=shopingCart.objects.filter(user=user)
    amount=0
    for i in cart_iteam:
        amount=i.total_price+amount
    context={
        'cart_list':cart_iteam,
        'amount':amount,
        'cart_count':len(cart_iteam),
        
        }
    return render(request, 'cart.html',context)

@login_required(login_url="Loginpage")
def itemincrement(request):
    if request.method == 'POST':
        pro_id=request.POST['pid']
        user_id=request.user.id
        user =User.objects.get(id=user_id)
        product = Product.objects.get(id=pro_id)
        cart_iteam=shopingCart.objects.filter(user=user,Product=product).first()
        
        x=cart_iteam.quntity+1
        t_price=cart_iteam.price*x
        cart_iteam.quntity=x
        cart_iteam.total_price=t_price
        cart_iteam.save()
        
            
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="Loginpage")
def itemdecrement(request):
    if request.method == 'POST':
        pro_id=request.POST['pid']
        user_id=request.user.id
        user =User.objects.get(id=user_id)
        product = Product.objects.get(id=pro_id)
        cart_iteam=shopingCart.objects.filter(user=user,Product=product)
        if len(cart_iteam)!=0:
            x=cart_iteam[0].quntity-1
            t_price=cart_iteam[0].price*x
            cart_iteam[0].quntity=x
            cart_iteam[0].total_price=t_price
            cart_iteam[0].save()
        
            
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="Loginpage")
def itemclear(request):
    if request.method == 'POST':
        pro_id=request.POST['pid']
        user_id=request.user.id
        user =User.objects.get(id=user_id)
        product = Product.objects.get(id=pro_id)
        cart_iteam=shopingCart.objects.get(user=user,Product=product)
        # cart_iteam=shopingCart.objects.filter(user=user,Product=product)
        cart_iteam.delete()
        
            
    
    return redirect(request.META['HTTP_REFERER'])
    # ----------------------------------


@login_required(login_url="Loginpage")
def wishlistdetail(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    cart_iteam=wish_list.objects.filter(user=user)
    context={
        'cart_list':cart_iteam,
        'item_count':len(cart_iteam),
        
        }
    return render(request, 'wishlist.html',context)


@login_required(login_url="Loginpage")
def whishlistadd(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    if request.method == 'POST':
        pro_id=request.POST['pid']
        product = Product.objects.get(id=pro_id)
        cart_iteam=wish_list.objects.filter(user=user,Product=product)

        if len(cart_iteam)==0:
            wish_list(user=user,Product=product).save()
        
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="Loginpage")
def whis_itemclear(request):
    if request.method == 'POST':
        pro_id=request.POST['pid']
        user_id=request.user.id
        user =User.objects.get(id=user_id)
        product = Product.objects.get(id=pro_id)
        cart_iteam=wish_list.objects.get(user=user,Product=product)
        cart_iteam.delete()
        
            
    
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="Loginpage")
def checkout(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    product = shopingCart.objects.filter(user=user)
    total_amount=0
    for i in product:
        total_amount=i.total_price+total_amount
    amount=int(total_amount)

    
    context={
        'amount':total_amount,
        'product_list':product,
        
        }
    return render(request, 'orderplace.html',context)

@login_required(login_url="Loginpage")
def orderupdate(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    cart_iteam=shopingCart.objects.filter(user=user)
    
    total_amount=0
    for i in cart_iteam:
        total_amount=i.total_price+total_amount
    amount=int(total_amount)

    payment=client.order.create({

        "amount": amount*100, 
        "currency": "INR",
        "payment_capture":"1"

        })
    order_id=payment['id']

    if request.method == 'POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        country=request.POST['country']
        addres=request.POST['addres']
        city=request.POST['city']
        state=request.POST['state']
        postcode=request.POST['pcode']
        phone=request.POST['phone']
        email=request.POST['email']
        additional_info=request.POST['addinfo']
        
        order=Order(user=user,firstname=firstname,lastname=lastname,contry=country,address=addres,city=city,state=state,postcode=postcode,phone=phone,email=email,additional_info=additional_info,amount=amount,payment_id=order_id)
        order.save()
        orderid=Order.objects.get(id=order.id)
        

        for i in cart_iteam:
            order=Orderiteam(order=orderid,product=i.Product,image=i.Product.image,quantity=i.quntity,price=i.price,total=i.total_price)
            order.save()
        
        
    context={
        
        'cart_list':cart_iteam,
        'amount':amount,
        'order_id':order_id,
        'cart_count':len(cart_iteam),
        }
    return render(request, 'orderiteams.html',context)


@csrf_exempt
def success(request):
    if request.method == 'POST':
        a=request.POST
       
                
        x=a['razorpay_order_id']   
        user=Order.objects.filter(payment_id=x).first()
        user.paid=True
        user.save()
        user_id=request.user.id
        user =User.objects.get(id=user_id)
        cart_iteam=shopingCart.objects.filter(user=user)
        cart_iteam.delete()
    return render(request, 'paymentsuccess.html')



def sellerhome(request,id):
    user_id=request.user.id
    user =User.objects.get(id=id)
    produtc_list=Product.objects.filter(posted_by=user)
    seller=Seller.objects.get(user=user)

    context={
        "product":produtc_list,
        'seller':seller,
    }

    return render(request, 'sellerhome.html',context)

@login_required(login_url="Loginpage")
def seller_home(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    produtc_list=Product.objects.filter(posted_by=user)
    seller=Seller.objects.filter(user=user).first()

    context={
        "product":produtc_list,
        'seller':seller,
    }

    return render(request, 'seller_home.html',context)

@login_required(login_url="Loginpage")
def seller_reg(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    seller=Seller.objects.filter(user=user).first()
    return render(request, 'seller_reg.html',{'context':seller})

# def seller_account(request):
#     return render(request, 'seller_reg.html')

@login_required(login_url="Loginpage")
def update_profile(request):
    user_id=request.user.id
    user =User.objects.get(id=user_id)
    if request.method == 'POST':
        name=request.POST['name']
        image=request.FILES.get('profilephoto')
        bio=request.POST['bio']
        address=request.POST['address']
        whatsapp_number=request.POST['w_number']
        phone_number=request.POST['c_number']
        insta=request.POST['intsa_id']
        facebook=request.POST['fb']
        youtoob=request.POST['youtube']
        pinterest=request.POST['pin_terst']
        web=request.POST['web']
        seller=Seller.objects.filter(user=user)

        if len(seller) == 0:
            profile=Seller(user=user,name=name,image=image,bio=bio,address=address,whatsapp_number=whatsapp_number,phone_number=phone_number,insta=insta,facebook=facebook,youtoob=youtoob,pinterest=pinterest,web=web)
            profile.save()
            return redirect('seller_home')
        else:
            seller[0].name=name
            seller[0].bio=bio
            seller[0].address=address
            seller[0].whatsapp_number=whatsapp_number
            seller[0].phone_number=phone_number
            seller[0].insta=insta
            seller[0].facebook=facebook
            seller[0].youtoob=youtoob
            seller[0].pinterest=pinterest
            seller[0].web=web
            if image:
                seller[0].image=image
            seller[0].save()
            return redirect('seller_home')
            
        
    return render(request, 'seller_reg.html')

@login_required(login_url="Loginpage")
def updateproduct(request,pid):
    product=Product.objects.get(id=pid)
    photos=Photos.objects.all()
    category_name=category.objects.all()
    buyer_name=buyer.objects.all()
    color_name=color.objects.all()
    size_name=size.objects.all()
    Availability=availability.objects.all()
    user_id=request.user.id
    user =User.objects.get(id=user_id)

    context={
        "product":product,
        'photos':photos,
        "cat_name":category_name,
        'Size':size_name,
        'buyer':buyer_name,
        'color':color_name,
        'Availability':Availability
        
    }

    return render(request, 'update_product.html',context)

@login_required(login_url="Loginpage")
def update_product(request):
    
    if request.method == 'POST':
        pid=request.POST['pid']
        price=request.POST['Price']
        off=request.POST['Offer']
        stock= availability.objects.get(id=request.POST['Avalibility'])
        product=Product.objects.get(id=pid)



        product.price=price
        product.off=off
        product.availability=stock

        product.save()

        return redirect('seller_home')
        
        
    return render(request, 'update_product.html')


@login_required(login_url="Loginpage")
def delete_product(request,pid):
    product=Product.objects.get(id=pid)

    product.delete()
    return redirect('seller_home')






