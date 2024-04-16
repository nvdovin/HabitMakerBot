from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    # Определите отображаемые поля и другие настройки административной панели
    list_display = ['name', 'user_id', 'registration_date']
    # Добавьте другие настройки, если необходимо

admin.site.register(User, CustomUserAdmin)
