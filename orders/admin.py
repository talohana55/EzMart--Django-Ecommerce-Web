from django.contrib import admin

# Register your models here.
from orders.models import OrderedItem

admin.site.register(OrderedItem)