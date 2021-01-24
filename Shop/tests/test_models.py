from django.test import TestCase
from Shop.models import Store, StoreManager


class TestModels(TestCase):

    def setUp(self):
        self.store = Store.objects.create(
            name='store',
            businessNum='12345678',
            category='FS',
            facebook_url='None',
            instagram_url='None',
            twitter_url='None',
        )

    def test_Store_cancreate(self):
        self.assertIsNotNone(self.store, "Should have been created!")

