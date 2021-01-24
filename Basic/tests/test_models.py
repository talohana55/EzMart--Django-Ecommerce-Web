from django.test import TestCase
from Basic.models import Form


class TestModels(TestCase):

    def setUp(self):
        self.form1 = Form(
            name='form1',
            email='form@gmail.com',
            subject='complains',
            message='problem1',
            status='O',
        )

    def test_FORM_cancreate(self):
        self.assertIsNotNone(self.form1, "Should have been created!")
