from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, user_id, name, password=None):
        if not user_id:
            raise ValueError("Users must have an user_id")
        if not name:
            raise ValueError("Users must have an name")
        user = self.model(
            user_id=user_id,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    name = models.CharField(verbose_name="Имя пользователя", max_length=100)
    user_id = models.IntegerField(verbose_name="ID пользователя", unique=True)
    registration_date = models.DateField(verbose_name="Дата регистрации пользователя", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname} with id [{self.user_id}]."

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"