import unittest
from views import get_object

class TestGetObject(unittest.TestCase):

    def test_get_object_success(self):
        # Create a user
        user = User.objects.create_user(username='test_user', password='test_password')

        # Create a post
        post = Post.objects.create(title='Test Post', body='Test Body', author=user)

        # Get the post
        get_object(self, queryset=Post.objects.filter(pk=post.pk))

    def test_get_object_failure(self):
        # Create a user
        user = User.objects.create_user(username='test_user', password='test_password')

        # Create a post
        post = Post.objects.create(title='Test Post', body='Test Body', author=user)

        # Try to get the post with a different user
        with self.assertRaises(Http404):
            get_object(self, queryset=Post.objects.filter(pk=post.pk), request = user)

if __name__ == '__main__':
    unittest.main()
