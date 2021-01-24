from django.db import models
from accounts.models import Account


class OrderManager(models.Manager):
    def __str__(self):
        return self.product


class OrderedItem(models.Model):
    buyer_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(
        max_length=100, default='Product name here')
    shop_name = models.CharField(max_length=100, default='Store name here')
    buyer_name = models.CharField(max_length=100, default='Buyer name here')
    create_date = models.DateTimeField(
        verbose_name='date_sold', auto_now_add=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    product_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Awaiting Shipping")
    objects = OrderManager()

    def __str__(self):
        return self.product_name
