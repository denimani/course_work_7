from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from habit.models import UnpleasantHabit
from habit.paginators import HabitPagination
from habit.serializers.unpleasant_habit import UnpleasantHabitCreateSerializer


class UnpleasantHabitListAPIView(ListAPIView):
    pagination_class = HabitPagination
    serializer_class = UnpleasantHabitCreateSerializer
    queryset = UnpleasantHabit.objects.all()


class UnpleasantHabitCreateAPIView(CreateAPIView):
    serializer_class = UnpleasantHabitCreateSerializer


class UnpleasantHabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = UnpleasantHabitCreateSerializer
    queryset = UnpleasantHabit.objects.all()


class UnpleasantHabitDestroyAPIView(DestroyAPIView):
    queryset = UnpleasantHabit.objects.all()


class UnpleasantHabitUpdateAPIView(UpdateAPIView):
    serializer_class = UnpleasantHabitCreateSerializer
    queryset = UnpleasantHabit.objects.all()
