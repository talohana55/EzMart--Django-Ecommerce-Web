from django.test import SimpleTestCase
from django.urls import reverse, resolve
from accounts.views import registercustomer, registerbusiness, Login, logout


class TestUrls(SimpleTestCase):

    def test_regcus_url_is_resolved(self):
        # get the url that matches '/registercustomer' from the 'registercustomer' function in views.py of accounts
        url = reverse('registercustomer')
        # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
        self.assertEqual(resolve(url).func, registercustomer)

    def test_regbusi_url_is_resolved(self):
        # get the url that matches '/registerbusiness' from the 'registerbusiness' function in views.py of accounts
        url = reverse('registerbusiness')
        # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
        self.assertEqual(resolve(url).func, registerbusiness)

    def test_Login_url_is_resolved(self):
        # get the url that matches '/Login' from the 'Login' function in views.py of accounts
        url = reverse('login')
        # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
        self.assertEqual(resolve(url).func, Login)

    def test_logout_url_is_resolved(self):
        # get the url that matches '/logout' from the 'logout' function in views.py of accounts
        url = reverse('logout')
        # check that the URL is being parsed correctly, and that it is reachable by comparing the .func of it to the imported function
        self.assertEqual(resolve(url).func, logout)
