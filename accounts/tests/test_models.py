from django.test import TestCase
from accounts.models import Account,MyAccManager

class TestModels(TestCase):

    def setUp(self):  # set up for the Account testing at the end.
        self.acc1= Account.objects.create( # create dummy account, dummy values sent.
            email= 'acc1@email.com',
            first_name='acc',
            last_name='1',
            address='acc1address',
            phone='123456',
            username='account1',
            password='pass123',
        )

    def test_accMan_cancreate(self):  # check MyAccManagers' account creating capability.
        self.assertIsNotNone(self.acc1, "Should have been created!")  # during set up, we created a dummy account by calling create_user in MyAccManager. Check that the user was created.
       
    
    def test_acc_is_admin(self):  # test a base account
        self.assertFalse(self.acc1.has_perm(self.acc1.is_admin), "Should be false")  # by default, a user should never be admin!


