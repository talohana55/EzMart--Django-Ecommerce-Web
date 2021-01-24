from django.test import TestCase
from orders.models import OrderManager, OrderedItem


class TestModels(TestCase):

    def setUp(self):
        self.order = OrderedItem.objects.create(
            buyer_id='123',
            shop_id='1234',
            price='10000000',
            quantity='150',
            product_id='14141',
            shipping_address='onelulu',
        )

    def test_Order_cancreate(self):
        self.assertIsNotNone(self.order, "Should have been created!")
