import unittest
from models import create_user_profile, save_user_profile


class TestCreateUser(unittest.TestCase):

    def test_Create_user_profile_bd5ac76a45(self):
        # Test 1: Ensure that the create_user_profile function creates a new user profile.
        user_profile = create_user_profile("John Doe", "john.doe@example.com")
        self.assertIsNotNone(user_profile)
        self.assertEqual(user_profile.name, "John Doe")
        self.assertEqual(user_profile.email, "john.doe@example.com")


class TestSaveUser(unittest.TestCase):

    def test_Save_user_profile_1ba43a1a05(self):
        # Test 1: Ensure that the save_user_profile function saves the user profile.
        user_profile = create_user_profile("John Doe", "john.doe@example.com")
        user_profile.name = "Jane Doe"
        user_profile.email = "jane.doe@example.com"
        save_user_profile(user_profile)
        user_profile = User.objects.get(pk=user_profile.id)
        self.assertEqual(user_profile.name, "Jane Doe")
        self.assertEqual(user_profile.email, "jane.doe@example.com")


class TestStr(unittest.TestCase):

    def test___str___57494adc14(self):
        # Test 1: Ensure that the __str__ function returns the correct string representation of the user profile.
        user_profile = create_user_profile("John Doe", "john.doe@example.com")
        self.assertEqual(str(user_profile), "John Doe <john.doe@example.com>")


if __name__ == '__main__':
    unittest.main()
