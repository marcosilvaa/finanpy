# User Stories

Este documento apresenta as user stories que definem os requisitos funcionais do sistema Finanpy.

## Épico: Autenticação e Onboarding

### US-001: Cadastro de novo usuário
**Como** usuário novo,
**quero** me cadastrar com meu e-mail,
**para** acessar meu dashboard financeiro.

**Critérios de aceite:**
- Formulário de cadastro com campos: e-mail, senha (e confirmação de senha)
- Validação de formato de e-mail válido
- Validação de e-mail único no sistema
- Confirmação de senha igual à senha original
- Redirecionamento automático para `/dashboard` após cadastro bem-sucedido
- Mensagens de erro claras em português

### US-002: Login com e-mail
**Como** usuário cadastrado,
**quero** fazer login com meu e-mail,
**para** acessar minhas informações financeiras.

**Critérios de aceite:**
- Formulário com campos: e-mail e senha
- Validação de credenciais corretas
- Redirecionamento automático para `/dashboard` após login
- Mensagens de erro claras em português para credenciais inválidas
- Preservação do estado de sessão

### US-003: Logout
**Como** usuário logado,
**quero** fazer logout da aplicação,
**para** encerrar minha sessão de forma segura.

**Critérios de aceite:**
- Link ou botão de logout disponível em todas as páginas logadas
- Limpeza de dados de sessão
- Redirecionamento para página pública após logout

## Épico: Gestão de Transações

### US-004: Registro de transação
**Como** usuário logado,
**quero** registrar minhas receitas e despesas,
**para** acompanhar meu fluxo de caixa.

**Critérios de aceite:**
- Formulário com campos: valor, data, tipo (entrada/saída), categoria
- Validação de valor maior que zero
- Validação de data válida
- Filtro automático de categorias por tipo (receita/despesa)
- Mensagem de confirmação após registro
- Atualização imediata do saldo no dashboard

### US-005: Visualização de transações
**Como** usuário,
**quero** visualizar minhas transações registradas,
**para** acompanhar meu histórico financeiro.

**Critérios de aceite:**
- Listagem de transações com paginação (se necessário)
- Filtros por período, tipo, categoria
- Ordenação por data (padrão: mais recente primeiro)
- Formatação monetária adequada (R$)
- Diferenciação visual entre receitas (verde) e despesas (vermelho/rosa)

### US-006: Edição de transação
**Como** usuário,
**quero** editar uma transação previamente registrada,
**para** corrigir informações incorretas.

**Critérios de aceite:**
- Acesso à tela de edição para cada transação
- Formulário preenchido com dados atuais
- Validações aplicadas na atualização
- Mensagem de confirmação após alteração
- Atualização refletida na listagem e no saldo

### US-007: Exclusão de transação
**Como** usuário,
**quero** excluir uma transação indesejada,
**para** manter meus registros organizados.

**Critérios de aceite:**
- Confirmação antes da exclusão
- Mensagem de confirmação após exclusão
- Atualização do saldo e histórico
- Impedir exclusão de transações de sistemas críticos (se aplicável)

## Épico: Gestão de Categorias

### US-008: Criação de categorias
**Como** usuário,
**quero** criar minhas próprias categorias,
**para** organizar minhas finanças do meu jeito.

**Critérios de aceite:**
- Formulário para criar categoria com nome e tipo
- Validação de campos obrigatórios
- Restrição de categorias duplicadas por tipo e usuário
- Mensagem de confirmação após criação
- Disponibilização imediata para uso em transações

### US-009: Visualização de categorias
**Como** usuário,
**quero** visualizar minhas categorias,
**para** gerenciar e escolher categorias para minhas transações.

**Critérios de aceite:**
- Listagem com nome e tipo da categoria
- Agrupamento visual por tipo (receita/despesa)
- Indicador visual do número de transações associadas (opcional)
- Ordenação por nome ou data de criação

### US-010: Edição de categorias
**Como** usuário,
**quero** editar minhas categorias existentes,
**para** atualizar nomes ou tipos conforme necessário.

**Critérios de aceite:**
- Acesso à tela de edição para cada categoria
- Formulário preenchido com dados atuais
- Validações aplicadas na atualização
- Atualização refletida nas transações existentes
- Mensagem de confirmação após alteração

### US-011: Exclusão de categorias
**Como** usuário,
**quero** excluir categorias que não uso mais,
**para** manter minha lista de categorias organizada.

**Critérios de aceite:**
- Verificação de transações associadas antes da exclusão
- Impedimento de exclusão se houver transações vinculadas
- Confirmação antes da exclusão
- Mensagem de confirmação após exclusão bem-sucedida

## Épico: Dashboard Financeiro

### US-012: Visualização de resumo financeiro
**Como** usuário,
**quero** visualizar um resumo financeiro na página inicial,
**para** ter insights rápidos sobre minha situação.

**Critérios de aceite:**
- Exibição de saldo total atual
- Exibição de total de receitas e despesas no período (mês atual)
- Listagem das últimas 5 transações
- Indicador visual de saldo positivo/negativo
- Atualização em tempo real após novas transações

### US-013: Acesso a detalhes financeiros
**Como** usuário,
**quero** acessar informações detalhadas sobre minhas finanças,
**para** analisar meus padrões de receita e despesa.

**Critérios de aceite:**
- Links para visualização completa de transações
- Filtros rápidos para diferentes períodos
- Resumo por categorias (gráfico ou tabela)
- Exportação de dados (se implementado)