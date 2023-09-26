import unittest
from django.test import TestCase
from django.urls import reverse
from .views import get_success_url, PostCreateView, PostUpdateView, PostDeleteView
from .models import Post, Category, Tag, HitCount, Comment


class TestGetSuccessUrl(unittest.TestCase):

    def test_Get_success_url_ee9d9a6412(self):
        post = Post.objects.create(
            category=Category.objects.create(name='test-category'),
            title='test-title',
            slug='test-slug',
            content='test-content'
        )
        self.assertEqual(get_success_url(self, post), reverse('posts:postDetail', args=(post.category.slug, post.pk, post.slug)))

    def test_Get_success_url_with_no_post(self):
        self.assertRaises(Http404, get_success_url, self, None)

    def test_Get_success_url_with_no_category(self):
        post = Post.objects.create(
            title='test-title',
            slug='test-slug',
            content='test-content'
        )
        self.assertRaises(Http404, get_success_url, self, post)

    def test_Get_success_url_with_no_slug(self):
        post = Post.objects.create(
            category=Category.objects.create(name='test-category'),
            title='test-title',
            content='test-content'
        )
        self.assertRaises(Http404, get_success_url, self, post)

    def test_PostUpdateView_get_success_url(self):
        post = Post.objects.create(
            category=Category.objects.create(name='test-category'),
            title='test-title',
            slug='test-slug',
            content='test-content'
        )
        self.assertEqual(PostUpdateView.get_success_url(self, post), reverse('posts:postDetail', args=(post.category.slug, post.pk, post.slug)))

    def test_PostDeleteView_get_success_url(self):
        post = Post.objects.create(
            category=Category.objects.create(name='test-category'),
            title='test-title',
            slug='test-slug',
            content='test-content'
        )
        self.assertEqual(PostDeleteView.get_success_url(self), reverse('user:viewProfile'))

