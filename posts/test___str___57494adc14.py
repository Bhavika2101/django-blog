import unittest
from models import getHitCount

class TestGetHitCount(unittest.TestCase):

    def test_GetHitCount_8bbc39393b(self):
        hit_count = getHitCount()
        self.assertEqual(hit_count, 1)

if __name__ == '__main__':
    unittest.main()
