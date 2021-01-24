from django.test import TestCase, Client
from django.urls import reverse
import json
from accounts.models import Account, MyAccManager


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()  # emulate new client

    def test_EZMart_regcust_GET(self):   # test the registercustomer methods

        # attempt to get an account by reversing the 'registeredcustomer' functions' path.
        response = self.client.get(reverse('registercustomer'))

        # check if the response was correct using status code: 200
        self.assertEquals(response.status_code, 200)
        # check if the corrent template was emulated
        self.assertTemplateUsed(response, 'registercustomer.html')

    def test_EZMart_regbusi_GET(self):  # test the registerbusiness methods

        # attempt to get an account by reversing the 'registerbusiness' functions' path.
        response = self.client.get(reverse('registerbusiness'))

        # check if the response was correct using status code: 200
        self.assertEquals(response.status_code, 200)
        # check if the corrent template was emulated
        self.assertTemplateUsed(response, 'registerbusiness.html')

    def test_EZMart_login_GET(self):  # test the login methods

        # attempt to get an account by reversing the 'login' functions' path.
        response = self.client.get(reverse('login'))

        # check if the response was correct using status code: 200
        self.assertEquals(response.status_code, 200)
        # check if the corrent template was emulated
        self.assertTemplateUsed(response, 'Login.html')

    def test_EZMart_logout_GET(self):
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 302)


