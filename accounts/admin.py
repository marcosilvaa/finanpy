from django.contrib import admin

from .models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user_email',
        'name',
        'bank_name',
        'account_type',
        'balance',
        'is_active',
    )
    list_filter = ('account_type', 'is_active')
    search_fields = ('name', 'bank_name', 'user__email')
    readonly_fields = ('created_at', 'updated_at')

    @admin.display(description='user email', ordering='user__email')
    def user_email(self, obj):
        return obj.user.email
