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
- context_name: "Cursor Memory Bank"
  description: "Система управления памятью для Cursor IDE"
  jira_project_key: "CMB"
  jira_default_issue_type: "Story"
  jira_status_mapping:
    PLAN: "Backlog"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "CMBDOCS"
  gitlab_project_id: "cursor_memory_bank"
  gitlab_default_branch: "main"
  vercel_project_id: "cursor_memory_bank"
  deepseek_api_key: "ваш_реальный_ключ_здесь"
  deepseek_model: "deepseek-chat"
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

## AI Task Management Integration

### Обзор изменений
Интегрирована логика управления AI-метками и валидации задач прямо в существующие правила Cursor.

### Измененные файлы

1. **`main-optimized.mdc`**
   - Добавлен раздел "AI TRANSPARENCY AND VALIDATION"
   - Краткое описание интегрированной функциональности

2. **`van-mode-map.mdc`**
   - Step 2.1: AI Task Validation
   - Полная логика валидации задач без AI-меток

3. **`creative-mode-map.mdc`**
   - Step 4.1: AI Task Validation
   - Специализированная валидация для дизайн-задач

4. **`implement-mode-map.mdc`**
   - Step 4.1: AI Task Validation
   - Специализированная валидация для технических задач

5. **`plan-mode-map.mdc`**
   - Обновлены вызовы создания задач с метками `created-by-ai`
   - Синхронизация меток и текстовых примечаний

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

#### Специализация по режимам
- **VAN**: Общая валидация с определением сложности
- **CREATIVE**: Фокус на дизайн-требованиях
- **IMPLEMENT**: Фокус на технических требованиях

### Преимущества интеграции
- Нет новых файлов правил
- Логика встроена в существующие процессы
- Контекстно-зависимая валидация
- Полная прозрачность работы AI
- Автоматическая синхронизация меток и описаний 