# Integration Configuration for Memory Bank System

Централизованные настройки интеграций для системы Memory Bank.

## Project Contexts

Определите контексты ваших проектов. Каждый контекст может иметь свои ключи и URL для различных сервисов.

**Для ИИ:** При активации режима, который взаимодействует с Jira, Confluence, GitLab или Vercel, сначала спросите пользователя, какой `activeProjectContext` использовать.

**Пример структуры:**

```yaml
- context_name: "My Project"
  description: "Описание проекта"
  jira_project_key: "PROJ"
  jira_default_issue_type: "Story"
  jira_status_mapping:
    PLAN: "Backlog"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "PROJDOCS"
  gitlab_project_id: "your_gitlab_project_id"
  gitlab_default_branch: "main"
  vercel_project_id: "your_vercel_project_id"
  deepseek_api_key: "your_deepseek_api_key"
  deepseek_model: "deepseek-chat"
```

**Ваши контексты:**

```yaml
- context_name: "YOUR_PROJECT_NAME"
  description: "Описание вашего проекта"
  jira_project_key: "YOUR_KEY"
  jira_default_issue_type: "Story"
  jira_status_mapping:
    PLAN: "Backlog"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "YOUR_SPACE"
  gitlab_project_id: "YOUR_GITLAB_ID"
  gitlab_default_branch: "main"
  vercel_project_id: "YOUR_VERCEL_ID"
  deepseek_api_key: "YOUR_DEEPSEEK_KEY"
  deepseek_model: "deepseek-chat"
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