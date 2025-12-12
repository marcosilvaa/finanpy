# Agentes de IA do Projeto Finanpy

Este diretório contém agentes especializados de IA para diferentes funções no desenvolvimento do sistema Finanpy. Cada agente é especialista em uma parte específica da stack tecnológica do projeto.

## Índice de Agentes

- [Backend Django Developer](django-backend-developer.md) - Especialista em desenvolvimento backend com Django Framework
- [Frontend Django Template & TailwindCSS Designer](frontend-dtl-tailwind.md) - Especialista em frontends com Django Template Language e TailwindCSS
- [QA/Tester](qa-tester.md) - Especialista em testes e garantia de qualidade
- [DevOps Engineer](devops-engineer.md) - Especialista em infraestrutura e deploy
- [Database Specialist](database-specialist.md) - Especialista em modelagem e banco de dados

## Descrição e Quando Usar Cada Agente

### Backend Django Developer
Especialista em desenvolvimento backend com Django Framework, Python 3.13+, Django 5+, e padrões de projeto Django. Responsável por implementar models, views, forms, autenticação personalizada por e-mail, e toda a lógica de backend.

**Quando usar**: 
- Implementação de models (User, Transaction, Category, etc.)
- Criação de views e URLs
- Implementação de autenticação personalizada
- Criação de forms e validações
- Integração de apps Django

### Frontend Django Template & TailwindCSS Designer
Especialista em criação de interfaces com Django Template Language e estilização com TailwindCSS. Conhece profundamente o design system do projeto, com tema escuro e paleta de cores específica.

**Quando usar**:
- Criação de templates Django
- Estilização com TailwindCSS
- Implementação do design system
- Criação de componentes reutilizáveis
- Responsividade e experiência do usuário

### QA/Tester
Especialista em testes e garantia de qualidade. Usa o MCP server do playwright para acessar o sistema e verificar se está funcionando como o esperado, e se o design está correto. Implementa testes automatizados e manuais.

**Quando usar**:
- Criação de testes de aceitação
- Testes de interface e design
- Verificação de funcionalidades
- Testes de regressão
- Validação de UX/UI

### DevOps Engineer
Especialista em infraestrutura, deploy e configuração do ambiente de desenvolvimento e produção.

**Quando usar**:
- Configuração de ambiente de desenvolvimento
- Deployment
- Configuração de servidores
- Gerenciamento de dependências
- Pipeline de CI/CD

### Database Specialist
Especialista em modelagem e banco de dados, com foco em SQLite e relações entre os modelos Django de acordo com o ERD do projeto.

**Quando usar**:
- Modelagem de dados
- Migrações de banco de dados
- Otimização de queries
- Validação de relacionamentos
- Consultas complexas