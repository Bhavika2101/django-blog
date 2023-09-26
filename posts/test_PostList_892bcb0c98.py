import unittest
from views import dispatch

class TestDispatch(unittest.TestCase):

    def test_Dispatch_e87ceff3c8(self):
        request = None
        response = dispatch(request)
        self.assertEqual(response.status_code, 200)

    def test_Dispatch_with_invalid_request(self):
        request = None
        with self.assertRaises(Http404):
            dispatch(request)

if __name__ == '__main__':
    unittest.main()
