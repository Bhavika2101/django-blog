# Test generated by RoostGPT for test python-django using AI Type Vertex AI and AI Model code-bison-32k

import unittest
from .models import Post


class TestGetHitCount(unittest.TestCase):

    def test_GetHitCount_8bbc39393b(self):
        # Create a Post object
        post = Post(title="Test Post", content="Test Content")
        # Save the Post object
        post.save()
        # Get the hit count of the Post object
        hit_count = post.getHitCount()
        # Assert that the hit count is 0
        self.assertEqual(hit_count, 0)

        # Create a Comment object
        comment = Comment(post=post, author=post.author, content="Test Comment")
        # Save the Comment object
        comment.save()
        # Get the hit count of the Post object
        hit_count = post.getHitCount()
        # Assert that the hit count is 1
        self.assertEqual(hit_count, 1)

    def test_GetHitCount_8bbc39393b_fail(self):
        # Create a Post object
        post = Post(title="Test Post", content="Test Content")
        # Save the Post object
        post.save()
        # Get the hit count of the Post object
        hit_count = post.getHitCount()
        # Assert that the hit count is not 0
        self.assertNotEqual(hit_count, 0)

