from django.test import TestCase

from telegram_bot.models import TelegramProfile
from users.models import CustomUser


class TelegramProfileTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='telegram_user',
            password='test12345'
        )

    def test_create_telegram_profile(self):
        profile = TelegramProfile.objects.create(
            user=self.user,
            chat_id='123456789'
        )

        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.chat_id, '123456789')

    def test_telegram_profile_str(self):
        profile = TelegramProfile.objects.create(
            user=self.user,
            chat_id='123456789'
        )

        self.assertEqual(
            str(profile),
            f'Telegram для {self.user}'
        )
