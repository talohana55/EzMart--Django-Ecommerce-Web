from django.test import TestCase, Client
from django.urls import reverse
import json
from products.models import ProductManager, Product


class TestViewsOrders(TestCase):

    def setUp(self):
        self.client = Client()  # emulate new client

    def test_EZMart_show_product_GET(self):   # test the contact methods
        # attempt to get an account by reversing the 'contact' functions' path.
        response = self.client.get(reverse('product'))
        # check if the response was correct using status code: 200
        self.assertEquals(response.status_code, 200)
        # check if the corrent template was emulated
        self.assertTemplateUsed(response, 'product.html')
