# Test generated by RoostGPT for test python-django using AI Type Vertex AI and AI Model code-bison-32k

import unittest
from django.contrib import messages
from django.test import TestCase
from .views import CommentCreateView

class TestCommentCreateView(TestCase):

    def test_form_valid_cd84ba476e(self):
        form = CommentCreateView.form_valid(self, form)
        self.assertEqual(form.instance.author, self.request.user)
        self.assertEqual(form.instance.post_id, self.kwargs['pk'])
        self.assertEqual(messages.success(self.request, 'Comment successfully added.'), None)

    def test_form_invalid_cd84ba476e(self):
        form = CommentCreateView.form_invalid(self, form)
        self.assertEqual(form.instance.author, None)
        self.assertEqual(form.instance.post_id, None)
        self.assertEqual(messages.success(self.request, 'Comment successfully added.'), None)

    def test_form_valid_with_existing_slug(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.request.user,
        )
        form = CommentCreateView.form_valid(self, form)
        self.assertEqual(form.instance.author, self.request.user)
        self.assertEqual(form.instance.post_id, post.pk)
        self.assertEqual(messages.success(self.request, 'Comment successfully added.'), None)

    def test_form_valid_with_new_slug(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.request.user,
        )
        form = CommentCreateView.form_valid(self, form)
        self.assertEqual(form.instance.author, self.request.user)
        self.assertEqual(form.instance.post_id, post.pk)
        self.assertEqual(messages.success(self.request, 'Comment successfully added.'), None)
        self.assertEqual(form.instance.slug, 'test-post-2')

    def test_form_valid_with_existing_slug_and_updated_title(self):
        post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            author=self.request.user,
        )
        post.title = "Updated Test Post"
        post.save()
        form = CommentCreateView.form_valid(self, form)
        self.assertEqual(form.instance.author, self.request.user)
        self.assertEqual(form.instance.post_id, post.pk)
        self.assertEqual(messages.success(self.request, 'Comment successfully added.'), None)
        self.assertEqual(form.instance.slug, 'updated-test-post')

