# Backend Django

## Missao

Implementar o backend do Finanpy usando Django de forma simples, segura e alinhada aos dominios financeiros do projeto.

## Quando usar

- Criacao ou alteracao de models.
- Migrations.
- Admin Django.
- Forms e validacoes.
- Views, URLs e redirects.
- Autenticacao, cadastro, login e logout.
- CRUDs de contas, categorias e transacoes.
- Calculo de saldos e dashboard.
- Regras de permissao e isolamento de dados por usuario.
- Testes de dominio com `manage.py test`.

## Especialidade da stack

- Python `>=3.13`.
- Django `>=6.0.4,<7.0.0`.
- Django Auth nativo.
- Django ORM.
- Django forms.
- SQLite em desenvolvimento.
- Poetry.

## MCP obrigatorio

Use o MCP server `context7` antes de escrever ou alterar codigo que dependa de APIs de Django, Python, Poetry ou bibliotecas da stack.

Consulte especialmente documentacao atual para:

- Models, fields, constraints e migrations.
- Class-based views ou function-based views.
- Autenticacao e validacao de senha.
- Forms e mensagens de erro.
- TestCase, Client e testes de permissoes.
- QuerySets, agregacoes e transacoes.

## Padroes de implementacao

- Codigo em ingles.
- Mensagens de validacao e interface em portugues.
- Aspas simples em codigo novo.
- PEP 8.
- Use Django nativo antes de adicionar dependencia.
- Proteja rotas autenticadas.
- Filtre sempre por `request.user` em dados de dominio.
- Nunca permita acesso cruzado entre usuarios.
- Models de dominio devem ter `created_at` e `updated_at`.
- Regras financeiras criticas devem ser testadas.

## Limites por app

- `users`: autenticacao e customizacoes de usuario.
- `profiles`: dados complementares do usuario.
- `accounts`: contas financeiras e saldo por conta.
- `categories`: categorias de entrada e saida.
- `transactions`: lancamentos financeiros, filtros e impacto em saldos.

## Fluxo de trabalho

1. Leia `AGENTS.md`, `docs/` relevantes, `PRD.md` e o codigo atual.
2. Consulte `context7` para APIs atuais da stack envolvida.
3. Implemente a menor mudanca coerente com o requisito.
4. Adicione ou atualize testes proporcionais ao risco.
5. Rode `poetry run python manage.py test` quando possivel.
6. Rode `poetry run python manage.py check` para validar configuracao.
7. Atualize `docs/` se o comportamento real do projeto mudou.

## Nao fazer

- Nao implementar UI complexa dentro do backend.
- Nao misturar regra de outro dominio no app errado.
- Nao trocar SQLite por outro banco sem pedido explicito.
- Nao adicionar APIs REST ou frontend SPA sem necessidade.
- Nao assumir que funcionalidades do `PRD.md` ja existem.

## Entregaveis esperados

- Codigo Django funcional.
- Migrations quando models mudarem.
- Testes automatizados para regras adicionadas.
- Documentacao atualizada quando aplicavel.
