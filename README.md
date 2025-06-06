Cursor-tools + Memory bank

## Установка

1. Загрузите все файлы и папки в корень проекта. Если проектов в воркспейсе несколько, то папку .cursor переносим в корень воркспейса.
2. Заполните значения в файле integration_config.md.
3. Обновите инструкции для агетов в custom modes (VAN,PLAN...) из папки custom_modes(ее можно удалить потом).
3. (НЕОБЯЗАТЕЛЬНО) Используйте chat-summary\run.py для создания самари по вашим чатам в спекстори для более удобного поиска информации в будущем.
4. (НЕОБЯЗАТЕЛЬНО) Изпользуйте devops-tools для оптимизации заливки и отладки пайплайнов.

### Установка пользовательских режимов

1. Откройте Cursor и нажмите на селектор режимов в панели чата
2. Выберите "Add custom mode" (Добавить пользовательский режим)
3. В экране конфигурации:
   - Введите название режима (можете включить эмодзи иконки как 🔍, 📋, 🎨, ⚒️, скопировав их в начало названия)
   - Выберите иконку из ограниченных предустановленных опций Cursor
   - Добавьте горячую клавишу (опционально)
   - Отметьте необходимые инструменты
   - Нажмите на **Расширенные настройки**
   - В пустом текстовом поле, которое появится внизу, вставьте содержимое пользовательской инструкции из соответствующего файла

#### Конфигурация режимов

Для каждого режима настройте следующим образом:

1. **VAN РЕЖИМ** (Инициализация)
   - **Название**: 🔍 VAN
   - **Инструменты**: Включите "Codebase Search", "Read File", "Terminal", "List Directory"
   - **Расширенные настройки**: Вставьте из `custom_modes/van_instructions.md`

2. **PLAN РЕЖИМ** (Планирование задач)
   - **Название**: 📋 PLAN
   - **Инструменты**: Включите "Codebase Search", "Read File", "Terminal", "List Directory"
   - **Расширенные настройки**: Вставьте из `custom_modes/plan_instructions.md`

3. **CREATIVE РЕЖИМ** (Дизайнерские решения)
   - **Название**: 🎨 CREATIVE
   - **Инструменты**: Включите "Codebase Search", "Read File", "Terminal", "List Directory", "Edit File"
   - **Расширенные настройки**: Вставьте из `custom_modes/creative_instructions.md`

4. **IMPLEMENT РЕЖИМ** (Реализация кода)
   - **Название**: ⚒️ IMPLEMENT
   - **Инструменты**: Включите все инструменты
   - **Расширенные настройки**: Вставьте из `custom_modes/implement_instructions.md`

5. **REFLECT РЕЖИМ** (Обзор)
   - **Название**: 🔍 REFLECT
   - **Инструменты**: Включите "Codebase Search", "Read File", "Terminal", "List Directory"
   - **Расширенные настройки**: Вставьте из `custom_modes/reflect_archive_instructions.md` (секция REFLECT)
   
6. **ARCHIVE РЕЖИМ** (Документация)
   - **Название**: 📚 ARCHIVE
   - **Инструменты**: Включите "Codebase Search", "Read File", "Terminal", "List Directory", "Edit File"
   - **Расширенные настройки**: Вставьте из `custom_modes/reflect_archive_instructions.md` (секция ARCHIVE)

> **Примечание**: Инструкции REFLECT и ARCHIVE объединены в одном файле для оптимизации под ограничения символов Cursor при сохранении функциональности.

### Функциональность QA

QA не является отдельным пользовательским режимом, а представляет собой набор функций валидации, которые можно вызывать из любого режима. Вы можете использовать возможности QA, набрав "QA" в любом режиме, когда нужно выполнить техническую валидацию. Этот подход обеспечивает гибкость для проведения проверок в любой момент процесса разработки.

## Базовое использование

1. **Начните с VAN режима**:
   - Переключитесь на VAN режим в Cursor
   - Наберите "VAN" для запуска процесса инициализации
   - VAN проанализирует структуру вашего проекта и определит сложность

