import unittest
from models import create_user_profile

class TestCreateUser(unittest.TestCase):

    def test_create_user_profile(self):
        user = User.objects.create(username='test_user', password='test_password')
        self.assertTrue(UserDetail.objects.filter(user=user).exists())

    def test_create_user_profile_with_existing_user(self):
        user = User.objects.create(username='test_user', password='test_password')
        UserDetail.objects.create(user=user)
        self.assertRaises(IntegrityError, UserDetail.objects.create, user=user)

if __name__ == '__main__':
    unittest.main()
