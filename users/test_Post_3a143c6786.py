import unittest
from views import post

class TestPost(unittest.TestCase):

    def test_post_success(self):
        request = {
            'POST': {
                'username': 'test_user',
                'email': 'test_user@example.com',
                'first_name': 'Test',
                'last_name': 'User',
                'bio': 'This is a test bio.',
                'location': 'Test Location',
                'profile_image': 'test_image.jpg',
            },
            'FILES': {
                'profile_image': 'test_image.jpg',
            }
        }
        response = post(self, request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your profile was successfully updated!')

    def test_post_failure(self):
        request = {
            'POST': {
                'username': 'test_user',
                'email': 'test_user@example.com',
                'first_name': 'Test',
                'last_name': 'User',
                'bio': 'This is a test bio.',
                'location': 'Test Location',
                'profile_image': 'test_image.jpg',
            },
            'FILES': {
                'profile_image': 'test_image.jpg',
            }
        }
        response = post(self, request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your profile was successfully updated!')

if __name__ == '__main__':
    unittest.main()
