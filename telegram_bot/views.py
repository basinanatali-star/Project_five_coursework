from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from telegram_bot.serializers import TelegramProfileSerializer


class TelegramProfileCreateView(generics.CreateAPIView):
    """Привязка Telegram-чата к пользователю."""

    serializer_class = TelegramProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)