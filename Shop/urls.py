from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StoreHomePage, name='StoreHomePage'),
    path('inventory', views.inventory, name='inventory'),
    path('add_prod', views.add_prod, name='add_prod'),
    path('delete_prod', views.delete_prod, name='delete_prod'),
    path('update_prod', views.update_prod, name='update_prod'),
    path('Stores', views.shopView, name='Stores'),
    path('GoToStore', views.GoToStore, name='GoToStore'),

]
