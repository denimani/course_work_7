from rest_framework import serializers

from habit.models import PleasantHabit, UnpleasantHabit


class PleasantHabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор представления приятной привычки
    """

    class Meta:
        model = PleasantHabit
        fields = '__all__'
        # validators = [HabitDurationValidator(field='duration')]


class GoodHabitCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор представления создания неприятной привычки
    """

    class Meta:
        model = UnpleasantHabit
        fields = '__all__'
        # validators = [HabitDurationValidator(field='duration')]

    def validate(self, attrs):
        """
        Валидация данных
        """

        if 'pleasant_habit' in attrs:
            pleasant_habit_id = attrs.get('pleasant_habit').id
            pleasant_habit = PleasantHabit.objects.filter(id=pleasant_habit_id).first()
            # Проверка признака приятной привычки
            if pleasant_habit.is_pleasant_habit is not True:
                raise serializers.ValidationError(
                    'Related habits can only include habits with a sign of a pleasant habit')
        # Проверка того, чтобы была выбрана или привычка, или действие
        if attrs.get('pleasant_habit') is None and attrs.get('reward') is None:
            raise serializers.ValidationError("You must choose a related habit or specify a reward!")
        # Исключение одновременного выбора связанной привычки и указания вознаграждения
        if attrs.get('pleasant_habit') and attrs.get('reward'):
            raise serializers.ValidationError(
                "Невозможно одновременно выбрать связанную привычку и указать вознаграждение!")
        return attrs
