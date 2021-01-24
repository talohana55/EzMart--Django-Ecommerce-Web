from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator
from Shop.models import Store


USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'


ACCOUNT_TYPES = (
        ('A', 'Admin'),
        ('B', 'Business'),
        ('C', 'Customer'),
    )


class MyAccManager(BaseUserManager):
    def create_user(self,username,email,first_name,last_name,address,phone,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        user = self.model(
            username = username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone
        ) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,email,password=None):
        user = self.create_user(
            username = username,
            email=self.normalize_email(email),
            first_name='Admin',
            last_name='Admin',
            address='',
            phone='',
            password = password,
           
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.acc_type = 'A' 
        user.save(using=self._db)
        return user
    def create_business_user(self,email,first_name,last_name,address,phone,username,password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            password = password,
        )
        user.acc_type = 'B' 
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username                    = models.CharField(
        max_length=300,
        validators = [
            RegexValidator(regex = USERNAME_REGEX,
            message='Username must be alphanumeric or contain numbers',
            code='invalid_username'
            )],
         unique=True)
    email                    = models.EmailField(max_length=255,unique=True,verbose_name="email address")
    data_joined              = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login               = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                 = models.BooleanField(default=False)
    is_active                = models.BooleanField(default=True)
    is_staff                 = models.BooleanField(default=False)
    is_superuser             = models.BooleanField(default=False)
    first_name               = models.CharField(max_length=30, default='')
    last_name                = models.CharField(max_length=30, default='')
    address                  = models.CharField(max_length=150, default='')
    phone                    = models.CharField(max_length=14, default='')
    acc_type                 = models.CharField(max_length=2, choices = ACCOUNT_TYPES , default = 'C')  
    store                    = models.OneToOneField(Store, null= True,blank = True, default= None, on_delete=models.CASCADE)


    objects = MyAccManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
