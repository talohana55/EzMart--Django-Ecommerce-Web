from django.urls import path,include
from . import views

urlpatterns = [  
 path('receipts', views.receipts, name='receipts'),

]
