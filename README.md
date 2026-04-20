# Finanpy

Aplicação de gestão financeira pessoal construída com Django e TailwindCSS.

## Stack

- Python 3.13+
- Django 6.x
- TailwindCSS (via django-tailwind)
- SQLite (desenvolvimento)
- Poetry

## Setup

```bash
# Instalar dependências
poetry install

# Copiar variáveis de ambiente
cp .env.example .env  # edite com seus valores

# Aplicar migrations
poetry run python manage.py migrate

# Criar superusuário
poetry run python manage.py createsuperuser

# Compilar assets Tailwind (em outro terminal)
poetry run python manage.py tailwind start

# Iniciar servidor
poetry run python manage.py runserver
```

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|---|---|---|
| `SECRET_KEY` | Chave secreta Django | — |
| `DEBUG` | Modo debug | `False` |
| `ALLOWED_HOSTS` | Hosts permitidos | `localhost,127.0.0.1` |
