import unittest
from models import create_user_profile

class TestCreateUserProfile(unittest.TestCase):

    def test_Create_user_profile_bd5ac76a45(self):
        # Test case to check if the create_user_profile() method is called when a new user is created.
        user = User.objects.create_user(username='test_user', password='test_password')
        self.assertTrue(create_user_profile.called)

    def test_Create_user_profile_cd5ac76a45(self):
        # Test case to check if the create_user_profile() method is called when a user is updated.
        user = User.objects.create_user(username='test_user', password='test_password')
        user.username = 'updated_test_user'
        user.save()
        self.assertTrue(create_user_profile.called)

    def test_Create_user_profile_dd5ac76a45(self):
        # Test case to check if the create_user_profile() method is not called when a user is deleted.
        user = User.objects.create_user(username='test_user', password='test_password')
        user.delete()
        self.assertFalse(create_user_profile.called)

if __name__ == '__main__':
    unittest.main()
