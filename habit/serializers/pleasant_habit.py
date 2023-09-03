from rest_framework import serializers

from habit.models import PleasantHabit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = PleasantHabit
        fields = '__all__'
