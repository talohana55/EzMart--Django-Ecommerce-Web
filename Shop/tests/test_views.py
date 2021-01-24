from django.test import TestCase, Client
from django.urls import reverse
import json
from Shop.models import StoreManager, Store


class TestViewsOrders(TestCase):

    def setUp(self):
        self.client = Client() 

    def test_EZMart_StoreHomePage_GET(self):   
        response = self.client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_EZMart_add_prod_GET(self):
        response = self.client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_EZMart_delete_prod_GET(self):
        response = self.client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_EZMart_update_prod_GET(self):
        response = self.client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_EZMart_Inventory_GET(self):
        response = self.client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')
