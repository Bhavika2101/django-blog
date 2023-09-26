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


class TestGet_object_bd8f399266(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Post Body', author=self.user)

    def test_get_object_success(self):
        request = RequestFactory().get('/')
        request.user = self.user
        view = PostDeleteView()
        view.request = request
        view.kwargs = {'pk': self.post.pk}
        post = view.get_object()
        self.assertEqual(post, self.post)

    def test_get_object_failure(self):
        request = RequestFactory().get('/')
        request.user = AnonymousUser()
        view = PostDeleteView()
        view.request = request
        view.kwargs = {'pk': self.post.pk}
        with self.assertRaises(Http404):
            view.get_object()

