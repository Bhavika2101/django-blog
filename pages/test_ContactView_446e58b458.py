import unittest
from views import get_context_data

class TestGetContextData(unittest.TestCase):

    def test_Get_context_data_bb289b6072(self):
        request = RequestContext(request)
        context = get_context_data(request)
        self.assertEqual(context['title'], 'Contact')

if __name__ == '__main__':
    unittest.main()
