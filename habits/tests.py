from django.test import TestCase

from habits.models import Habit
from users.models import CustomUser
from habits.serializers import HabitSerializer
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class HabitModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='test_user',
            password='test12345'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place='Дом',
            time='07:00',
            action='Сделать зарядку',
            pleasant_habit=False,
            reward='Посмотреть фильм',
            periodicity=1,
            time_spent=60,
            public_habits=False
        )

    def test_habit_creation(self):
        self.assertEqual(self.habit.action, 'Сделать зарядку')

    def test_habit_user(self):
        self.assertEqual(self.habit.user, self.user)

    def test_habit_str(self):
        self.assertEqual(
            str(self.habit),
            f'Сделать зарядку — {self.user}'
        )


class HabitSerializerTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='serializer_user',
            password='test12345'
        )

        self.data = {
            'place': 'Дом',
            'time': '07:00:00',
            'action': 'Сделать зарядку',
            'pleasant_habit': False,
            'reward': 'Посмотреть фильм',
            'periodicity': 1,
            'time_spent': 60,
            'public_habits': False
        }

    def test_valid_data(self):
        serializer = HabitSerializer(data=self.data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_time_spent(self):
        self.data['time_spent'] = 180

        serializer = HabitSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_periodicity(self):
        self.data['periodicity'] = 10

        serializer = HabitSerializer(data=self.data)
        self.assertFalse(serializer.is_valid())


class HabitViewTest(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='api_user',
            password='test12345'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        url = reverse('habit-list')

        data = {
            'place': 'Дом',
            'time': '07:00:00',
            'action': 'Прочитать книгу',
            'pleasant_habit': False,
            'reward': 'Посмотреть фильм',
            'periodicity': 1,
            'time_spent': 60,
            'public_habits': False
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_habits(self):
        url = reverse('habit-list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)