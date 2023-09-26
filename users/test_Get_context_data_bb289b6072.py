import unittest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from posts.models import Post, Category, Tag
from views import get_context_data

class TestGetContextData(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.client.login(username='testuser', password='123456')

    def test_Get_context_data_bb289b6072(self):
        response = self.client.get(reverse('user:viewProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('popularposts' in response.context)
        self.assertTrue('categories' in response.context)
        self.assertTrue('tags' in response.context)

    def test_Get_context_data_bb289b6072_fail(self):
        response = self.client.get(reverse('user:viewProfile'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse('popularpost' in response.context)
        self.assertFalse('categorie' in response.context)
        self.assertFalse('tag' in response.context)

