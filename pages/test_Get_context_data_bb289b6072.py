import random
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from posts.models import Post, Category, Tag
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


class TestGet_context_data_bb289b6072(TestCase):

    def setUp(self):
        self.view = AboutView()
        self.request = RequestContext(request)

    def test_get_context_data_with_no_posts(self):
        # Arrange
        Post.objects.all().delete()

        # Act
        context = self.view.get_context_data(**{'request': self.request})

        # Assert
        self.assertEqual(context['randomposts'], [])
        self.assertEqual(context['popularposts'], [])

    def test_get_context_data_with_less_than_three_posts(self):
        # Arrange
        Post.objects.create(title='Post 1', slug='post-1', content='Content 1', available=True)
        Post.objects.create(title='Post 2', slug='post-2', content='Content 2', available=True)

        # Act
        context = self.view.get_context_data(**{'request': self.request})

        # Assert
        self.assertEqual(context['randomposts'], [Post.objects.get(title='Post 1'), Post.objects.get(title='Post 2')])
        self.assertEqual(context['popularposts'], [])

    def test_get_context_data_with_more_than_three_posts(self):
        # Arrange
        Post.objects.create(title='Post 1', slug='post-1', content='Content 1', available=True)
        Post.objects.create(title='Post 2', slug='post-2', content='Content 2', available=True)
        Post.objects.create(title='Post 3', slug='post-3', content='Content 3', available=True)
        Post.objects.create(title='Post 4', slug='post-4', content='Content 4', available=True)

        # Act
        context = self.view.get_context_data(**{'request': self.request})

        # Assert
        self.assertEqual(len(context['randomposts']), 3)
        self.assertEqual(context['popularposts'], [Post.objects.get(title='Post 4'), Post.objects.get(title='Post 3'), Post.objects.get(title='Post 2')])

    def test_get_context_data_with_no_categories(self):
        # Arrange
        Category.objects.all().delete()

        # Act
        context = self.view.get_context_data(**{'request': self.request})

        # Assert
        self.assertEqual(context['categories'], [])

    def test_get_context_data_with_no_tags(self):
        # Arrange
        Tag.objects.all().delete()

        # Act
        context = self.view.get_context_data(**{'request': self.request})

        # Assert
        self.assertEqual(context['tags'], [])

    def test_get_context_data_with_popular_posts_with_no_views(self):
        # Arrange
        Post.objects.create(title='Post 1', slug='post-1', content='Content 1', available=True)
        Post.objects.create(title='Post 2', slug='post-2', content='Content 2', available=True)
        Post.objects.create(title='Post 3', slug='post-3', content='Content 3', available=True)
        Post.objects.create(title='Post 4', slug='post-4', content='Content 4', available=True)

        # Act
        context = self.view.get_context_data(**{'request': self.request})

        # Assert
        self.assertEqual(context['popularposts'], [])

