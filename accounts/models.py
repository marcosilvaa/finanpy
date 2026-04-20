from django.contrib.auth import get_user_model
from django.db import models


class Account(models.Model):
    class AccountType(models.TextChoices):
        CHECKING = 'CHECKING', 'Conta corrente'
        SAVINGS = 'SAVINGS', 'Poupança'
        WALLET = 'WALLET', 'Carteira'

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='accounts',
    )
    name = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
    )
    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'conta bancária'
        verbose_name_plural = 'contas bancárias'
        ordering = ['name']
        indexes = [
            models.Index(
                fields=['user', 'is_active'],
                name='accounts_user_active_idx',
            ),
            models.Index(
                fields=['user', 'account_type'],
                name='accounts_user_type_idx',
            ),
        ]
