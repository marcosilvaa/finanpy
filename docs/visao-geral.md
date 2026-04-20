# Visao geral

## Produto

Finanpy e um sistema de gestao de financas pessoais feito com Python e Django.

O `PRD.md` define o produto como uma aplicacao web simples para organizar contas, categorias, transacoes e visualizacoes financeiras. No estado atual do repositorio, existe apenas a base Django e os apps separados por dominio.

## Objetivo

Fornecer uma base simples e manutenivel para evoluir um MVP de financas pessoais.

## Publico-alvo

Conforme o `PRD.md`, o produto mira pessoas que querem organizar financas pessoais sem complexidade excessiva, especialmente adultos e jovens profissionais que controlam contas, entradas e saidas.

## Escopo atual do codigo

O repositorio contem:

- Projeto Django em `config/`.
- Apps Django: `accounts`, `categories`, `profiles`, `transactions` e `users`.
- Configuracao com SQLite.
- URL do Django Admin em `/admin/`.
- Arquivos iniciais de `models.py`, `views.py`, `admin.py` e `tests.py` em cada app.

O repositorio ainda nao contem:

- Models de dominio implementados.
- Views ou URLs de produto.
- Templates, CSS ou JavaScript da aplicacao.
- Fluxos de autenticacao customizados.
- Dashboard, listagens, formularios ou filtros.
