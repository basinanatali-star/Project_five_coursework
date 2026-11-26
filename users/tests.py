from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from users.models import CustomUser


class UserModelTest(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create_user(
            username='test_user',
            password='test12345'
        )

        self.assertEqual(user.username, 'test_user')
        self.assertTrue(user.check_password('test12345'))


class UserRegisterTest(APITestCase):

    def test_register_user(self):
        url = reverse('register')

        data = {
            'username': 'new_user',
            'password': 'test12345',
            'email': 'test@example.com'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
