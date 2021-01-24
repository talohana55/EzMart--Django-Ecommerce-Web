from django.test import TestCase, Client
from django.urls import reverse
import json
from Basic.models import Form


class TestViewsBasic(TestCase):

    def setUp(self):
        self.client = Client()  # emulate new client

    def test_EZMart_contact_GET(self):   # test the contact methods
        # attempt to get an account by reversing the 'contact' functions' path.
        response = self.client.get(reverse('contact'))
        # check if the response was correct using status code: 200
        self.assertEquals(response.status_code, 200)
        # check if the corrent template was emulated
        self.assertTemplateUsed(response, 'contact.html')

    def test_EZMart_SearchProdView_GET(self):

        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
    
    def test_EZMart_purchase_GET(self):      # refer to Product test
        response = self.client.get(reverse('product'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product.html')

    def test_EZMart_index_GET(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_EZMart_about_GET(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_EZMart_regulations_GET(self):
        response = self.client.get(reverse('regulations'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'regulations.html')

    def test_EZMart_privacy_GET(self):
        response = self.client.get(reverse('privacy'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy.html') 
