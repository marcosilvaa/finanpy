# Setup de desenvolvimento

## Requisitos

- Python `>=3.13,<4.0.0`.
- Poetry, conforme `pyproject.toml`.
- Django `>=6.0.4,<7.0.0`.
- Node.js / npm disponivel em `/opt/homebrew/bin/npm` (necessario para TailwindCSS).

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

## Variaveis de ambiente

O projeto usa `python-decouple` para ler variaveis de um arquivo `.env` na raiz do projeto.
Crie o arquivo antes de rodar o servidor:

```
SECRET_KEY=sua-chave-secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

O arquivo `.env` esta no `.gitignore` e nao deve ser versionado.

## Ambiente atual

`DEBUG` e `ALLOWED_HOSTS` sao controlados pelo `.env`. O padrao de `DEBUG` sem `.env` e `False`.

## TailwindCSS

Para compilar o CSS em desenvolvimento, rode em um terminal separado:

```bash
poetry run python manage.py tailwind start
```

Para compilar uma vez para producao:

```bash
poetry run python manage.py tailwind build
```
