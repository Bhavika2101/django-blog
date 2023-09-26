import unittest
from views import get_context_data

class TestGetContextData(unittest.TestCase):

    def test_Get_context_data_bb289b6072(self):
        request = RequestContext(request)
        context = get_context_data(request)
        self.assertEqual(context['title'], 'Contact')
        self.assertEqual(context['form'], ContactForm())

    def test_Get_context_data_bb289b6072_post(self):
        request = RequestContext(request)
        request.method = 'POST'
        request.POST = {
            'subject': 'Test Subject',
            'email': 'test@example.com',
            'message': 'Test Message',
        }
        context = get_context_data(request)
        self.assertEqual(context['title'], 'Contact')
        self.assertEqual(context['form'], ContactForm())
        self.assertEqual(context['success'], True)

    def test_Get_context_data_bb289b6072_post_error(self):
        request = RequestContext(request)
        request.method = 'POST'
        request.POST = {
            'subject': 'Test Subject',
            'email': 'test@example.com',
            'message': 'Test Message',
        }
        with self.assertRaises(Exception):
            context = get_context_data(request)
        self.assertEqual(context['title'], 'Contact')
        self.assertEqual(context['form'], ContactForm())
        self.assertEqual(context['error'], True)

