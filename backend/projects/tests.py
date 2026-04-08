from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project

User = get_user_model()


class ProjectModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass123!'
        )
        self.project = Project.objects.create(
            owner=self.user,
            title='Test Project',
            description='A test project',
            status='planning'
        )

    def test_project_created(self):
        self.assertEqual(self.project.title, 'Test Project')

    def test_project_owner(self):
        self.assertEqual(self.project.owner, self.user)

    def test_project_default_status(self):
        self.assertEqual(self.project.status, 'planning')

    def test_str_method(self):
        self.assertEqual(str(self.project), 'Test Project')