# Setup de desenvolvimento

## Requisitos

- Python `>=3.13`.
- Poetry, conforme `pyproject.toml`.
- Django `>=6.0.4,<7.0.0`.

## Instalar dependencias

```bash
poetry install
```

## Rodar migracoes

```bash
poetry run python manage.py migrate
```

## Iniciar servidor local

```bash
poetry run python manage.py runserver
```

A URL configurada no projeto hoje e apenas:

- `/admin/`: Django Admin.

## Rodar testes

```bash
poetry run python manage.py test
```

Os arquivos de teste existem nos apps, mas ainda contem apenas o scaffold padrao do Django.

## Banco de dados local

O projeto usa SQLite no arquivo `db.sqlite3`, configurado em `config/settings.py`.

## Ambiente atual

`DEBUG = True` e `ALLOWED_HOSTS = []` indicam configuracao de desenvolvimento. Antes de qualquer uso em producao, essas configuracoes precisam ser revisadas.
