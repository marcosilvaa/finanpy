from django.contrib import admin

from profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_email', 'full_name', 'phone']
    search_fields = ['user__email', 'full_name']

    def user_email(self, obj):
        return obj.user.email

    user_email.short_description = 'Email'
