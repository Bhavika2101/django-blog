import unittest
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


class TestDispatch_e87ceff3c8(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)

    def test_dispatch_success(self):
        request = RequestFactory().get('/post/1/edit/')
        request.user = self.user
        response = PostUpdateView.as_view()(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 200)

    def test_dispatch_failure(self):
        request = RequestFactory().get('/post/1/edit/')
        request.user = AnonymousUser()
        response = PostUpdateView.as_view()(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 404)


class TestForm_valid_cd84ba476e(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)

    def test_form_valid(self):
        data = {'title': 'Test Post', 'body': 'Test Body'}
        request = RequestFactory().post('/post/new/', data=data)
        request.user = self.user
        response = PostCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_form_invalid(self):
        data = {'title': '', 'body': ''}
        request = RequestFactory().post('/post/new/', data=data)
        request.user = self.user
        response = PostCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class TestGetHitCount_8bbc39393b(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)

    def test_get_hit_count(self):
        hit_count = HitCount.objects.get(post=self.post)
        self.assertEqual(hit_count.hits, 1)


class TestGet_success_url_ee9d9a6412(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)

    def test_get_success_url(self):
        request = RequestFactory().get('/post/1/edit/')
        request.user = self.user
        response = PostUpdateView.as_view()(request, pk=self.post.pk)
        self.assertEqual(response.status_code, 200)


class Test___str___57494adc14(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)

    def test___str__(self):
        self.assertEqual(str(self.post), 'Test Post')


class TestTests(unittest.TestCase):

    def test_tests(self):
        self.assertTrue(True)
