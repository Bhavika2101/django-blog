import unittest
from django.test import TestCase
from .models import Tag


class Test__str__(TestCase):

    def setUp(self):
        self.tag = Tag(name='Test Tag')

    def test__str__(self):
        self.assertEqual(str(self.tag), 'Test Tag')

    def test__str__with_unicode_characters(self):
        self.tag.name = 'Tèst Tág'
        self.assertEqual(str(self.tag), 'Tèst Tág')

    def test__str__with_long_name(self):
        self.tag.name = 'This is a very long name for a tag'
        self.assertEqual(str(self.tag), 'This is a very long name for a tag')

    def test__str__with_empty_name(self):
        self.tag.name = ''
        self.assertEqual(str(self.tag), '')

    def test__str__with_none_name(self):
        self.tag.name = None
        self.assertEqual(str(self.tag), '')

    def test__str__with_hit_count(self):
        hit_count = HitCount.objects.create(ip='127.0.0.1')
        self.tag.hit_count.add(hit_count)
        self.assertEqual(str(self.tag), 'Test Tag (1)')

    def test__str__with_multiple_hit_counts(self):
        hit_count1 = HitCount.objects.create(ip='127.0.0.1')
        hit_count2 = HitCount.objects.create(ip='127.0.0.2')
        self.tag.hit_count.add(hit_count1)
        self.tag.hit_count.add(hit_count2)
        self.assertEqual(str(self.tag), 'Test Tag (2)')

    def test__str__with_hit_count_and_long_name(self):
        hit_count = HitCount.objects.create(ip='127.0.0.1')
        self.tag.hit_count.add(hit_count)
        self.tag.name = 'This is a very long name for a tag'
        self.assertEqual(str(self.tag), 'This is a very long name for a tag (1)')

    def test__str__with_hit_count_and_unicode_characters(self):
        hit_count = HitCount.objects.create(ip='127.0.0.1')
        self.tag.hit_count.add(hit_count)
        self.tag.name = 'Tèst Tág'
        self.assertEqual(str(self.tag), 'Tèst Tág (1)')

    def test__str__with_hit_count_and_none_name(self):
        hit_count = HitCount.objects.create(ip='127.0.0.1')
        self.tag.hit_count.add(hit_count)
        self.tag.name = None
        self.assertEqual(str(self.tag), '(1)')

