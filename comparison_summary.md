# Сравнение файлов правил изоляции

В этом документе представлено сравнение файлов между директориями `.cursor1/rules/isolation_rules` (оригинальная версия) и `.cursor/rules/isolation_rules` (измененная версия).

## Файлы с различиями:

### 1. `main.mdc`

**Разница**: В измененной версии (`.cursor`) добавлены 2 новые секции.

**Логика**: Улучшение протокола коммуникации с ИИ и добавление обязательных правил безопасности при работе с файлами.

**Добавленный код:**
```markdown
## 🗣️ AI COMMUNICATION PROTOCOL

**Instruction for AI:** You **MUST** start every message to the user with the following line, replacing `[Current Working Directory]` with the actual current working directory relative to the project root, or the absolute path if outside the project root:

`**📂 Проект: cursor-memory-bank | Папка: [Current Working Directory]**`

This ensures clarity about the context of your operations at all times.

## 🔒 MANDATORY SECURITY RULES

When working with files in the project, the following rules **MUST** be observed by the AI:

1.  **Backup Before Deletion**: Before deleting any file for any reason, its backup copy **MUST** be created in the `backup-files/` folder.
2.  **Create Backup Directory**: If the `backup-files/` directory is missing, it **MUST** be created automatically by the AI before attempting to save a backup.
3.  **Backup File Naming**: The backup file name format **MUST** be: `{original_filename}_{timestamp}.bak`. The timestamp should be in `YYYYMMDDHHMMSS` format (e.g., `myfile.txt_20240515103000.bak`).

These rules are critical for data safety and project integrity.
```

---

### 2. `main-optimized.mdc`

**Разница**: В измененной версии (`.cursor`) добавлены 4 новые секции.

**Логика**: Улучшение прозрачности и валидации ИИ, автоматическое назначение компонентов Jira, улучшение протокола коммуникации с ИИ и добавление обязательных правил безопасности.

**Добавленный код:**
```markdown
## 🤖 AI TRANSPARENCY AND VALIDATION

All modes now include integrated AI task validation:
- **AI Labels**: `created-by-ai`, `edited-by-ai` automatically applied
- **Task Validation**: Automatic interpretation and user confirmation for unlabeled tasks
- **Context-Aware**: Each mode presents specialized validation (design, implementation, etc.)
- **Story Points**: Estimation included in validation process

## 🏗️ AUTOMATIC COMPONENT ASSIGNMENT

All Jira operations automatically include component assignment:
- **Component Source**: Read from `activeProjectContext.jira_component` in `integration_config.md`
- **Auto-Assignment**: If component is NOT "NO_NAME", automatically set component in all Jira create/update operations
- **Scope**: Applies to task creation, task updates, Epic creation, and all Jira modifications
- **Validation**: Component existence verified before assignment

## 🗣️ AI COMMUNICATION PROTOCOL

**Instruction for AI:** You **MUST** start every message to the user with the following line, replacing `[Current Working Directory]` with the actual current working directory relative to the project root, or the absolute path if outside the project root:

`**📂 Проект: cursor-memory-bank | Папка: [Current Working Directory]**`

This ensures clarity about the context of your operations at all times.

## 🔒 MANDATORY SECURITY RULES

When working with files in the project, the following rules **MUST** be observed by the AI:

1.  **Backup Before Deletion**: Before deleting any file for any reason, its backup copy **MUST** be created in the `backup-files/` folder.
2.  **Create Backup Directory**: If the `backup-files/` directory is missing, it **MUST** be created automatically by the AI before attempting to save a backup.
3.  **Backup File Naming**: The backup file name format **MUST** be: `{original_filename}_{timestamp}.bak`. The timestamp should be in `YYYYMMDDHHMMSS` format (e.g., `myfile.txt_20240515103000.bak`).

These rules are critical for data safety and project integrity.
```

---

### 3. `Core/optimization-integration.mdc`

**Разница**: В измененной версии (`.cursor`) в секции "OPTIMIZATION COMPONENT REGISTRY" добавлена новая запись для `deepseekIntegration` и изменены некоторые строки в секции "OPTIMIZATION METRICS".

**Логика**: Добавлена интеграция с DeepSeek и обновлены метрики оптимизации.

