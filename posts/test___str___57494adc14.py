import unittest
from models import Tag


class TestTagStr(unittest.TestCase):

    def test___str___57494adc14(self):
        tag = Tag(name='Test Tag')
        self.assertEqual(str(tag), 'Test Tag')

    def test___str___57494adc14_with_emoji(self):
        tag = Tag(name='Test Tag 🙈')
        self.assertEqual(str(tag), 'Test Tag 🙈')


if __name__ == '__main__':
    unittest.main()
