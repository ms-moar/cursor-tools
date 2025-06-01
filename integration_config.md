--- 
description: "Central configuration for multi-project context, integrations (Jira, GitLab, Confluence, DeepSeek), and tool settings. The structure and usage of this file are governed by the .cursor/rules/isolation_rules/Core/multi-context-system.mdc rule."
globs: ["integration_config.md"]
alwaysApply: false
---

# Integration & Project Context Configuration

> **IMPORTANT**: The structure, available fields, and logic for interpreting this configuration are defined in detail in the `.cursor/rules/isolation_rules/Core/multi-context-system.mdc` rule. Refer to it for comprehensive guidance on how to define and use project contexts and their specific settings.

# Integration Configuration for Memory Bank System

## Project Contexts

**Для ИИ:** При активации режима, который взаимодействует с Jira, Confluence или GitLab, сначала спросите пользователя, какой `activeProjectContext` использовать.

## Контекст 1

```yaml
- context_name: "Cursor Memory Bank"
  description: "Система управления памятью для Cursor IDE"
  jira_project_key: "CMB"
  jira_default_issue_type: "Story"
  jira_component: "NO_NAME"
  jira_status_mapping:
    PLAN: "Backlog"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "CMBDOCS"
  gitlab_project_id: "cursor_memory_bank"
  gitlab_default_branch: "main"
  deepseek_api_key: "ваш_реальный_ключ_здесь"
  deepseek_model: "deepseek-reasoner"
  jira_login: "ВАШ_JIRA_ЛОГИН"
```

## Контекст 2

```yaml
- context_name: "Второй проект"
  description: "Описание второго проекта"
  jira_project_key: "PROJ2"
  jira_default_issue_type: "Story"
  jira_component: "NO_NAME"
  jira_status_mapping:
    PLAN: "Backlog"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "PROJ2DOCS"
  gitlab_project_id: "second_project"
  gitlab_default_branch: "main"
  deepseek_api_key: "ваш_второй_ключ_здесь"
  deepseek_model: "deepseek-reasoner"
  jira_login: "ВАШ_JIRA_ЛОГИН"
```

## DeepSeek AI Integration

### Модели
- `deepseek-chat`: Общение и анализ
- `deepseek-coder`: Программирование
- `deepseek-reasoner`: Сложные задачи

### Для ИИ
- Автоматически читать API ключ из активного контекста проекта
- Выбирать модель в зависимости от типа задачи
- При ошибках API сообщать пользователю

## Global Settings

### Local Task Management (`tasks.md`)
- **Цель**: Локальный файл для отслеживания задач
- **Формат**: `- [ ] **[PROJECT:ID]** Название - *Описание* - SP=[X] (Context: Name)`
- **Управление**: ИИ создает и обновляет файл автоматически

### Task Assignment Rules
- Перед взятием чужой задачи в Jira - подтверждение у пользователя
- При смене исполнителя - предложить обновить Jira

### Task Estimation (Story Points)
- ИИ предоставляет финальную оценку SP в режиме `PLAN`
- Формат в Jira: `SP_VALUE=[X]` в описании задачи
- Для малых эпиков (< 7 SP): подзадачи в описании, не отдельными issues

## Setup Instructions

1. Заполните секцию "Ваши контексты" реальными данными
2. Настройте `jira_status_mapping` под ваш workflow
3. ИИ будет автоматически управлять `tasks.md`
4. При работе с интеграциями ИИ спросит активный контекст проекта

### Логика работы

#### Автоматические метки
- При создании задач AI: метка `created-by-ai` + текст "Примечание: Задача создана с помощью ИИ."
- При редактировании AI: метка `edited-by-ai` + текст "Примечание: Задача отредактирована с помощью ИИ."

#### Валидация задач

Если задача не имеет AI-меток:
1. Анализ содержимого задачи
2. Представление интерпретации пользователю (специализированной по режиму)
3. Получение подтверждения или уточнений
4. Обновление описания при необходимости
5. Оценка Story Points
6. Добавление соответствующих меток

## Automatic Component Assignment Integration

### Обзор изменений
Добавлена автоматическая установка компонента Jira для всех операций с задачами.

### Логика работы

#### Источник компонента
- Читается из `activeProjectContext.jira_component` в `integration_config.md`
- Если значение НЕ равно "NO_NAME", компонент автоматически устанавливается

#### Применение
- **Создание задач**: Все вызовы `mcp_mcp-atlassian_jira_create_issue` включают параметр `components`
- **Обновление задач**: Все вызовы `mcp_mcp-atlassian_jira_update_issue` включают параметр `components`
- **Область действия**: Эпики, задачи, все типы Jira issues

#### Измененные файлы
1. **`main-optimized.mdc`** - добавлен раздел "AUTOMATIC COMPONENT ASSIGNMENT"
2. **`plan-mode-map.mdc`** - логика компонента в создании эпиков и задач
3. **`implement-mode-map.mdc`** - логика компонента в обновлении задач
4. **`creative-mode-map.mdc`** - логика компонента в обновлении задач
5. **`van-mode-map.mdc`** - логика компонента в валидации задач

#### Условная логика
```
Let jiraComponent = activeProjectContext.jira_component
Let shouldSetComponent = (jiraComponent != "NO_NAME")

If shouldSetComponent:
    Call API with components [jiraComponent]
Else:
    Call API without components parameter
```

### Преимущества
- Автоматическая категоризация задач по компонентам
- Единообразная настройка через конфигурацию
- Гибкость: можно отключить установкой "NO_NAME"
- Применяется ко всем операциям с Jira без исключений

### Настройка
Для активации установки компонента измените `jira_component` в нужном контексте проекта с "NO_NAME" на название реального компонента в вашем Jira проекте.