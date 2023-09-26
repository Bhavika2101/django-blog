import unittest
from views import get_context_data

class TestGet_context_data(unittest.TestCase):

    def test_Get_context_data_bb289b6072(self):
        # Test case to check if the context data is returned correctly
        context = get_context_data(self)
        self.assertTrue(context['popularposts'])
        self.assertTrue(context['relatedposts'])
        self.assertTrue(context['categories'])
        self.assertTrue(context['tags'])
        self.assertTrue(context['comments'])

    def test_Get_context_data_with_no_data(self):
        # Test case to check if the context data is returned correctly when there is no data
        context = get_context_data(self)
        self.assertFalse(context['popularposts'])
        self.assertFalse(context['relatedposts'])
        self.assertFalse(context['categories'])
        self.assertFalse(context['tags'])
        self.assertFalse(context['comments'])

if __name__ == '__main__':
    unittest.main()
