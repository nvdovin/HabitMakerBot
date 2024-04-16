from django.db import models


# Create your models here.

class UsefulHabit(models.Model):
    habit_title = models.CharField(verbose_name="Полезная привычка", max_length=200)
    habit_description = models.TextField(verbose_name="Описание привычки", null=True, blank=True)

    class Meta:
        verbose_name = "Полезная привычка"
        verbose_name_plural = "Полезные привычки"


class Award(models.Model):
    award_title = models.CharField(verbose_name="Награда", max_length=200)
    award_description = models.TextField(verbose_name="Описание награды", null=True, blank=True)

    class Meta:
        verbose_name = "Награда"
        verbose_name_plural = "Награды"


class Habits(models.Model):
    habit_title = models.CharField(verbose_name="Название привычки", max_length=200)
    habit_description = models.TextField(verbose_name="Описание привычки", null=True, blank=True)
    act_time = models.TimeField(verbose_name="Время выполнения привычки", auto_now=True)
    last_changing = models.DateTimeField(verbose_name="Последнее редактирование", auto_now=True)
    date_of_creating = models.DateField(verbose_name="Дата создания привычки", auto_now_add=True)
    award = models.ForeignKey(to=Award, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Награда")
    useful_habit = models.ForeignKey(to=UsefulHabit, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
