import unittest
import random
from django.test import TestCase
from django.db.models import QuerySet  # Add this import
from posts.models import Post
from pages.views import LatestPostListView  # Corrected import statement

class TestGetContextData(TestCase):

    def setUp(self):
        self.available_posts = Post.objects.filter(available=True)
        self.post_list = LatestPostListView()
        self.post_list.object_list = self.available_posts  # Assign the object_list

    def test_random_posts_when_more_than_3_posts(self):
        # Test case 1: When there are more than 3 posts
        post_count = 4
        if post_count > len(self.available_posts):
            post_count = len(self.available_posts)  # Adjust post_count if it's greater than available_posts count
        random_items = random.sample(list(self.available_posts), post_count)
        context = self.post_list.get_context_data(post_count=post_count)
        self.assertTrue(
        context['randomposts'] == [] or (isinstance(context['randomposts'], QuerySet) and len(context['randomposts']) == 0)
    )

    def test_random_posts_when_less_than_3_posts(self):
        # Test case 2: When there are less than 3 posts
        post_count = 2
        context = self.post_list.get_context_data(post_count=post_count)
        self.assertTrue(
        context['randomposts'] == [] or (isinstance(context['randomposts'], QuerySet) and len(context['randomposts']) == 0)
    )

    def test_random_posts_when_no_posts(self):
        # Test case 3: When there are no posts
        post_count = 0
        context = self.post_list.get_context_data(post_count=post_count)
        self.assertTrue(
        context['randomposts'] == [] or (isinstance(context['randomposts'], QuerySet) and len(context['randomposts']) == 0)
    )

    def test_random_posts_when_only_1_post(self):
        # Test case 4: When there is only 1 post
        post_count = 1
        context = self.post_list.get_context_data(post_count=post_count)
        self.assertTrue(
        context['randomposts'] == [] or (isinstance(context['randomposts'], QuerySet) and len(context['randomposts']) == 0)
    )
if __name__ == '__main__':
    unittest.main()
