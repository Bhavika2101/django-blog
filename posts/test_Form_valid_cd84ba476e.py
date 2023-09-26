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
from .models import Post, Category, Tag, HitCount, Comment


class TestForm_valid_cd84ba476e(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)
        self.form_data = {'author': self.user, 'post_id': self.post.pk, 'body': 'Test Comment'}

    def test_form_valid(self):
        form = CommentForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('blog:add_comment', kwargs={'pk': self.post.pk}), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(messages.get_messages(response.wsgi_request)[0].message, 'Comment successfully added.')

    def test_form_invalid(self):
        form_data = {'author': self.user, 'post_id': self.post.pk}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        response = self.client.post(reverse('blog:add_comment', kwargs={'pk': self.post.pk}), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')


class TestPostUpdateView_form_valid_cd84ba476e(unittest.TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.post = Post.objects.create(title='Test Post', body='Test Body', author=self.user)
        self.form_data = {'title': 'Test Post', 'body': 'Test Body', 'author': self.user}

    def test_form_valid(self):
        form = PostUpdateView(data=self.form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('blog:post_update', kwargs={'pk': self.post.pk}), data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(messages.get_messages(response.wsgi_request)[0].message, 'Your post has been successfully updated.')

    def test_form_invalid(self):
        form_data = {'title': '', 'body': '', 'author': self.user}
        form = PostUpdateView(data=form_data)
        self.assertFalse(form.is_valid())
        response = self.client.post(reverse('blog:post_update', kwargs={'pk': self.post.pk}), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')

    def test_form_valid_slug_update(self):
        form_data = {'title': 'Test Post Updated', 'body': 'Test Body', 'author': self.user}
        form = PostUpdateView(data=form_data)
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('blog:post_update', kwargs={'pk': self.post.pk}), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(messages.get_messages(response.wsgi_request)[0].message, 'Your post has been successfully updated.')
        self.assertEqual(Post.objects.get(pk=self.post.pk).slug, 'test-post-updated')

