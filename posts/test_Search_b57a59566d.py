import unittest
from views import *

class TestDelete(unittest.TestCase):

    def test_Delete_46228725a2(self):
        request = {
            'POST': {
                'id': '1'
            }
        }
        response = delete(request)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/posts/')

class TestDispatch(unittest.TestCase):

    def test_Dispatch_e87ceff3c8(self):
        request = {
            'PATH_INFO': '/posts/1/',
            'REQUEST_METHOD': 'GET'
        }
        response = dispatch(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post Detail')

class TestForm_valid(unittest.TestCase):

    def test_Form_valid_cd84ba476e(self):
        request = {
            'POST': {
                'title': 'Test Post',
                'content': 'Test Content',
                'tags': 'test,tag'
            }
        }
        response = form_valid(request)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/posts/')

class TestGetHitCount(unittest.TestCase):

    def test_GetHitCount_8bbc39393b(self):
        request = {
            'GET': {
                'id': '1'
            }
        }
        response = getHitCount(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '1')

class TestGet(unittest.TestCase):

    def test_Get_77d719334e(self):
        request = {
            'GET': {
                'id': '1'
            }
        }
        response = get(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post Detail')

class TestGet_client_ip(unittest.TestCase):

    def test_Get_client_ip_d036d14216(self):
        request = {
            'META': {
                'REMOTE_ADDR': '127.0.0.1'
            }
        }
        response = get_client_ip(request)
        self.assertEqual(response, '127.0.0.1')

class TestGet_context_data(unittest.TestCase):

    def test_Get_context_data_bb289b6072(self):
        request = {
            'GET': {
                'id': '1'
            }
        }
        response = get_context_data(request)
        self.assertEqual(response['post'].id, 1)

class TestGet_object(unittest.TestCase):

    def test_Get_object_bd8f399266(self):
        request = {
            'GET': {
                'id': '1'
            }
        }
        response = get_object(request)
        self.assertEqual(response.id, 1)

class TestGet_success_url(unittest.TestCase):

    def test_Get_success_url_ee9d9a6412(self):
        request = {
            'POST': {
                'title': 'Test Post',
                'content': 'Test Content',
                'tags': 'test,tag'
            }
        }
        response = get_success_url(request)
        self.assertEqual(response, '/posts/')

class TestPostList(unittest.TestCase):

    def test_PostList_892bcb0c98(self):
        request = {
            'GET': {
                'page': '1'
            }
        }
        response = post_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post List')

class TestSearch(unittest.TestCase):

    def test_Search_b57a59566d(self):
        request = {
            'GET': {
                'query': 'test'
            }
        }
        response = search(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search Results')

    def test_Search_NoResults(self):
        request = {
            'GET': {
                'query': 'noresults'
            }
        }
        response = search(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No results found')

class Test___str__(unittest.TestCase):

    def test___str___57494adc14(self):
        request = {
            'GET': {
                'id': '1'
            }
        }
        response = get_object(request)
        self.assertEqual(response.__str__(), 'Post: Test Post')

class TestTests(unittest.TestCase):

    def test_tests(self):
        response = tests()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Results')

if __name__ == '__main__':
    unittest.main()
