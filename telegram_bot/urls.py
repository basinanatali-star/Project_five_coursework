from django.urls import path

from telegram_bot.views import TelegramProfileCreateView


urlpatterns = [
    path('connect/', TelegramProfileCreateView.as_view(), name='telegram-connect'),
]