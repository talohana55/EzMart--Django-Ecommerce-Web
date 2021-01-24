from django.db import models
from accounts.models import Account


FORM_STATUS = (
    ('O', 'Open'),
    ('C', 'Closed'),
)


class Form(models.Model):
    name     = models.CharField(max_length=30, default='')
    email         = models.EmailField(max_length=254)
    subject       = models.CharField(max_length=30)
    message       = models.TextField()
    status        = models.CharField(choices=FORM_STATUS, max_length=2, default = 'O')
    date_created  = models.DateTimeField(verbose_name='date created', auto_now_add=True)

    def __str__(self):
        return self.name
