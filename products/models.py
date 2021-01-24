from django.db import models
from Shop.models import Store
from django.core.files.base import ContentFile

CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Food Stuff', 'Food Stuff'),
    ('Tools', 'Tools'),
    ('Other','Other'),
)


class ProductManager(models.Manager):

    def __str__(self):
        return self.title



class Product(models.Model):
    title        = models.CharField(max_length=100, default ='Product name here')
    price        = models.FloatField(default=0)
    category     = models.CharField(choices=CATEGORY_CHOICES, max_length=222,blank= True)
    store        = models.ForeignKey(Store, models.SET_NULL,blank= True, null= True)
    description  = models.CharField(max_length=500 , default ='Description name here')
    active       = models.BooleanField(default= True)
    time_stamp   = models.DateTimeField(verbose_name="Time Stamp",auto_now=True)
    quantity     = models.IntegerField(default=0)
    img          = models.ImageField(null=True,blank=True,upload_to="static/images")
    objects      = ProductManager()

    def __str__(self):
        return self.title

