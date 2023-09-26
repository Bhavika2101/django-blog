import unittest
from views import dispatch

class TestDispatch(unittest.TestCase):

    def test_dispatch_success(self):
        request = HttpRequest()
        response = dispatch(request)
        self.assertEqual(response.status_code, 200)

    def test_dispatch_failure(self):
        request = HttpRequest()
        response = dispatch(request)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
