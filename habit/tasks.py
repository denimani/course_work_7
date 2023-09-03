from datetime import datetime

from celery import shared_task
from django.conf import settings
from telebot import TeleBot

from habit.models import PleasantHabit, UnpleasantHabit


@shared_task
def pleasent_habit_notice():
    habits = PleasantHabit.objects.all()

    for habit in habits:
        if habit.time == datetime.now():
            bot = TeleBot(settings.TELEGRAM_TOKEN)
            message = f"Пришло время {habit.action}!"
            bot.send_message(habit.user.chat_id, message)


@shared_task
def unpleasant_habit_notice():
    habits = UnpleasantHabit.objects.all()

    for habit in habits:
        if habit.time == datetime.now():
            bot = TeleBot(settings.TELEGRAM_TOKEN)
            message = f"Пришло время {habit.action}!"
            bot.send_message(habit.user.chat_id, message)
