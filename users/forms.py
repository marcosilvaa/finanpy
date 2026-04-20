from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

FIELD_CLASSES = (
    'bg-gray-800 text-white border-gray-600 rounded-lg px-4 py-2 w-full '
    'focus:outline-none focus:ring-2 focus:ring-indigo-500'
)


class SignupForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = FIELD_CLASSES

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': FIELD_CLASSES}),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': FIELD_CLASSES}),
    )
