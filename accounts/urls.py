from django.urls import path, include
from . import views

urlpatterns = [
    path('registercustomer', views.registercustomer, name='registercustomer'),
    path('login', views.Login, name='login'),
    path("logout", views.logout, name="logout"),
    path('registerbusiness', views.registerbusiness, name='registerbusiness'),
    path('userProfile', views.userProfile, name='userProfile'),
    path('businessProfile', views.businessProfile, name='businessProfile'),
    path('ordersManage', views.ordersManage, name='ordersManage'),
    path('ship', views.ship, name='ship'),
    path('Business', views.Business, name='Business'),
    path('sellingreport', views.sellingreport, name='sellingreport'),
]
