# Arquitetura Técnica

## Stack

- **Backend**: Python 3.13+, Django 5+
- **Frontend**: Django Template Language + Tailwind CSS (via CDN ou build simples)
- **Banco de dados**: SQLite (padrão Django)
- **Autenticação**: Django Built-in (customizada para e-mail)
- **Deploy inicial**: Servidor de desenvolvimento do Django

## Estrutura de Dados

```mermaid
erDiagram
        User ||--|| Profile : "has"
        User ||--|{ Account : "owns"
        User ||--|{ Category : "defines"
        User ||--|{ Transaction : "makes"

        Account ||--|{ Transaction : "contains"
        Category ||--|{ Transaction : "classifies"

        User {
            int id
            string email "USERNAME_FIELD"
            string password
            string first_name
            datetime date_joined
        }

        Profile {
            int id
            int user_id FK
            string avatar_url
            datetime created_at
            datetime updated_at
        }

        Account {
            int id
            int user_id FK
            string name
            decimal initial_balance
            string type "bank, wallet"
            datetime created_at
            datetime updated_at
        }

        Category {
            int id
            int user_id FK
            string name
            string type "income, expense"
            string color_code
            datetime created_at
            datetime updated_at
        }

        Transaction {
            int id
            int user_id FK
            int account_id FK
            int category_id FK
            decimal amount
            string description
            date date
            boolean is_income
            datetime created_at
            datetime updated_at
        }
```

## Apps do Projeto

O projeto é organizado em apps Django modulares:

- `accounts`: Gerenciamento de autenticação e usuários
- `profiles`: Informações complementares dos usuários
- `categories`: Categorização de transações
- `transactions`: Registro de movimentações financeiras
- `core`: Funcionalidades básicas e páginas públicas
- `users`: (referência ao modelo de usuário customizado)

## Requisitos não-funcionais

- **Performance**: carregamento rápido com SQLite e sem sobrecarga.
- **Segurança**: uso do sistema nativo de autenticação do Django.
- **Usabilidade**: interface clara, com feedback visual em ações.
- **Manutenibilidade**: código limpo, seguindo PEP8 e em inglês.
- **Responsividade**: layout adaptável a dispositivos móveis e desktops.
- **Internacionalização**: mensagens em português brasileiro apenas na UI.