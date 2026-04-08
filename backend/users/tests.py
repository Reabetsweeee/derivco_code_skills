from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')

    def test_user_email(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_password_is_hashed(self):
        self.assertNotEqual(self.user.password, 'TestPass123!')

    def test_str_method(self):
        self.assertEqual(str(self.user), 'testuser')