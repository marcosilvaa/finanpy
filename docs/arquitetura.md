# Arquitetura

## Stack atual

- Linguagem: Python `>=3.13`.
- Framework: Django `>=6.0.4,<7.0.0`.
- Banco: SQLite.
- Gerenciador de dependencias: Poetry.

O `PRD.md` tambem define Django Template Language, TailwindCSS e JavaScript minimo como direcao para o frontend. Esses arquivos ainda nao existem no repositorio.

## Estrutura principal

```text
.
├── config/
├── accounts/
├── categories/
├── profiles/
├── transactions/
├── users/
├── manage.py
├── pyproject.toml
└── PRD.md
```

## Projeto Django

`config/` contem a configuracao principal do Django:

- `settings.py`: apps instalados, middleware, banco SQLite, templates e static files.
- `urls.py`: rotas globais. Registra `/admin/`, inclui `users.urls` em `/auth/` e aponta `/` para a pagina inicial.
- `asgi.py` e `wsgi.py`: entradas padrao para servidores ASGI/WSGI.

## Apps existentes

Os apps estao registrados em `INSTALLED_APPS`:

- `accounts`: dominio de contas financeiras. Possui o model `Account`, vinculado ao usuario e com tipo, saldo e status ativo. Tambem possui admin customizado, `AccountForm` para cadastro e edicao, `AccountListView` para listar contas do usuario autenticado com saldo total, `AccountCreateView` para cadastrar contas do usuario logado, e template de listagem de contas.
- `categories`: dominio de categorias de transacoes.
- `profiles`: dominio de perfis de usuario. Possui o model `Profile`, vinculado ao usuario.
- `transactions`: dominio de transacoes financeiras.
- `users`: dominio de usuarios, cadastro, login e logout.

Os apps `categories` e `transactions` ainda existem como scaffold Django. O app `accounts` possui model de dominio, admin customizado, form, views de listagem e criacao, e template de listagem; ainda nao possui URLs, migrations ou CRUD completo implementado.

## Banco de dados

O banco configurado e SQLite:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

O `PRD.md` cita possibilidade futura de migrar para PostgreSQL, mas o projeto atual usa apenas SQLite.

## Templates e arquivos estaticos

`APP_DIRS = True` esta habilitado para templates de apps.

Templates existentes:

- `templates/base.html`
- `templates/home.html`
- `templates/includes/navbar.html`
- `templates/auth/signup.html`
- `templates/auth/login.html`
- `templates/accounts/account_list.html`

`STATIC_URL = '/static/'` esta configurado. O CSS compilado pelo Tailwind fica em `theme/static/css/dist/styles.css`.
