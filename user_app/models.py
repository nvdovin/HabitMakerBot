from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    
    def create_superuser(self, user_id, name, password=None):
        user = self.create_user(
            user_id=user_id,
            name=name,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(verbose_name="Имя пользователя", max_length=100, unique=True)
    name = models.CharField(verbose_name="Имя пользователя", max_length=100)
    user_id = models.IntegerField(verbose_name="ID пользователя", unique=True)
    registration_date = models.DateField(verbose_name="Дата регистрации пользователя", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Последний вход", auto_now=True, null=True, blank=True)

    is_active = models.BooleanField(verbose_name="Активен", default=True)
    is_staff = models.BooleanField(verbose_name="Сотрудник", default=False)
    is_admin = models.BooleanField(verbose_name="Администратор", default=False)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self) -> str:
        return f"{self.name} with id [{self.user_id}]."

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"