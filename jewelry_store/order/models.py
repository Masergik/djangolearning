from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Order(models.Model):
    description = models.TextField()
    date_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client')
    employee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='employee')
    delivery_method = models.ForeignKey('order.Delivery', on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey('order.Payment', on_delete=models.SET_NULL, null=True)


class Delivery(models.Model):
    method = models.CharField(max_length=255)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=14)


class Payment(models.Model):
    method = models.CharField(max_length=255)


class OrderStatus(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    status_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class OrderBasket(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.SET_NULL, null=True)
    product_name = models.ForeignKey('store.Product', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    store_quantity = models.ForeignKey('store.Store', on_delete=models.CASCADE)
