from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class buyer(models.Model):
    name=models.TextField(max_length=25, null=True,blank=True)
    photo=models.ImageField(upload_to='images',blank=True)

    def __str__(self):
        return self.name
    

class category(models.Model):
    name=models.TextField(max_length=25, null=True,blank=True)
    buyer =models.ForeignKey(buyer, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='images',blank=True)



    def __str__(self):
        return self.name

class color(models.Model):
    name=models.TextField(max_length=25, null=True,blank=True)


    def __str__(self):
        return self.name

class size(models.Model):
    name=models.TextField(max_length=25, null=True,blank=True)


    def __str__(self):
        return self.name
    
class availability(models.Model):
    name=models.TextField(max_length=5, null=True,blank=True)


    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.TextField(primary_key=True,unique=True)
    name=models.TextField(max_length=25, null=True,blank=True)
    buyer= models.ForeignKey(buyer, on_delete=models.CASCADE)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images',blank=True)
    size=models.ManyToManyField('size')
    color=models.ManyToManyField('color')
    description=models.TextField(max_length=100, null=True,blank=True)
    price= models.FloatField(null=True,blank=True)
    off= models.IntegerField(null=True,blank=True)
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    availability=models.ForeignKey(availability, on_delete=models.CASCADE)

    

class Photos(models.Model):
    p_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    images = models.FileField(null=True,blank=True)


class shopingCart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quntity=models.IntegerField(null=True,blank=True)
    color=models.TextField(max_length=25, null=True,blank=True)
    size=models.TextField(max_length=25, null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    total_price=models.FloatField(null=True,blank=True)
    image=models.ImageField(upload_to='images',blank=True)

class wish_list(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    contry=models.CharField(max_length=100)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    postcode=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    additional_info=models.TextField(null=True,blank=True)
    payment_id=models.CharField(max_length=300,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    amount=models.CharField(max_length=1000)
    date=models.DateField(auto_now_add=True)

    
    
    
class Orderiteam(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images',blank=True)
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=50)
    total=models.CharField(max_length=1000)

    def __str__(self):
        return self.order.user.username
    
class Seller(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images',blank=True)
    bio=models.TextField(null=True,blank=True)
    whatsapp_number=models.IntegerField()
    phone_number=models.IntegerField()
    address=models.TextField()
    insta=models.CharField(max_length=200,null=True,blank=True)
    facebook=models.CharField(max_length=200,null=True,blank=True)
    youtoob=models.CharField(max_length=200,null=True,blank=True)
    pinterest=models.CharField(max_length=200,null=True,blank=True)
    web=models.CharField(max_length=200,null=True,blank=True)