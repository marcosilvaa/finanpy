from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.views.generic import ListView

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
