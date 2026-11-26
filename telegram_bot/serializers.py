from rest_framework import serializers

from telegram_bot.models import TelegramProfile


class TelegramProfileSerializer(serializers.ModelSerializer):
    """Сериализатор привязки Telegram."""

    class Meta:
        model = TelegramProfile
        fields = ('id', 'chat_id')
        read_only_fields = ('id',)