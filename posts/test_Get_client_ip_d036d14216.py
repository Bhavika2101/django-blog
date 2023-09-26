import unittest
from django.test import TestCase
from views import get_client_ip

class TestGetClientIp(unittest.TestCase):

    def test_get_client_ip_with_x_forwarded_for(self):
        request = MockRequest(META={'HTTP_X_FORWARDED_FOR': '127.0.0.1'})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_without_x_forwarded_for(self):
        request = MockRequest(META={'REMOTE_ADDR': '127.0.0.1'})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_with_invalid_x_forwarded_for(self):
        request = MockRequest(META={'HTTP_X_FORWARDED_FOR': 'invalid'})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_with_empty_x_forwarded_for(self):
        request = MockRequest(META={'HTTP_X_FORWARDED_FOR': ''})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_with_none_x_forwarded_for(self):
        request = MockRequest(META={'HTTP_X_FORWARDED_FOR': None})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_with_empty_remote_addr(self):
        request = MockRequest(META={'REMOTE_ADDR': ''})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_with_none_remote_addr(self):
        request = MockRequest(META={'REMOTE_ADDR': None})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

    def test_get_client_ip_with_invalid_remote_addr(self):
        request = MockRequest(META={'REMOTE_ADDR': 'invalid'})
        ip = get_client_ip(request)
        self.assertEqual(ip, '127.0.0.1')

class MockRequest:
    def __init__(self, META):
        self.META = META
