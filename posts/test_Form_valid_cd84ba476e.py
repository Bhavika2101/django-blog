import unittest
from models import getHitCount

class TestGetHitCount(unittest.TestCase):

    def test_GetHitCount_8bbc39393b(self):
        hit_count = getHitCount(self)
        self.assertEqual(hit_count, 100)

    def test_GetHitCount_8bbc39393c(self):
        hit_count = getHitCount(self)
        self.assertNotEqual(hit_count, 100)

    def test_GetHitCount_8bbc39393d(self):
        hit_count = getHitCount(self)
        self.assertTrue(hit_count > 0)

    def test_GetHitCount_8bbc39393e(self):
        hit_count = getHitCount(self)
        self.assertFalse(hit_count < 0)

if __name__ == '__main__':
    unittest.main()
