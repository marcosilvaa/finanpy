from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import CreateView, ListView

from .forms import AccountForm
from .models import Account


class AccountListView(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    model = Account
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_balance = (
            self.get_queryset()
            .aggregate(total_balance=Sum('balance'))['total_balance']
            or Decimal('0')
        )
        context['total_balance'] = total_balance
        return context


class AccountCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    model = Account
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = '/accounts/'
    extra_context = {
        'title': 'Nova Conta',
    }

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, 'Conta criada com sucesso.')
        return response
