# Finanpy - Contexto do Projeto

## Visão Geral do Projeto
O Finanpy é um sistema de gestão de finanças pessoais moderno e eficiente, desenvolvido com Django e TailwindCSS. O objetivo é fornecer uma ferramenta simples para organizar contas bancárias, categorizar transações e visualizar o panorama financeiro através de um dashboard intuitivo.

### Principais Tecnologias
- **Backend:** Django 6.0.4 (Python 3.13+)
- **Frontend:** Django Template Language + TailwindCSS (via `django-tailwind`)
- **Banco de Dados:** SQLite (Desenvolvimento) / Preparado para PostgreSQL (Produção)
- **Gerenciador de Dependências:** Poetry
- **Estilo de Código:** PEP 8, aspas simples, nomes em inglês.

### Arquitetura de Apps
- `users`: Modelo de usuário customizado (`CustomUser`) com login via e-mail.
- `profiles`: Perfis de usuário com informações adicionais (nome, telefone).
- `accounts`: Gestão de contas bancárias (corrente, poupança, carteira).
- `categories`: Categorização de transações (Entradas/Saídas).
- `transactions`: Registro de movimentações financeiras.
- `theme`: App do TailwindCSS para gestão de estilos.

---

## Comandos Úteis

### Ambiente e Dependências
```bash
# Instalar dependências
poetry install

# Ativar ambiente virtual
poetry shell
```

### Banco de Dados e Migrations
```bash
# Gerar novas migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser
```

### Desenvolvimento (Frontend e Backend)
```bash
# Iniciar servidor Django
python manage.py runserver

# Iniciar compilador Tailwind (em outro terminal)
python manage.py tailwind start
```

---

## Convenções de Desenvolvimento

### Padrões de Código
- **Idioma:** Código (variáveis, classes, métodos) em **inglês**. Interface e documentação em **português**.
- **Aspas:** Preferência por **aspas simples** (`'string'`).
- **Models:** Todos os modelos devem incluir os campos `created_at` e `updated_at`.
- **Managers:** Utilizar Managers customizados quando necessário (ex: `CustomUserManager`).
- **Signals:** Utilizar signals para lógica desacoplada (ex: criação automática de perfil).

### Estrutura de Templates
- Localizados na raiz em `/templates`.
- Seguem a estrutura de pastas por app (ex: `templates/accounts/`).
- O template base está em `templates/base.html`.

### Estilo (TailwindCSS)
- O arquivo principal de estilos está em `theme/static_src/src/styles.css`.
- Configurações do Tailwind em `theme/static_src/tailwind.config.js`.
- **Nota:** O `NPM_BIN_PATH` no `settings.py` pode precisar de ajuste dependendo do ambiente (`/opt/homebrew/bin/npm` por padrão para macOS).

### Workflow com Agentes
O projeto utiliza uma estrutura de agentes de IA documentada em `agents/`. Cada agente possui um papel específico (Tech Lead, Backend, Frontend, QA) com diretrizes detalhadas em seus respectivos arquivos `.md`.

---

## Documentação Adicional
- `PRD.md`: Requisitos detalhados e visão do produto.
- `TASKS.md`: Roadmap e status atual das tarefas (Sprints).
- `AGENTS.md`: Guia de atuação dos agentes de IA no projeto.
- `docs/`: Documentação técnica detalhada sobre arquitetura e padrões.
