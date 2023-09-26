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


class TestDelete(unittest.TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            body='Test post body',
            author=self.user,
            category=self.category,
            tag=self.tag,
        )

    def test_delete_post(self):
        response = self.client.delete(reverse('post_delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('post_list'))
        messages.success(self.request, 'Post successfully deleted.')

    def test_delete_post_with_nonexistent_pk(self):
        response = self.client.delete(reverse('post_delete', kwargs={'pk': 999999}))
        self.assertEqual(response.status_code, 404)


class TestDispatch(unittest.TestCase):

    def test_dispatch_get(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)

    def test_dispatch_post(self):
        response = self.client.post(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 405)


class TestFormValid(unittest.TestCase):

    def test_form_valid(self):
        data = {
            'title': 'Test Post',
            'slug': 'test-post',
            'body': 'Test post body',
            'author': self.user.pk,
            'category': self.category.pk,
            'tag': self.tag.pk,
        }
        response = self.client.post(reverse('post_create'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('post_detail', kwargs={'pk': self.post.pk}))


class TestGetHitCount(unittest.TestCase):

    def test_get_hit_count(self):
        hit_count = HitCount.objects.get(post=self.post)
        self.assertEqual(hit_count.hits, 1)


class TestGetObject(unittest.TestCase):

    def test_get_object(self):
        post = get_object_or_404(Post, pk=self.post.pk)
        self.assertEqual(post, self.post)

    def test_get_object_with_nonexistent_pk(self):
        with self.assertRaises(Http404):
            get_object_or_404(Post, pk=999999)


class TestGetSuccessUrl(unittest.TestCase):

    def test_get_success_url(self):
        self.assertEqual(self.post.get_success_url(), reverse('post_detail', kwargs={'pk': self.post.pk}))


class TestStr(unittest.TestCase):

    def test_str(self):
        self.assertEqual(str(self.post), self.post.title)


class TestTests(unittest.TestCase):

    def test_tests(self):
        self.assertTrue(True)
