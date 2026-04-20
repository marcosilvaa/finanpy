from decimal import Decimal

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.db import connection
from django.test import RequestFactory, TransactionTestCase
from django.urls import reverse

from accounts.models import Account
from accounts.views import AccountListView


User = get_user_model()


class AccountListViewTests(TransactionTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        existing_tables = connection.introspection.table_names()
        cls.created_account_table = Account._meta.db_table not in existing_tables
        # Account migration is scheduled for Sprint 2.12.
        if cls.created_account_table:
            with connection.schema_editor() as schema_editor:
                schema_editor.create_model(Account)

    @classmethod
    def tearDownClass(cls):
        if cls.created_account_table:
            with connection.schema_editor() as schema_editor:
                schema_editor.delete_model(Account)
        super().tearDownClass()

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            email='user@example.com',
            password='password123',
        )
        self.other_user = User.objects.create_user(
            email='other@example.com',
            password='password123',
        )

    def build_view(self):
        request = self.factory.get('/accounts/')
        request.user = self.user
        view = AccountListView()
        view.setup(request)
        return view

    def test_get_queryset_filters_by_request_user_and_orders_by_name(self):
        Account.objects.create(
            user=self.user,
            name='Conta B',
            bank_name='Banco 1',
            account_type=Account.AccountType.CHECKING,
            balance=Decimal('100.00'),
        )
        Account.objects.create(
            user=self.user,
            name='Conta A',
            bank_name='Banco 2',
            account_type=Account.AccountType.SAVINGS,
            balance=Decimal('200.00'),
        )
        Account.objects.create(
            user=self.other_user,
            name='Conta Z',
            bank_name='Banco 3',
            account_type=Account.AccountType.WALLET,
            balance=Decimal('300.00'),
        )

        view = self.build_view()

        accounts = list(view.get_queryset())

        self.assertEqual(
            [account.name for account in accounts],
            ['Conta A', 'Conta B'],
        )
        self.assertTrue(
            all(account.user_id == self.user.id for account in accounts)
        )

    def test_anonymous_user_is_redirected_to_login(self):
        request = self.factory.get('/accounts/')
        request.user = AnonymousUser()

        response = AccountListView.as_view()(request)

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('users:login'), response['Location'])

    def test_get_context_data_adds_total_balance_for_request_user_only(self):
        Account.objects.create(
            user=self.user,
            name='Conta A',
            bank_name='Banco 1',
            account_type=Account.AccountType.CHECKING,
            balance=Decimal('150.50'),
        )
        Account.objects.create(
            user=self.user,
            name='Conta B',
            bank_name='Banco 2',
            account_type=Account.AccountType.SAVINGS,
            balance=Decimal('99.50'),
        )
        Account.objects.create(
            user=self.other_user,
            name='Conta X',
            bank_name='Banco 3',
            account_type=Account.AccountType.WALLET,
            balance=Decimal('1000.00'),
        )

        view = self.build_view()

        context = view.get_context_data(object_list=view.get_queryset())

        self.assertEqual(context['total_balance'], Decimal('250.00'))
        self.assertEqual(
            list(context['accounts'].values_list('name', flat=True)),
            ['Conta A', 'Conta B'],
        )
