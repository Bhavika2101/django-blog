# This test case was generated by claudeAI and it doesn't work.

import unittest
from django.test import RequestFactory
from views import AboutView, get_context_data

class TestGetContextData(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.view = AboutView()

    def test_get_context_data_success(self):
        """Test get context data success case"""
        request = self.factory.get('/about/')
        response = self.view.get(request)
        context = get_context_data(response)
        
        self.assertIn('randomposts', context)
        self.assertIn('popularposts', context)
        self.assertIn('categories', context)
        self.assertIn('tags', context)
        
        # TODO: Check actual data returned

    def test_get_context_data_failure(self):
        """Test get context data failure case"""
        request = self.factory.get('/about/')
        
        # Override get_context_data to return empty dict
        self.view.get_context_data = lambda self: {}
        
        response = self.view.get(request)
        context = get_context_data(response)
        
        self.assertNotIn('randomposts', context)
        self.assertNotIn('popularposts', context)
        self.assertNotIn('categories', context)
        self.assertNotIn('tags', context)
        
if __name__ == '__main__':
    unittest.main()