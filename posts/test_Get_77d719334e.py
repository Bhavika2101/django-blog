import unittest
from views import get

class TestGet(unittest.TestCase):

    def test_Get_77d719334e(self):
        # Test case 1: Success case
        request = HttpRequest()
        response = get(self, request)
        self.assertEqual(response.status_code, 200)

    def test_Get_77d719334e(self):
        # Test case 2: Failure case
        request = HttpRequest()
        response = get(self, request)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
