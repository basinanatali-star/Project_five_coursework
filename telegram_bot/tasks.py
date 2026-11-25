import asyncio

from celery import shared_task
from telegram import Bot
from django.conf import settings
from django.utils import timezone

from telegram_bot.models import TelegramProfile
from habits.models import Habit


@shared_task
def send_habit_reminder(habit_id):
    """Отправка напоминания о привычке в Telegram."""

    habit = Habit.objects.get(pk=habit_id)

    try:
        profile = TelegramProfile.objects.get(user=habit.user)
    except TelegramProfile.DoesNotExist:
        return 'Telegram не подключён'

    message = (
        f'Напоминание о привычке!\n'
        f'Место: {habit.place}\n'
        f'Время: {habit.time}\n'
        f'Действие: {habit.action}'
    )

    async def send_message():
        async with Bot(token=settings.TELEGRAM_BOT_TOKEN) as bot:
            await bot.send_message(
                chat_id=profile.chat_id,
                text=message,
            )

    asyncio.run(send_message())

    habit.last_reminder_date = timezone.localdate()
    habit.save(update_fields=['last_reminder_date'])

    return 'Напоминание отправлено'


@shared_task
def check_habit_reminders():
    """Проверка привычек с учётом периодичности."""

    now = timezone.localtime()
    today = timezone.localdate()

    habits = Habit.objects.filter(
        time__hour=now.hour,
        time__minute=now.minute,
    )

    for habit in habits:
        if habit.last_reminder_date is None:
            send_habit_reminder.delay(habit.id)

        elif (today - habit.last_reminder_date).days >= habit.periodicity:
            send_habit_reminder.delay(habit.id)
