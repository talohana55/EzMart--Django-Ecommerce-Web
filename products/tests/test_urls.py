from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import show_product


class TestUrls(SimpleTestCase):

    def test_show_product_url_is_resolved(self):
        url = reverse('product')
        self.assertEqual(resolve(url).func, show_product)
