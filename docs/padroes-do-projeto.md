# Padroes do projeto

## Idioma

Conforme `PRD.md`:

- Codigo em ingles.
- Mensagens para usuarios em portugues quando existirem telas e validacoes.

## Estilo de codigo

Conforme `PRD.md`:

- Seguir PEP 8.
- Usar aspas simples em codigo novo.
- Manter apps com responsabilidades bem definidas.
- Evitar over-engineering.

Observacao: o scaffold atual criado pelo Django usa aspas duplas em alguns arquivos. Para codigo novo do projeto, usar aspas simples conforme padrao definido no `PRD.md`.

## Organizacao por apps

Cada app deve concentrar uma responsabilidade:

- `users`: usuario/autenticacao quando houver customizacao.
- `profiles`: dados complementares do usuario.
- `accounts`: contas financeiras.
- `categories`: categorias de entrada e saida.
- `transactions`: lancamentos financeiros.

Evite colocar regras de um dominio dentro de outro app sem necessidade.

## Models

O `PRD.md` define que models devem ter `created_at` e `updated_at`.

Como ainda nao ha models de dominio implementados, esse padrao deve ser seguido quando eles forem criados.

## Seguranca

Padroes definidos no `PRD.md` para quando as funcionalidades forem implementadas:

- Usar autenticacao nativa do Django.
- Proteger rotas autenticadas.
- Garantir que dados de um usuario nao sejam acessiveis por outro.
- Usar validacoes do Django para senha.
- Sanitizar entradas de usuario.

No codigo atual, ainda nao existem rotas autenticadas de produto nem regras de permissao de dominio.

## Frontend

O `PRD.md` define a direcao visual:

- Django Template Language.
- TailwindCSS.
- JavaScript vanilla apenas quando necessario.
- Interface responsiva.
- Tema escuro.
- Textos de interface em portugues.

Nenhum template ou arquivo estatico foi implementado ainda.

## Testes

Os apps possuem arquivos `tests.py`, ainda vazios.

Quando regras financeiras forem implementadas, priorizar testes para:

- Isolamento de dados por usuario.
- Calculo e atualizacao de saldos.
- Criacao, edicao e exclusao de transacoes.
- Validacoes de entrada.
