import unittest
from views import dispatch

class TestDispatch(unittest.TestCase):

    def test_Dispatch_e87ceff3c8(self):
        request = None
        args = None
        kwargs = None
        post = Post()
        post.author = None
        self.assertRaises(Http404, dispatch, request, post, args, kwargs)

    def test_Dispatch_e87ceff3c8_success(self):
        request = None
        args = None
        kwargs = None
        post = Post()
        post.author = self.request.user
        self.assertTrue(dispatch(request, post, args, kwargs))

if __name__ == '__main__':
    unittest.main()
