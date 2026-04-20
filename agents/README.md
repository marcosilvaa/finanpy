# Agentes do Finanpy

Indice dos agentes de IA recomendados para produzir codigo no Finanpy.

Use estes agentes conforme a natureza da tarefa. Todos devem ler primeiro `AGENT.md`, `docs/readme.md`, os documentos relevantes em `docs/`, o `PRD.md` e o codigo atual antes de propor ou alterar implementacoes.

## Agentes

| Agente | Arquivo | Quando usar |
| --- | --- | --- |
| Tech Lead Django | [tech-lead-django.md](tech-lead-django.md) | Para quebrar funcionalidades em tarefas tecnicas, revisar limites entre apps, decidir arquitetura Django simples e validar aderencia ao PRD e a documentacao. |
| Backend Django | [backend-django.md](backend-django.md) | Para models, migrations, admin, forms, views, URLs, autenticacao, regras de negocio, queries, permissoes e testes de dominio. |
| Frontend Django Templates e TailwindCSS | [frontend-django-tailwind.md](frontend-django-tailwind.md) | Para templates Django, TailwindCSS, layouts responsivos, tema escuro, formularios, feedback visual e JavaScript vanilla minimo. |
| QA Playwright | [qa-playwright.md](qa-playwright.md) | Para validar fluxos no navegador, responsividade, regressao visual, acessibilidade basica, testes end-to-end e funcionamento real do sistema. |

## Stack de referencia

- Python `>=3.13`.
- Django `>=6.0.4,<7.0.0`.
- Poetry.
- SQLite em desenvolvimento.
- Django Template Language.
- TailwindCSS.
- JavaScript vanilla apenas quando necessario.
- Django Auth nativo.

## Regras comuns

- O codigo novo deve ser escrito em ingles.
- Textos de interface e mensagens ao usuario devem ser em portugues.
- Use aspas simples em codigo novo.
- Siga PEP 8 e evite over-engineering.
- Preserve o isolamento de dados por usuario.
- Mantenha regras de dominio no app dono da responsabilidade.
- Models de dominio devem ter `created_at` e `updated_at`.
- Atualize a documentacao em `docs/` quando uma funcionalidade real mudar.

## Uso de MCPs

- Agentes que implementam codigo tecnico devem usar o MCP server `context7` antes de escrever ou alterar codigo dependente de Django, TailwindCSS, Python, Poetry ou APIs relevantes. O objetivo e usar documentacao atualizada da stack real do projeto.
- O agente de QA deve usar o MCP server `playwright` para acessar o sistema em execucao, testar fluxos, conferir responsividade e verificar se o design funciona como esperado.
