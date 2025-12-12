# Estrutura de Pastas

Esta documentação descreve a estrutura de pastas do projeto Finanpy e a responsabilidade de cada diretório.

## Estrutura Geral

```
finanpy/
├── .git/
├── .venv/
├── accounts/
├── categories/
├── core/
├── profiles/
├── transactions/
├── users/
├── .gitignore
├── .python-version
├── db.sqlite3
├── main.py
├── manage.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── uv.lock
└── docs/
```

## Descrição dos Diretórios

### `.git/`
- Diretório interno do Git para controle de versão

### `.venv/`
- Ambiente virtual do Python contendo as dependências do projeto

### `accounts/`
- App Django responsável pela autenticação e gerenciamento de usuários
- Contém modelo de usuário customizado com login por e-mail
- Implementa views e formulários de autenticação

### `categories/`
- App Django para gerenciamento de categorias de transações
- Permite criação, edição e exclusão de categorias personalizáveis
- Separa categorias por tipo (receita/despesa)

### `core/`
- App com funcionalidades centrais e páginas públicas
- Contém a view inicial (home) e configurações fundamentais
- Centraliza funcionalidades compartilhadas

### `profiles/`
- App Django para informações adicionais do usuário
- Gerencia perfil, avatar e configurações do usuário
- Conectado ao modelo de usuário via relacionamento 1:1

### `transactions/`
- App Django para registro e gerenciamento de transações financeiras
- Implementa operações CRUD para transações
- Relaciona transações com categorias e contas

### `users/`
- Referência ao modelo de usuário customizado extendido do Django
- Pode conter modelos, views ou lógica relacionada a usuários

### `docs/`
- Diretório contendo toda a documentação do projeto
- Documentos em formato Markdown (.md)
- Serve como referência para desenvolvedores e mantenedores

## Arquivos Principais

### `manage.py`
- Script de gerenciamento do Django
- Usado para rodar comandos como migrações, coletar statics, etc.

### `main.py`
- Ponto de entrada principal da aplicação Django
- Configurações centrais da aplicação

### `requirements.txt`
- Lista de dependências Python do projeto
- Define bibliotecas e versões necessárias

### `pyproject.toml`
- Arquivo de configuração para ferramentas de build e dependências modernas

### `db.sqlite3`
- Banco de dados SQLite padrão do Django
- Armazena dados da aplicação durante desenvolvimento

### `.gitignore`
- Especifica quais arquivos e diretórios devem ser ignorados pelo Git
- Inclui arquivos temporários, .env, __pycache__, etc.