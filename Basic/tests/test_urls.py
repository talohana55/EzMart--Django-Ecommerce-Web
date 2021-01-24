from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Basic.views import index, contact, privacy, regulations, aboutUs, SearchProdView, purchase, checkout


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):        
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_contact_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_privacy_url_is_resolved(self):
        url = reverse('privacy')
        self.assertEqual(resolve(url).func, privacy)

    def test_regulations_url_is_resolved(self):
        url = reverse('regulations')
        self.assertEqual(resolve(url).func, regulations)

    def test_aboutUs_url_is_resolved(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, aboutUs)   

    def test_purchase_url_is_resolved(self):
        url = reverse('purchase')
        self.assertEqual(resolve(url).func, purchase)

    

    
