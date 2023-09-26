import unittest
from django.test import TestCase
from django.urls import reverse
from posts.models import Post, Category, Tag, HitCount, Comment
from posts.views import PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class TestGet_success_url_ee9d9a6412(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='test category', slug='test-category')
        self.post = Post.objects.create(
            author=self.user,
            category=self.category,
            title='test post',
            slug='test-post',
            content='test content'
        )

    def test_get_success_url_with_valid_data(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_create'),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': 'test post',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('posts:postDetail', args=(self.category.slug, self.post.pk, self.post.slug)))

    def test_get_success_url_with_invalid_data(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_create'),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': '',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'title': ['This field is required.']})

    def test_get_success_url_with_valid_data_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_update', args=(self.category.slug, self.post.pk, self.post.slug)),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': 'test post',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('posts:postDetail', args=(self.category.slug, self.post.pk, self.post.slug)))

    def test_get_success_url_with_invalid_data_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_update', args=(self.category.slug, self.post.pk, self.post.slug)),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': '',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'title': ['This field is required.']})

    def test_get_success_url_with_valid_data_delete(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_delete', args=(self.category.slug, self.post.pk, self.post.slug)),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': 'test post',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('user:viewProfile'))

    def test_get_success_url_with_invalid_data_delete(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_delete', args=(self.category.slug, self.post.pk, self.post.slug)),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': '',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors, {'title': ['This field is required.']})


class TestForm_valid_cd84ba476e(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='test category', slug='test-category')

    def test_form_valid(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(
            reverse('posts:post_create'),
            data={
                'category': self.category.pk,
                'tags': 'test tag',
                'title': 'test post',
                'image': 'test_image.jpg',
                'content': 'test content'
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('posts:postDetail', args=(self.category.slug, self.post.pk, self.post.slug)))


class TestGetHitCount_8bbc39393b(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='test category', slug='test-category')
        self.post = Post.objects.create(
            author=self.user,
            category=self.category,
            title='test post',
            slug='test-post',
            content='test content'
        )

    def test_get_hit_count(self):
        hit_count = HitCount.objects.get(post=self.post)
        self.assertEqual(hit_count.hits, 0)
        self.client.get(reverse('posts:postDetail', args=(self.category.slug, self.post.pk, self.post.slug)))
        hit_count.refresh_from_db()
        self.assertEqual(hit_count.hits, 1)


class Test___str___57494adc14(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='test category', slug='test-category')
        self.post = Post.objects.create(
            author=self.user,
            category=self.category,
            title='test post',
            slug='test-post',
            content='test content'
        )

    def test___str__(self):
        self.assertEqual(str(self.post), 'test post')


class TestPosts(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.category = Category.objects.create(name='test category', slug='test-category')
        self.post = Post.objects.create(
            author=self.user,
            category=self.category,
            title='test post',
            slug='test-post',
            content='test content'
        )

    def test_posts_list(self):
        response = self.client.get(reverse('posts:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test post')

    def test_post_detail(self):
        response = self.client.get(reverse('posts:postDetail', args=(self.category.slug, self.post.pk, self.post.slug)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test post')

    def test_post_create(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('posts:post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Post')

    def test_post_update(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('posts:post_update', args=(self.category.slug, self.post.pk, self.post.slug)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Update Post')

    def test_post_delete(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('posts:post_delete', args=(self.category.slug, self.post.pk, self.post.slug)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Delete Post')


if __name__ == '__main__':
    unittest.main()
