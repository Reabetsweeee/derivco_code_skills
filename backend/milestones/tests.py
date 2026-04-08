from django.test import TestCase
from django.contrib.auth import get_user_model
from projects.models import Project
from .models import Milestone

User = get_user_model()


class MilestoneModelTest(TestCase):

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
        self.milestone = Milestone.objects.create(
            project=self.project,
            title='First milestone',
            description='Get the backend working'
        )

    def test_milestone_created(self):
        self.assertEqual(self.milestone.title, 'First milestone')

    def test_default_not_completed(self):
        self.assertFalse(self.milestone.is_completed)

    def test_str_method(self):
        self.assertIn('First milestone', str(self.milestone))