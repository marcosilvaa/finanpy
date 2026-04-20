# Estado atual

## Implementado

- Projeto Django criado.
- Configuracao principal em `config/`.
- Django Admin disponivel em `/admin/`.
- SQLite configurado como banco local.
- Variaveis de ambiente gerenciadas via `python-decouple` (arquivo `.env` na raiz).
  - `SECRET_KEY` lida do `.env`.
  - `DEBUG` lido do `.env` (padrao `False`).
  - `ALLOWED_HOSTS` lido do `.env` (padrao `localhost,127.0.0.1`).
- `LANGUAGE_CODE = 'pt-br'` e `TIME_ZONE = 'America/Sao_Paulo'` configurados.
- Apps criados e registrados:
  - `accounts`
  - `categories`
  - `profiles`
  - `transactions`
  - `users`
- Estrutura padrao de cada app:
  - `admin.py`
  - `apps.py`
  - `models.py`
  - `tests.py`
  - `views.py`
  - `migrations/__init__.py`

- TailwindCSS integrado via `django-tailwind==3.8.0`:
  - App `theme` gerado e registrado em `INSTALLED_APPS`.
  - `TAILWIND_APP_NAME = 'theme'` configurado em `config/settings.py`.
  - `NPM_BIN_PATH = '/opt/homebrew/bin/npm'` configurado em `config/settings.py`.
  - Dependencias Node instaladas em `theme/static_src/node_modules/`.

- `AUTH_USER_MODEL = 'users.CustomUser'` configurado em `config/settings.py`.
- `CustomUser` (app `users`): herda de `AbstractUser`, login via `email` (campo unico), `REQUIRED_FIELDS = []`, campos `created_at` e `updated_at`, `__str__` retorna email.
- Migracao inicial do app `users` gerada: `users/migrations/0001_initial.py`.
- `Profile` (app `profiles`): perfil complementar vinculado ao usuario, com `full_name`, `phone`, `created_at` e `updated_at`.
- `Account` (app `accounts`): conta bancaria vinculada ao usuario, com nome, banco, tipo, saldo, status ativo e timestamps.
- Admin de `Account` configurado para listar, filtrar e buscar contas bancarias.
- `AccountForm` (app `accounts`) criado para cadastro e edicao de contas, com labels em portugues e classes TailwindCSS nos campos.
- `AccountListView` (app `accounts`) criada para listar contas do usuario autenticado, ordenadas por nome, com saldo total consolidado no contexto.
- `AccountCreateView` (app `accounts`) criada para cadastrar contas do usuario autenticado usando `AccountForm`, associando a conta ao usuario logado e exibindo mensagem de sucesso.
- Template `templates/accounts/account_list.html` criado para exibir contas do usuario, saldo total consolidado, estado vazio e botoes de acao ainda desabilitados enquanto as URLs de CRUD nao existem.
- Pagina inicial publica em `/`.
- Rotas de autenticacao no app `users`:
  - `/auth/signup/`: cadastro com email e senha.
  - `/auth/login/`: login com email e senha.
  - `/auth/logout/`: logout via POST.
- Templates existentes:
  - `templates/base.html`
  - `templates/home.html`
  - `templates/includes/navbar.html`
  - `templates/auth/signup.html`
  - `templates/auth/login.html`
  - `templates/accounts/account_list.html`
- Testes de autenticacao e home em `users/tests.py`.
- Testes da listagem e criacao de contas em `accounts/tests.py`, cobrindo isolamento por usuario, ordenacao por nome, saldo total, protecao por autenticacao e associacao da conta criada ao usuario logado.

## Nao implementado ainda

- Migration do model `Account`.
- Models de categorias e transacoes.
- Admin customizado para categorias e transacoes.
- URLs dos apps de produto (`accounts`, `categories`, `profiles`, `transactions`).
- Demais views de produto.
- Templates de criacao, edicao e exclusao de contas.
- Dashboard.
- CRUD de contas.
- CRUD de categorias.
- CRUD de transacoes.
- Filtros de transacoes.
- Calculo de saldos.
- Testes de regras financeiras alem da listagem de contas.

## Como ler o `PRD.md`

O `PRD.md` descreve a visao e os requisitos planejados para o Finanpy. Nem todos os itens do `PRD.md` existem no codigo atual.

Ao implementar novas partes, use o `PRD.md` como guia, mas atualize esta documentacao apenas com comportamento que realmente existir no projeto.
