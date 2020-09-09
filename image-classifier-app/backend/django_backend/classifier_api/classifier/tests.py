from django.test import TestCase

from .models import User

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(name='test user')
        User.objects.create(email='testuser@example.com')
        User.objects.create(email='password')

    def test_name_content(self):
        user = User.objects.get(id=1)
        expected_object_name = f'{user.name}'
        self.assertEquals(expected_object_name, 'test user')

    def test_email_content(self):
        user = User.objects.get(id=2)
        expected_object_name = f'{user.email}'
        self.assertEquals(expected_object_name, 'testuser@example.com')

    def test_password_content(self):
        user = User.objects.get(id=3)
        expected_object_name = f'{user.password}'
        self.assertEquals(expected_object_name, 'password')
