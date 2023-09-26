import unittest
from django.test import TestCase
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.urls import reverse_lazy
from views import form_valid


class TestFormValid(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='123456')
        self.client.login(username='testuser', password='123456')

    def test_Form_valid_cd84ba476e(self):
        form_data = {'old_password': '123456', 'new_password1': 'new_password', 'new_password2': 'new_password'}
        response = self.client.post(reverse_lazy('change_password'), form_data)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(str(messages[0]), 'Your password has been changed successfully.')

    def test_Form_invalid_cd84ba476e(self):
        form_data = {'old_password': 'wrong_password', 'new_password1': 'new_password', 'new_password2': 'new_password'}
        response = self.client.post(reverse_lazy('change_password'), form_data)
        messages = get_messages(response.wsgi_request)
        self.assertEqual(str(messages[0]), 'Your old password was entered incorrectly. Please enter it again.')

