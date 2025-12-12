# Diretrizes de Desenvolvimento

Este documento descreve as diretrizes e padrões de desenvolvimento utilizados no projeto Finanpy.

## Linguagem e Codificação

- Código-fonte deve ser escrito em **inglês** (variáveis, funções, classes, comentários)
- Interface do usuário deve ser em **português brasileiro**
- Seguir convenções PEP8 para estilo de código Python
- Usar tipagem opcional quando apropriado

## Estrutura de Projeto

- Seguir estrutura modular com apps Django separados por domínio
- Cada app deve ter responsabilidades bem definidas
- Manter imports organizados e coesos
- Evitar dependências circulares entre apps

## Modelos

- Usar `snake_case` para nomes de modelos e campos
- Incluir métodos `__str__` em todos os modelos
- Definir `Meta` classes com ordenação padrão quando relevante
- Utilizar validators para validação de campos
- Implementar `created_at` e `updated_at` em modelos que precisarem de rastreamento temporal

## Views

- Preferir Class-Based Views (CBVs) quando possível
- Utilizar mixins para funcionalidades compartilhadas
- Proteger views que requerem autenticação com `LoginRequiredMixin`
- Manter lógica de negócios fora das views, preferencialmente nos models ou services

## Templates

- Seguir convenções Django para nomeação de templates
- Usar `snake_case` para nomes de arquivos de template
- Explorar herança de templates com `base.html`
- Utilizar includes para componentes reutilizáveis

## Formulários

- Herdar de `forms.ModelForm` ou `forms.Form` conforme necessário
- Implementar validação customizada nos métodos `clean_*`
- Utilizar `ModelForm` para forms que interagem diretamente com modelos
- Fazer uso dos widgets do Django quando necessário para controle de input

## Testes

- Escrever testes unitários para lógica de negócios
- Cobrir funcionalidades críticas com testes de aceitação
- Utilizar fixtures ou factories para dados de teste
- Manter cobertura de testes em níveis razoáveis

## Git e Versionamento

- Utilizar mensagens de commit claras e descritivas em inglês
- Seguir convenção de commits: `tipo(scope): descrição`
- Tipos comuns: feat, fix, docs, style, refactor, test, chore
- Manter branch main estável
- Utilizar branches feature para desenvolvimento

## Segurança

- Sanitizar entradas de usuário
- Utilizar proteção CSRF do Django
- Prevenir SQL injection com queries ORM
- Validar e sanitizar uploads quando implementados