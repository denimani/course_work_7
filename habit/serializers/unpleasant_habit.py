from rest_framework import serializers

from habit.models import UnpleasantHabit
from habit.validators import validate_habit_time


class UnpleasantHabitCreateSerializer(serializers.ModelSerializer):
    duration = serializers.IntegerField(validators=[validate_habit_time])

    class Meta:
        model = UnpleasantHabit
        fields = '__all__'
