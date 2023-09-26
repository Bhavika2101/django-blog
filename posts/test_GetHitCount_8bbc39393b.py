import unittest
from django.test import TestCase
from .models import Post, Comment


class TestGetHitCount(unittest.TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='Test Content')
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Test Comment')

    def test_get_hit_count(self):
        self.assertEqual(self.comment.getHitCount(), 1)

    def test_get_hit_count_for_non_existent_comment(self):
        self.assertEqual(Comment.objects.get(id=1000).getHitCount(), 0)


class TestStr(unittest.TestCase):

    def setUp(self):
        self.post = Post.objects.create(title='Test Post', content='Test Content')
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Test Comment')

    def test_str(self):
        self.assertEqual(str(self.comment), 'Test Comment')


if __name__ == '__main__':
    unittest.main()
