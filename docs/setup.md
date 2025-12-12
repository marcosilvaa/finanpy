# Configuração Inicial

Este guia detalha os passos necessários para configurar o ambiente de desenvolvimento do Finanpy.

## Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)
- Git

## Passos para Configuração

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd finanpy
```

### 2. Criar Ambiente Virtual

```bash
python -m venv .venv
source .venv/bin/activate  # No Linux/Mac
# ou
.venv\Scripts\activate     # No Windows
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

```bash
python manage.py migrate
```

### 5. Criar Superusuário

```bash
python manage.py createsuperuser
```

Siga as instruções para criar o usuário administrador.

### 6. Rodar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

A aplicação estará disponível em `http://127.0.0.1:8000/`.

## Configurações Adicionais

### Variáveis de Ambiente

Se necessário, crie um arquivo `.env` na raiz do projeto com configurações específicas do ambiente:

```env
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
DATABASE_URL=sqlite:///db.sqlite3
```

### Internacionalização

O projeto está configurado para usar Português Brasileiro como idioma padrão:
- `LANGUAGE_CODE = 'pt-br'`
- `TIME_ZONE = 'America/Sao_Paulo'`

## Troubleshooting

### Problemas com Dependências

Se encontrar problemas com dependências, tente:

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Problemas com Migrações

Para resolver problemas com migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Permissões de Arquivo

Certifique-se de que o ambiente virtual tem as permissões corretas para leitura e escrita.