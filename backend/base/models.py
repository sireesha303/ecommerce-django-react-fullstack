from django.db import models
from django.contrib.auth.models import User
import uuid


class Product(models.Model):
    """Product model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200,null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(upload_to='images')
    brand = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    rating = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    count_in_stock = models.IntegerField(default=0, null=True, blank=True)
    num_reviews = models.IntegerField(default=0,null=True, blank=True )

    def __str__(self):
        return self.name


class Review(models.Model):
    """Review Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    rating =  models.IntegerField(default=0, null=True, blank=True )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_method = models.CharField(max_length=100,null=False, blank=False)
    tax_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField( null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return str(self.created_at)


class OrderItem(models.Model):
    """Order Item model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class ShippingAddress(models.Model):
    """Shipping Address Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=False)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)

    def __str__(self):
        return self.address


