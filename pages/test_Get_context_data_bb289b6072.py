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

        # Test case 4: When there is an error getting the posts
        post_count = 4
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        self.assertEqual(context['randomposts'], random_items)

        # Test case 5: When popularposts is None
        post_count = 4
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        context['popularposts'] = None
        self.assertEqual(context['popularposts'], None)

        # Test case 6: When categories is None
        post_count = 4
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        context['categories'] = None
        self.assertEqual(context['categories'], None)

        # Test case 7: When tags is None
        post_count = 4
        items = list(Post.objects.filter(available=True))
        random_items = random.sample(items, 3)
        context = get_context_data(self, **kwargs)
        context['tags'] = None
        self.assertEqual(context['tags'], None)

if __name__ == '__main__':
    unittest.main()
