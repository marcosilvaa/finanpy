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
- `urls.py`: rotas globais. Hoje registra apenas `/admin/`.
- `asgi.py` e `wsgi.py`: entradas padrao para servidores ASGI/WSGI.

## Apps existentes

Os apps estao registrados em `INSTALLED_APPS`:

- `accounts`: dominio de contas financeiras, conforme direcao do `PRD.md`.
- `categories`: dominio de categorias de transacoes.
- `profiles`: dominio de perfis de usuario.
- `transactions`: dominio de transacoes financeiras.
- `users`: dominio de usuarios.

Hoje esses apps existem como scaffold Django. Eles ainda nao possuem models, views ou regras de negocio implementadas.

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

`APP_DIRS = True` esta habilitado para templates de apps, mas nao ha templates no repositorio.

`STATIC_URL = "static/"` esta configurado, mas nao ha diretorio de static files no repositorio.
