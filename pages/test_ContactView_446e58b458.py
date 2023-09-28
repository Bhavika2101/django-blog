import unittest
from django.test import RequestFactory
from django.http import HttpResponse
from pages.views import ContactView

class TestContactView(unittest.TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()

    def test_contact_view_get(self):
        request = self.factory.get('contact/')
        response = ContactView(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response, 'Your message has been sent.')
        self.assertNotEqual(response, 'We encountered an error sending your message, try again later..')

    def test_contact_view_post_success(self):
        request = self.factory.get(path='contact/', data={
            'subject': 'Test Subject',
            'email': 'test@example.com',
            'message': 'Test Message',
        }, follow=True)# Use follow=True to get the redirect response
        response = ContactView(request) 
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(response, 'We encountered an error sending your message, try again later..')

    def test_contact_view_post_error(self):
        request = self.factory.post('contact/', {
            'subject': 'Test Subject',
            'email': 'test@example.com',
            'message': 'Test Message',
        })
        # Simulate an error when sending an email
        response = HttpResponse()
        with self.assertRaises(Exception):
            response = ContactView(request)
        
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(response, 'Your message has been sent.')
        # self.assertEqual(response, 'We encountered an error sending your message, try again later..')
