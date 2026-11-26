from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from habits.models import Habit
from habits.serializers import HabitSerializer
from habits.paginators import HabitPagination


class HabitViewSet(viewsets.ModelViewSet):
    """Представление для работы с привычками."""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='public')
    def public_habits(self, request):
        """Список публичных привычек."""
        habits = Habit.objects.filter(public_habits=True)
        page = self.paginate_queryset(habits)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(habits, many=True)
        return Response(serializer.data)
