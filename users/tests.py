from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


def make_user(email='user@example.com', password='ValidPass123!'):
    return User.objects.create_user(
        email=email,
        password=password,
        username=email,
    )


class SignupViewTests(TestCase):
    def test_signup_creates_user(self):
        self.client.post(reverse('users:signup'), {
            'email': 'new@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(User.objects.filter(email='new@example.com').count(), 1)

    def test_signup_logs_in_after_creation(self):
        self.client.post(reverse('users:signup'), {
            'email': 'new@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(
            int(self.client.session['_auth_user_id']),
            User.objects.get(email='new@example.com').pk,
        )

    def test_signup_redirects_to_home(self):
        response = self.client.post(reverse('users:signup'), {
            'email': 'new@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertRedirects(response, reverse('home'), fetch_redirect_response=False)

    def test_signup_duplicate_email_shows_error(self):
        make_user(email='existing@example.com')
        response = self.client.post(reverse('users:signup'), {
            'email': 'existing@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Este e-mail já está cadastrado.')

    def test_signup_page_loads(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)


class LoginViewTests(TestCase):
    def setUp(self):
        self.user = make_user()

    def test_valid_credentials_log_in_user(self):
        self.client.post(reverse('users:login'), {
            'email': 'user@example.com',
            'password': 'ValidPass123!',
        })
        self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)

    def test_valid_credentials_redirect_to_home(self):
        response = self.client.post(reverse('users:login'), {
            'email': 'user@example.com',
            'password': 'ValidPass123!',
        })
        self.assertRedirects(response, reverse('home'), fetch_redirect_response=False)

    def test_invalid_credentials_show_error(self):
        response = self.client.post(reverse('users:login'), {
            'email': 'user@example.com',
            'password': 'WrongPassword!',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'E-mail ou senha inválidos.')

    def test_login_page_loads(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_credentials_do_not_create_session(self):
        self.client.post(reverse('users:login'), {
            'email': 'user@example.com',
            'password': 'WrongPassword!',
        })
        self.assertNotIn('_auth_user_id', self.client.session)


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = make_user()

    def test_logout_ends_session(self):
        self.client.force_login(self.user)
        self.client.post(reverse('users:logout'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_logout_redirects(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


class HomeViewTests(TestCase):
    def setUp(self):
        self.user = make_user()

    def test_anonymous_user_sees_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_authenticated_user_redirected_to_accounts(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, '/accounts/', fetch_redirect_response=False)
