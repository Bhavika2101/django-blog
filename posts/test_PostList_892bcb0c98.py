import unittest
from django.test import TestCase
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template.defaultfilters import slugify
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Category, Tag, HitCount, Comment.


class TestPostList(unittest.TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Test Category', slug='test-category')
        self.tag = Tag.objects.create(name='Test Tag', slug='test-tag')
        self.post = Post.objects.create(title='Test Post', slug='test-post', content='Test content', available=True, category=self.category, tags=[self.tag])

    def test_post_list_view_with_no_category_or_tag(self):
        request = RequestFactory().get('/')
        response = PostList(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'All Posts')
        self.assertEqual(response.context_data['post_list'].count(), 1)

    def test_post_list_view_with_category(self):
        request = RequestFactory().get('/?category_slug=test-category')
        response = PostList(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Posts By Category')
        self.assertEqual(response.context_data['post_list'].count(), 1)

    def test_post_list_view_with_tag(self):
        request = RequestFactory().get('/?tag_slug=test-tag')
        response = PostList(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Posts By Tag')
        self.assertEqual(response.context_data['post_list'].count(), 1)

    def test_post_list_view_with_invalid_category(self):
        request = RequestFactory().get('/?category_slug=invalid-category')
        with self.assertRaises(Http404):
            PostList(request)

    def test_post_list_view_with_invalid_tag(self):
        request = RequestFactory().get('/?tag_slug=invalid-tag')
        with self.assertRaises(Http404):
            PostList(request)

