from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orders.views import receipts



class TestUrls(SimpleTestCase):

    def test_receipts_url_is_resolved(self):
        url = reverse('receipts')
        self.assertEqual(resolve(url).func, receipts)
    
