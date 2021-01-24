from django.test import TestCase
from products.models import ProductManager,Product


class TestModels(TestCase):

    def setUp(self):
        self.prod = Product.objects.create(
            title='productTOTest',
            price='10000000',
            category='FS',
            quantity='150',
        )

    def test_Product_cancreate(self):
        self.assertIsNotNone(self.prod, "Should have been created!")



