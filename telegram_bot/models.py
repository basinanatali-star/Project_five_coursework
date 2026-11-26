from django.conf import settings
from django.db import models


class TelegramProfile(models.Model):
    """Связь пользователя сайта с Telegram."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='telegram_profile',
        verbose_name='Пользователь',
    )
    chat_id = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='ID Telegram-чата',
    )

    def __str__(self):
        return f'Telegram для {self.user}'
