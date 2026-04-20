from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'is_staff', 'is_active', 'date_joined']
    ordering = ['email']


admin.site.register(CustomUser, CustomUserAdmin)
