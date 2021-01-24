from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Shop.views import inventory, update_prod, delete_prod, add_prod, get_prods, StoreHomePage


class TestUrls(SimpleTestCase):

    def test_StoreHomePage_url_is_resolved(self):
        url = reverse('StoreHomePage')
        self.assertEqual(resolve(url).func, StoreHomePage)

    def test_add_prod_url_is_resolved(self):
        url = reverse('add_prod')
        self.assertEqual(resolve(url).func, add_prod)

    def test_delete_prod_url_is_resolved(self):
        url = reverse('delete_prod')
        self.assertEqual(resolve(url).func, delete_prod)

    def test_update_prod_url_is_resolved(self):
        url = reverse('update_prod')
        self.assertEqual(resolve(url).func, update_prod)

    
    def test_inventory_url_is_resolved(self):
        url = reverse('inventory')
        self.assertEqual(resolve(url).func, inventory)
