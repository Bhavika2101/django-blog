# Test generated by RoostGPT for test python-django using AI Type Vertex AI and AI Model code-bison-32k

import unittest
from views import get

class TestGet(unittest.TestCase):

    def test_Get_77d719334e(self):
        # Test case 1: Success case
        request = HttpRequest()
        response = get(self, request)
        self.assertEqual(response.status_code, 200)

        # Test case 2: Failure case
        request = HttpRequest()
        response = get(self, request)
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
