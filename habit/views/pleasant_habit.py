from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from habit.models import PleasantHabit
from habit.paginators import HabitPagination
from habit.serializers.pleasant_habit import PleasantCreateHabitSerializer


class PleasantHabitListAPIView(ListAPIView):
    pagination_class = HabitPagination
    serializer_class = PleasantCreateHabitSerializer
    queryset = PleasantHabit.objects.all()


class PleasantHabitCreateAPIView(CreateAPIView):
    serializer_class = PleasantCreateHabitSerializer


class PleasantHabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = PleasantCreateHabitSerializer
    queryset = PleasantHabit.objects.all()


class PleasantHabitDestroyAPIView(DestroyAPIView):
    queryset = PleasantHabit.objects.all()


class PleasantHabitUpdateAPIView(UpdateAPIView):
    serializer_class = PleasantCreateHabitSerializer
    queryset = PleasantHabit.objects.all()
