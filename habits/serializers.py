from rest_framework import serializers
from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычек."""

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        """Проверка правильности создания привычки."""

        pleasant_habit = data.get(
            'pleasant_habit',
            self.instance.pleasant_habit if self.instance else False
        )

        related_habit = data.get(
            'related_habit',
            self.instance.related_habit if self.instance else None
        )

        reward = data.get(
            'reward',
            self.instance.reward if self.instance else None
        )

        time_spent = data.get(
            'time_spent',
            self.instance.time_spent if self.instance else 0
        )

        periodicity = data.get(
            'periodicity',
            self.instance.periodicity if self.instance else 1
        )

        errors = {}

        if time_spent > 120:
            errors['time_spent'] = (
                'Время выполнения не должно превышать 120 секунд.'
            )

        if not 1 <= periodicity <= 7:
            errors['periodicity'] = (
                'Периодичность должна быть от 1 до 7 дней.'
            )

        if pleasant_habit:
            if related_habit or reward:
                errors['non_field_errors'] = [
                    'У приятной привычки не может быть вознаграждения '
                    'или связанной привычки.'
                ]
        else:
            if related_habit and reward:
                errors['non_field_errors'] = [
                    'Нельзя одновременно указывать вознаграждение '
                    'и связанную привычку.'
                ]

            elif not related_habit and not reward:
                errors['non_field_errors'] = [
                    'Необходимо указать вознаграждение '
                    'или связанную приятную привычку.'
                ]

            if related_habit and not related_habit.pleasant_habit:
                errors.setdefault('non_field_errors', []).append(
                    'Связанная привычка должна быть приятной.'
                )

        if errors:
            raise serializers.ValidationError(errors)

        return data
