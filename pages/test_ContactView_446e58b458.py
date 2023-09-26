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


class TestContactView(TestCase):

    def setUp(self):
        self.request = RequestContext(request)
        self.categories = Category.objects.all()
        self.tags = Tag.objects.all()
        self.popularposts = Post.objects.filter(available=True).annotate(viewyek=Count('views')).order_by('-viewyek')[:3]  # Get popular 3 posts

        self.context = {
            'popularposts': self.popularposts,
            'categories': self.categories,
            'tags': self.tags,
        }

    def test_ContactView_get(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, 'Contact Us')

    def test_ContactView_post_success(self):
        data = {
            'subject': 'Test Subject',
            'email': 'test@example.com',
            'message': 'Test Message',
        }
        response = self.client.post('/contact/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, 'Your message has been sent.')

    def test_ContactView_post_failure(self):
        data = {
            'subject': '',
            'email': '',
            'message': '',
        }
        response = self.client.post('/contact/', data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, 'We encountered an error sending your message, try again later..')

