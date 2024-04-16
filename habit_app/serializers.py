from rest_framework import serializers
from .models import Award, Habits, UsefulHabit

class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = ["habit_title", "habit_description", "act_time",
                "award", "useful_habit"]


class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = "__all__"


class UsefulHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulHabit
        fields = "__all__"