from django.test import TestCase
from django.contrib.auth import get_user_model
from projects.models import Project
from .models import Comment, CollabRequest

User = get_user_model()


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass123!'
        )
        self.project = Project.objects.create(
            owner=self.user,
            title='Test Project',
            description='A test project'
        )
        self.comment = Comment.objects.create(
            project=self.project,
            author=self.user,
            body='This is a test comment'
        )

    def test_comment_created(self):
        self.assertEqual(self.comment.body, 'This is a test comment')

    def test_comment_author(self):
        self.assertEqual(self.comment.author, self.user)

    def test_str_method(self):
        self.assertIn('testuser', str(self.comment))


class CollabRequestModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass123!'
        )
        self.project = Project.objects.create(
            owner=self.user,
            title='Test Project',
            description='A test project'
        )
        self.collab = CollabRequest.objects.create(
            project=self.project,
            requester=self.user,
            message='I want to join!'
        )

    def test_collab_created(self):
        self.assertEqual(self.collab.message, 'I want to join!')

    def test_default_status(self):
        self.assertEqual(self.collab.status, 'pending')

    def test_str_method(self):
        self.assertIn('testuser', str(self.collab))