from django.db import models


CATEGORY_CHOICES = (
    ('E', 'Electronics'),
    ('FS', 'Food Stuff'),
    ('T', 'Tools')
)


STORE_STATUSES = (
    ('C', 'Confirmed'),
    ('AC', 'Awaiting confirmation'),
    ('DC','Declined confimation'),
    ('B','Banned'),

)



class StoreManager(models.Manager):

    def __str__(self):
        return self.name

class Store(models.Model):
     name               = models.CharField(max_length=300)
     date_joined        = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
     address            = models.CharField(max_length=150, default='Store Address')
     status             = models.CharField(max_length=2,choices = STORE_STATUSES, default='AC')
     businessNum        = models.IntegerField(unique=True )
     phone              = models.IntegerField(default=0)
     category           = models.CharField(max_length=3,choices = CATEGORY_CHOICES)
     ranking            = models.IntegerField(default=0)
     logo_img           = models.ImageField(null=True,blank=True,upload_to="static/images/")
     facebook_url       = models.CharField(max_length=255,null=True,blank=True)
     instagram_url      = models.CharField(max_length=255,null=True,blank=True)
     twitter_url        = models.CharField(max_length=255,null=True,blank=True)

    #store_socials            = models.ManyToManyField(Social, on_delete=models.CASCADE)  # Store Links to twitter / facebook etc
     objects = StoreManager()
     def __str__(self):
        return self.name
   