**Измененный код (секция `OPTIMIZATION COMPONENT REGISTRY`):**
```javascript
// Optimization component registry pseudocode
const optimizationRegistry = {
  // Core optimizations
  hierarchicalRuleLoading: {
    file: "Core/hierarchical-rule-loading.mdc",
    dependencies: [],
    priority: 1
  },
  adaptiveComplexityModel: {
    file: "main-optimized.mdc",
    dependencies: ["hierarchicalRuleLoading"],
    priority: 2
  },
  modeTransitionOptimization: {
    file: "Core/mode-transition-optimization.mdc",
    dependencies: ["hierarchicalRuleLoading", "adaptiveComplexityModel"],
    priority: 3
  },
  
  // Level-specific optimizations
  level1Optimization: {
    file: "Level1/optimized-workflow-level1.mdc",
    dependencies: ["adaptiveComplexityModel"],
    priority: 4
  },
  
  // Feature-specific optimizations
  creativePhaseOptimization: {
    file: "Phases/CreativePhase/optimized-creative-template.mdc",
    dependencies: ["hierarchicalRuleLoading", "adaptiveComplexityModel"],
    priority: 5
  },
  
  // Integration optimizations
  deepseekIntegration: {
    file: "Core/deepseek-integration.mdc",
    dependencies: ["hierarchicalRuleLoading"],
    priority: 6,
    triggers: ["дипсик", "deepseek", "используй дипсик", "через дипсик", "с помощью дипсика"]
  }
};
```

**Измененный код (секция `OPTIMIZATION METRICS`):**
```markdown
# Optimization Metrics

## Token Usage
- Core Rule Loading: [X] tokens
- Mode-Specific Rules: [Y] tokens
- Creative Phase Documentation: [Z] tokens
- Overall Token Reduction: [P]%

## Context Efficiency
- Context Utilization: [Q]%
- Context Waste: [R]%
- Effective Token Capacity: [S] tokens

## Rule Loading
- Rules Loaded: [T] / [U] (Total)
- Lazy-Loaded Rules: [V]
- Cached Rules: [W]

## Documentation
- Level 1 Documentation Size: [X] tokens
- Level 2 Documentation Size: [Y] tokens
- Level 3 Documentation Size: [Z] tokens
- Level 4 Documentation Size: [AA] tokens
```

---

### 4. `Level4/archive-comprehensive.mdc`

**Разница**: В измененной версии (`.cursor`) удалена секция "Key Files and Components Affected (from tasks.md)" (4 строки) из раздела "Implementation Documentation".

**Логика**: Упрощение шаблона архивирования, делая его более универсальным.

**Удаленный код (из `.cursor1/.../archive-comprehensive.mdc`):**
```markdown
### Key Files and Components Affected (from tasks.md)
[Summary or direct copy of file/component checklists from the original tasks.md for this project. This provides a quick reference to the scope of changes at a component/file level.]

```

---

## Файлы только в одной версии:

-   **`.cursor1/rules/isolation_rules/Core/memory-bank-paths.mdc`** (только в оригинальной версии)
-   **`.cursor/rules/isolation_rules/Core/deepseek-integration.mdc`** (только в измененной версии, пропущен по вашему запросу)

## Все остальные файлы идентичны.

Полный список идентичных файлов:

**Core:**
- `command-execution.mdc`
- `complexity-decision-tree.mdc`
- `creative-phase-enforcement.mdc`
- `creative-phase-metrics.mdc`
- `file-verification.mdc`
- `hierarchical-rule-loading.mdc`
- `mode-transition-optimization.mdc`
- `platform-awareness.mdc`

**Level1:**
- `optimized-workflow-level1.mdc`
- `quick-documentation.mdc`
- `workflow-level1.mdc`

**Level2:**
- `archive-basic.mdc`
- `reflection-basic.mdc`
- `task-tracking-basic.mdc`
- `workflow-level2.mdc`

**Level3:**
- `planning-comprehensive.mdc`
- `task-tracking-intermediate.mdc`

**Level4:**
- `architectural-planning.mdc`
- `phased-implementation.mdc`
- `reflection-comprehensive.mdc`
- `task-tracking-advanced.mdc`
- `workflow-level4.mdc`