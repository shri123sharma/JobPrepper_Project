from django.db import models
from article_app.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile",null=True,blank=True)
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    address=models.TextField(blank=True,null=True)
    date_of_birth=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"this is user profile{self.user}-{self.address}"
    

class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,null=True,blank=True,on_delete=models.CASCADE,related_name="product")
    stock_quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Product detail {self.name} with price {self.price}"


class Customer(models.Model):
    user_profile=models.OneToOneField(UserProfile,null=True,blank=True,on_delete=models.CASCADE,related_name="customer")
    loyalty_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"customer loyality point:-{str(self.loyalty_points)}"


class Order(models.Model):
    customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE,related_name="order")
    order_date=models.DateTimeField(auto_now_add=True)
    shipping_address=models.TextField()
    is_paid=models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.user_profile.user.username}"


class OrderItem(models.Model):
    order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.CASCADE,related_name="orderitem")
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE,related_name="product_order_item")
    quantity=models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order #{self.order.id}"


class Review(models.Model):
    customer=models.ForeignKey(Customer,null=True,blank=True,on_delete=models.CASCADE,related_name="customer_review")
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.CASCADE,related_name="product_review")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.customer.user_profile.user.username}"
    
    