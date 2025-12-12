# Guia de Estilos e Design System

Este documento define o design system utilizado no projeto Finanpy, baseado em Tailwind CSS com tema escuro customizado.

## Paleta de Cores

### Cores Base
- **Fundo principal**: `bg-gray-900` (`#111827`)
- **Fundo de cards**: `bg-gray-800` (`#1f2937`)
- **Texto primário**: `text-gray-100` (`#f9fafb`)
- **Texto secundário**: `text-gray-400` (`#9ca3af`)
- **Borda**: `border-gray-700`

### Cores de Destaque
- **Receita**: `text-emerald-400` / `bg-emerald-900/30`
- **Despesa**: `text-rose-400` / `bg-rose-900/30`

### Gradientes
- Botões principais: `bg-gradient-to-r from-indigo-600 to-purple-600`
- Cards: `bg-gradient-to-br from-gray-800 to-gray-900`

## Tipografia

- Fonte padrão: **Inter** (via Google Fonts, carregada no base template)
- Títulos: `font-bold text-xl` a `text-3xl`
- Parágrafos: `text-base`

## Componentes

### Botões
- **Primário**: 
  - Classes: `px-4 py-2 rounded-lg font-medium text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:opacity-90 transition`
  - Uso: Ações principais, chamadas para ação
- **Secundário**: 
  - Classes: `px-4 py-2 rounded-lg font-medium text-gray-200 bg-gray-700 hover:bg-gray-600`
  - Uso: Ações secundárias
- **Destrutivo**: 
  - Classes: `bg-rose-800 hover:bg-rose-700`
  - Uso: Ações que excluem ou modificam dados criticamente

### Inputs
- Classes: `w-full px-3 py-2 bg-gray-800 border border-gray-700 rounded-lg text-gray-100 focus:outline-none focus:ring-2 focus:ring-indigo-500`

### Forms
- **Contêiner**: `max-w-2xl mx-auto p-6 bg-gray-800 rounded-xl shadow-lg`
- **Espaçamento**: `space-y-4`

### Grids
- **Dashboard**: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`
- **Tabelas**: `w-full text-left border-collapse`
  - Cabeçalho: `text-gray-400 uppercase text-sm`
  - Linhas: `border-t border-gray-700 py-3`

### Menu/Navbar
- Fixo no topo (mobile: collapsible)
- Fundo: `bg-gray-900/90 backdrop-blur`
- Itens: `text-gray-300 hover:text-white`

## Padrões de Layout

### Dashboard
- Layout em grid responsivo
- Cards com informações resumidas
- Histórico recente de transações
- Indicadores financeiros principais

### Páginas de Formulário
- Formulários centralizados em containers máximos
- Espaçamento consistente entre campos
- Botões de ação alinhados à direita

### Listagens
- Tabelas com cabeçalhos claros
- Paginação quando necessário
- Filtros acessíveis

## Estilo Escuro

O tema escuro foi escolhido para proporcionar uma experiência visual agradável e reduzir cansaço ocular em ambientes com pouca luz. As cores foram selecionadas para garantir boa legibilidade e contraste adequado.