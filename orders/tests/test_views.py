from django.test import TestCase, Client
from django.urls import reverse
import json
from orders.models import OrderedItem,OrderManager


class TestViewsOrders(TestCase):

    def setUp(self):
        self.client = Client()
        
    def test_EZMart_receipts_GET(self):   
        response = self.client.get(reverse('receipts'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'receipts.html')
