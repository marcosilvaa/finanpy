from django import forms

from .models import Account


FIELD_CLASSES = (
    'block w-full rounded-lg border border-border-default bg-bg-secondary '
    'px-4 py-3 text-text-primary placeholder-text-secondary shadow-sm '
    'transition-colors focus:border-accent-primary focus:outline-none '
    'focus:ring-2 focus:ring-accent-primary/40'
)


class AccountForm(forms.ModelForm):
    account_type = forms.ChoiceField(
        choices=(
            ('', 'Selecione o tipo de conta'),
            (Account.AccountType.CHECKING, 'Conta corrente'),
            (Account.AccountType.SAVINGS, 'Poupança'),
            (Account.AccountType.WALLET, 'Carteira'),
        ),
        label='Tipo de conta',
        widget=forms.Select(
            attrs={
                'class': FIELD_CLASSES,
            }
        ),
    )

    class Meta:
        model = Account
        fields = ('name', 'bank_name', 'account_type', 'balance')
        labels = {
            'name': 'Nome da conta',
            'bank_name': 'Banco',
            'balance': 'Saldo atual',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': FIELD_CLASSES,
                    'placeholder': 'Ex.: Conta principal',
                }
            ),
            'bank_name': forms.TextInput(
                attrs={
                    'class': FIELD_CLASSES,
                    'placeholder': 'Ex.: Nubank',
                }
            ),
            'balance': forms.NumberInput(
                attrs={
                    'class': FIELD_CLASSES,
                    'placeholder': '0,00',
                    'step': '0.01',
                }
            ),
        }
