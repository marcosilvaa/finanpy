# AGENT.md

Guia para agentes trabalhando no projeto Finanpy.

## Prioridade de contexto

Ao iniciar trabalho neste repositorio, leia nesta ordem:

1. `AGENT.md` para regras operacionais.
2. `docs/readme.md` para indice da documentacao.
3. Documentos em `docs/` conforme a tarefa.
4. `PRD.md` para visao de produto e requisitos planejados.
5. Codigo atual para confirmar o que realmente existe.

Quando houver conflito, o codigo atual e a documentacao em `docs/` descrevem o estado real. O `PRD.md` descreve a direcao do produto e pode conter funcionalidades ainda nao implementadas.

## Estado atual do projeto

Finanpy e um projeto Django inicial para gestao de financas pessoais.

Existe hoje:

- Projeto Django em `config/`.
- Django Admin em `/admin/`.
- SQLite configurado como banco local.
- Apps registrados: `accounts`, `categories`, `profiles`, `transactions`, `users`.
- Scaffold padrao dos apps com `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py` e `migrations/__init__.py`.

Ainda nao existe:

- Models de dominio.
- Views de produto.
- URLs dos apps.
- Templates.
- Arquivos estaticos.
- Autenticacao customizada por email.
- CRUDs.
- Dashboard.
- Calculo de saldos.
- Testes de regra de negocio.

Nao documente nem trate como pronta nenhuma funcionalidade que esteja apenas no `PRD.md`.

## Stack

- Python `>=3.13`.
- Django `>=6.0.4,<7.0.0`.
- Poetry.
- SQLite em desenvolvimento.

O `PRD.md` define como direcao futura:

- Django Template Language.
- TailwindCSS.
- JavaScript vanilla minimo.
- Interface responsiva com tema escuro.

Esses arquivos ainda nao existem no projeto.

## Comandos uteis

Instalar dependencias:

```bash
poetry install
```

Rodar migracoes:

```bash
poetry run python manage.py migrate
```

Rodar servidor local:

```bash
poetry run python manage.py runserver
```

Rodar testes:

```bash
poetry run python manage.py test
```

Verificar configuracao Django:

```bash
poetry run python manage.py check
```

Se Django nao estiver importavel, rode `poetry install` antes de validar.

## Padroes de codigo

Siga os padroes definidos em `docs/padroes-do-projeto.md`:

- Codigo em ingles.
- Mensagens de interface em portugues quando existirem telas.
- PEP 8.
- Aspas simples em codigo novo.
- Apps com responsabilidades bem definidas.
- Evitar over-engineering.
- Models de dominio devem incluir `created_at` e `updated_at`.

Observacao: parte do scaffold Django usa aspas duplas. Nao altere arquivos apenas para trocar aspas. Use aspas simples em codigo novo ou em linhas que voce ja estiver modificando por outro motivo.

## Responsabilidades dos apps

- `users`: usuario e autenticacao quando houver customizacao.
- `profiles`: dados complementares do usuario.
- `accounts`: contas financeiras.
- `categories`: categorias de entrada e saida.
- `transactions`: lancamentos financeiros.

Mantenha regra de negocio no app dono do dominio. Evite acoplamento desnecessario entre apps.

## Seguranca e dados

O produto lida com dados financeiros. Ao implementar funcionalidades:

- Use autenticacao nativa do Django quando possivel.
- Proteja rotas autenticadas.
- Garanta isolamento de dados por usuario.
- Nunca permita que um usuario acesse dados de outro.
- Use validacoes do Django para senhas e formularios.
- Centralize logica financeira sensivel, especialmente saldo e transacoes.

## Testes

Ao adicionar regras de dominio, adicione testes proporcionais ao risco.

Priorize testes para:

- Isolamento de dados por usuario.
- Criacao, edicao e exclusao de transacoes.
- Atualizacao e recalculo de saldos.
- Validacoes de contas, categorias e transacoes.
- Fluxos de autenticacao quando forem implementados.

## Documentacao

Mantenha `docs/` sincronizado com o codigo real.

Ao implementar uma funcionalidade, atualize a documentacao correspondente:

- `docs/estado-atual.md` para listar o que passou a existir.
- `docs/arquitetura.md` para mudancas estruturais.
- `docs/padroes-do-projeto.md` para convencoes novas.
- `docs/setup-desenvolvimento.md` para comandos ou dependencias novas.

Nao copie o `PRD.md` para a documentacao como se fosse implementacao existente.

## Git e edicoes

- Nao reverta alteracoes de outras pessoas.
- Antes de editar, confira o arquivo atual.
- Mantenha mudancas pequenas e focadas na tarefa.
- Evite refatoracoes sem relacao direta com o pedido.
- Nao commite a menos que o usuario peca.

## Criterio de conclusao

Antes de finalizar uma tarefa:

- Confirme que a mudanca bate com o estado real do projeto.
- Rode testes ou checks possiveis.
- Se nao conseguir rodar validacoes, informe o motivo.
- Cite arquivos alterados no resumo final.