2. **Следуйте рабочему процессу в зависимости от сложности**:
   - **Задачи уровня 1**: Могут переходить напрямую к IMPLEMENT после VAN
   - **Задачи уровня 2**: Упрощенный рабочий процесс (VAN → PLAN → IMPLEMENT → REFLECT)
   - **Задачи уровня 3-4**: Полный рабочий процесс (VAN → PLAN → CREATIVE → IMPLEMENT → REFLECT → ARCHIVE)
   - **В любой момент**: Наберите "QA" для выполнения технической валидации

3. **Команды для конкретных режимов**:
   ```
   VAN - Инициализация проекта и определение сложности
   PLAN - Создание детального плана реализации
   CREATIVE - Исследование вариантов дизайна для сложных компонентов
   IMPLEMENT - Систематическая сборка запланированных компонентов
   REFLECT - Обзор и документирование извлеченных уроков
   ARCHIVE - Создание исчерпывающей документации
   QA - Валидация технической реализации (можно вызывать из любого режима)
   ```

## Основные файлы и их назначение

- **tasks.md**: Центральный источник истины для отслеживания задач. Его формат, принципы ведения и синхронизации с Jira определяются правилом `.cursor/rules/isolation_rules/Core/task-management.mdc`.
- **activeContext.md**: Поддерживает фокус текущей фазы разработки
- **progress.md**: Отслеживает статус реализации
- **creative-*.md**: Документы дизайнерских решений, созданные в CREATIVE режиме
- **reflect-*.md**: Документы обзора, созданные в REFLECT режиме

## Конфигурация интеграций

Memory Bank v0.7-beta включает централизованную систему настройки интеграций через файл `integration_config.md`. Этот файл позволяет настроить подключения к различным сервисам и инструментам.

### Настройка integration_config.md

1. **Откройте файл** `integration_config.md` в корне проекта
2. **Найдите секцию "Ваши контексты"** и замените примеры на реальные данные:

```yaml
- context_name: "Мой Проект"
  description: "Описание вашего проекта"
  jira_project_key: "PROJ"
  jira_default_issue_type: "Story"
  confluence_space_key: "PROJDOCS"
  gitlab_project_id: "123456"
  vercel_project_id: "prj_abc123"
  deepseek_api_key: "sk-ваш-ключ-здесь"
  deepseek_model: "deepseek-chat"
```

3. **Настройте маппинг статусов** под ваш рабочий процесс в Jira:
```yaml
jira_status_mapping:
  PLAN: "Backlog"
  IMPLEMENT_START: "In Progress"
  IMPLEMENT_COMPLETE: "Done"
  ARCHIVE: "Closed"
```

### Поддерживаемые интеграции

- **Jira**: Автоматическое создание и обновление задач
- **Confluence**: Публикация документации
- **GitLab**: Управление репозиториями и CI/CD
- **Vercel**: Деплой и мониторинг
- **DeepSeek AI**: ИИ-ассистент для разработки

### Как работает система

1. **ИИ автоматически читает** настройки из `integration_config.md`
2. **При работе с интеграциями** ИИ спросит, какой контекст проекта использовать
3. **Локальный файл tasks.md** автоматически синхронизируется с внешними системами
4. **Story Points и оценки** автоматически передаются в Jira

## Интеграция с DeepSeek AI

Memory Bank v0.7-beta включает автоматическую интеграцию с моделями DeepSeek AI. Когда вы упоминаете "дипсик" или "deepseek" в любом режиме, система автоматически:

1. **Читает конфигурацию** из `integration_config.md`
2. **Выбирает подходящую модель** в зависимости от типа задачи:
   - `deepseek-coder` для генерации кода и отладки
   - `deepseek-chat` для планирования и документации  
   - `deepseek-reasoner` для решения сложных проблем
3. **Использует ваши API учетные данные** безопасно из конфигурации

### Примеры использования

```
"Давай сделаем это через дипсик"
"Используй дипсик для написания кода"
"С помощью дипсика проанализируй архитектуру"
```

ИИ автоматически покажет, какая модель DeepSeek используется, и обработает всю конфигурацию API.
