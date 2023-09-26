import unittest
from views import get_context_data

class TestGetContextData(unittest.TestCase):

    def test_Get_context_data_bb289b6072(self):
        # Test case 1: When there are more than 3 posts
        post_count = 4
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        self.assertEqual(context['randomposts'], random_items)

        # Test case 2: When there are less than 3 posts
        post_count = 2
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        self.assertEqual(context['randomposts'], Post.objects.filter(available=True))

        # Test case 3: When there are no posts
        post_count = 0
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        self.assertEqual(context['randomposts'], Post.objects.filter(available=True))

        # Test case 4: When there is only 1 post
        post_count = 1
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        self.assertEqual(context['randomposts'], Post.objects.filter(available=True))

if __name__ == '__main__':
    unittest.main()
