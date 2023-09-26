import unittest
from views import form_valid

class TestFormValid(unittest.TestCase):

    def test_Form_valid_cd84ba476e(self):
        form = form_valid(self)
        self.assertTrue(form.is_valid())

    def test_Form_valid_cd84ba476f(self):
        form = form_valid(self)
        self.assertFalse(form.is_valid())

    def test_Form_valid_cd84ba476g(self):
        form = form_valid(self)
        self.assertTrue(form.is_valid())
        post = form.save(commit=False)
        post.author = self.request.user
        post.slug = slugify(post.title)
        counter = 1
        temp_slug = post.slug

        while Post.objects.filter(
                slug=post.slug).exists():  # If there is the same information in the database, it is created by adding 1 to the end.
            post.slug = '{}-{}'.format(temp_slug, counter)
            counter += 1

        form.save()
        messages.success(self.request, 'Your post has been successfully created.')
        self.assertEqual(post.slug, '{}-{}'.format(temp_slug, counter))

if __name__ == '__main__':
    unittest.main()
