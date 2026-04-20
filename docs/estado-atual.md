# Estado atual

## Implementado

- Projeto Django criado.
- Configuracao principal em `config/`.
- Django Admin disponivel em `/admin/`.
- SQLite configurado como banco local.
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

## Nao implementado ainda

- Models de contas, categorias, perfis, transacoes ou usuarios customizados.
- Admin customizado para models de dominio.
- Views de produto.
- URLs dos apps.
- Templates.
- Arquivos estaticos.
- Autenticacao customizada por email.
- Cadastro, login e logout customizados.
- Dashboard.
- CRUD de contas.
- CRUD de categorias.
- CRUD de transacoes.
- Filtros de transacoes.
- Calculo de saldos.
- Testes de regra de negocio.

## Como ler o `PRD.md`

O `PRD.md` descreve a visao e os requisitos planejados para o Finanpy. Nem todos os itens do `PRD.md` existem no codigo atual.

Ao implementar novas partes, use o `PRD.md` como guia, mas atualize esta documentacao apenas com comportamento que realmente existir no projeto.
