from django.conf import settings
from django.db import models


class Habit(models.Model):
    """Модель полезной и приятной привычки."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Пользователь',
    )

    place = models.CharField(
        max_length=150,
        verbose_name='Место',
    )

    time = models.TimeField(
        verbose_name='Время выполнения',
    )

    action = models.CharField(
        max_length=255,
        verbose_name='Действие',
    )

    pleasant_habit = models.BooleanField(
        default=False,
        verbose_name='Приятная привычка',
    )

    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rewarded_habits',
        limit_choices_to={'pleasant_habit': True},
        verbose_name='Связанная привычка',
    )

    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Периодичность (дни)',
    )

    last_reminder_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата последнего напоминания',
    )

    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Вознаграждение',
    )

    time_spent = models.PositiveSmallIntegerField(
        verbose_name='Время на выполнение (секунды)',
    )

    public_habits = models.BooleanField(
        default=False,
        verbose_name='Публичная привычка',
    )


    def __str__(self):
        return f'{self.action} — {self.user}'


    class Meta:
        ordering = ('time', 'id')
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
