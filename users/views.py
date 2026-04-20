from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from users.forms import LoginForm, SignupForm


class SignupView(CreateView):
    model = get_user_model()
    form_class = SignupForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            self.request,
            username=form.cleaned_data['email'],
            password=form.cleaned_data['password1'],
        )
        if user is not None:
            login(self.request, user)
        messages.success(
            self.request,
            'Conta criada com sucesso! Bem-vindo ao Finanpy.',
        )
        return response


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error(None, 'E-mail ou senha inválidos.')
        return self.form_invalid(form)


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        messages.success(request, 'Você saiu com sucesso.')
        return super().post(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'
