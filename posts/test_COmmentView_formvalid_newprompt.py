from django.test import TestCase, RequestFactory
from django.contrib import messages
from unittest.mock import patch
from django.contrib.auth.models import User

from models import Category, Tag, HitCount, Comment, Post
from views import CommentView

# TODO: Replace 'YourAppName' with the name of the app where CommentForm is located
from YourAppName.forms import CommentForm

class CommentViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser', password='12345')

    @patch('YourAppName.views.CommentView.form_valid')
    def test_form_valid(self, mock_form_valid):
        request = self.factory.get('/dummy_url')
        request.user = self.user
     
        # Simulating the form being valid with the correct user and post_id set.
        form_data = {'content': 'test comment'}
        form = CommentForm(data=form_data)

        # TODO: Use the true pk of a post in your database
        test_pk = 1  # Set this to the pk of a post that does exist

        request.resolver_match.kwargs = {'pk': test_pk}

        if form.is_valid():
            view = CommentView()
            view.request = request
            view.form_valid(form)
        
        # Now we can check if the form is valid and if the attributes are set correctly.
        self.assertTrue(form.is_valid())
        self.assertEqual(form.instance.author, self.user)
        self.assertEqual(form.instance.post_id, test_pk)
        get_messages = list(messages.get_messages(request))
        self.assertEqual(str(get_messages[0]), 'Comment successfully added.')
        mock_form_valid.assert_called_once_with(form)