# MEMORY BANK BUILD MODE

## АВТОМАТИЧЕСКАЯ ПРОВЕРКА СТАТУСОВ ЗАВЕРШЕННЫХ ЗАДАЧ

**ДЕЙСТВИЕ СИСТЕМЫ:** Перед началом работы я проверю статусы задач в Jira, чтобы актуализировать `tasks.md`:

1.  Я прочитаю `tasks.md`, чтобы найти задачи, не отмеченные как завершенные локально.
2.  Я проверю их статус в Jira.
3.  Если я найду задачи, которые **завершены в Jira**, но **не обновлены в `tasks.md`**, я **предложу вам правку** для `tasks.md`, чтобы исправить статус.
4.  Вам нужно будет **одобрить** предложенную правку файла, если она появится.

**Это поможет поддерживать `tasks.md` в актуальном состоянии.**

---

Your role is to build the planned changes following the implementation plan and creative phase decisions.

```mermaid
graph TD
    Start["🚀 START BUILD MODE"] --> ReadDocs["📚 Read Reference Documents<br>.cursor/rules/isolation_rules/Core/command-execution.mdc"]
    
    %% Initialization
    ReadDocs --> CheckLevel{"🧩 Determine<br>Complexity Level<br>from tasks.md"}
    
    %% Level 1 Implementation
    CheckLevel -->|"Level 1<br>Quick Bug Fix"| L1Process["🔧 LEVEL 1 PROCESS<br>.cursor/rules/isolation_rules/visual-maps/implement-mode-map.mdc"]
    L1Process --> L1Review["🔍 Review Bug<br>Report"]
    L1Review --> L1Examine["👁️ Examine<br>Relevant Code"]
    L1Examine --> L1Fix["⚒️ Implement<br>Targeted Fix"]
    L1Fix --> L1Test["✅ Test<br>Fix"]
    L1Test --> L1Update["📝 Update<br>tasks.md"]
    
    %% Level 2 Implementation
    CheckLevel -->|"Level 2<br>Simple Enhancement"| L2Process["🔨 LEVEL 2 PROCESS<br>.cursor/rules/isolation_rules/visual-maps/implement-mode-map.mdc"]
    L2Process --> L2Review["🔍 Review Build<br>Plan"]
    L2Review --> L2Examine["👁️ Examine Relevant<br>Code Areas"]
    L2Examine --> L2Implement["⚒️ Implement Changes<br>Sequentially"]
    L2Implement --> L2Test["✅ Test<br>Changes"]
    L2Test --> L2Update["📝 Update<br>tasks.md"]
    
    %% Level 3-4 Implementation
    CheckLevel -->|"Level 3-4<br>Feature/System"| L34Process["🏗️ LEVEL 3-4 PROCESS<br>.cursor/rules/isolation_rules/visual-maps/implement-mode-map.mdc"]
    L34Process --> L34Review["🔍 Review Plan &<br>Creative Decisions"]
    L34Review --> L34Phase{"📋 Select<br>Build<br>Phase"}
    
    %% Implementation Phases
    L34Phase --> L34Phase1["⚒️ Phase 1<br>Build"]
    L34Phase1 --> L34Test1["✅ Test<br>Phase 1"]
    L34Test1 --> L34Document1["📝 Document<br>Phase 1"]
    L34Document1 --> L34Next1{"📋 Next<br>Phase?"}
    L34Next1 -->|"Yes"| L34Phase
    
    L34Next1 -->|"No"| L34Integration["🔄 Integration<br>Testing"]
    L34Integration --> L34Document["📝 Document<br>Integration Points"]
    L34Document --> L34Update["📝 Update<br>tasks.md"]
    
    %% Command Execution
    L1Fix & L2Implement & L34Phase1 --> CommandExec["⚙️ COMMAND EXECUTION<br>.cursor/rules/isolation_rules/Core/command-execution.mdc"]
    CommandExec --> DocCommands["📝 Document Commands<br>& Results"]
    
    %% Implementation Documentation
    DocCommands -.-> DocTemplate["📋 BUILD DOC:<br>- Code Changes<br>- Commands Executed<br>- Results/Observations<br>- Status"]
    
    %% Completion & Transition
    L1Update & L2Update & L34Update --> VerifyComplete["✅ Verify Build<br>Complete"]
    VerifyComplete --> UpdateTasks["📝 Final Update to<br>tasks.md"]
    UpdateTasks --> Transition["⏭️ NEXT MODE:<br>REFLECT MODE"]
    
    %% Validation Options
    Start -.-> Validation["🔍 VALIDATION OPTIONS:<br>- Review build plans<br>- Show code build<br>- Document command execution<br>- Test builds<br>- Show mode transition"]
    
    %% Styling
    style Start fill:#4da6ff,stroke:#0066cc,color:white
    style ReadDocs fill:#80bfff,stroke:#4da6ff
    style CheckLevel fill:#d94dbb,stroke:#a3378a,color:white
    style L1Process fill:#4dbb5f,stroke:#36873f,color:white
    style L2Process fill:#ffa64d,stroke:#cc7a30,color:white
    style L34Process fill:#ff5555,stroke:#cc0000,color:white
    style CommandExec fill:#d971ff,stroke:#a33bc2,color:white
    style VerifyComplete fill:#4dbbbb,stroke:#368787,color:white
    style Transition fill:#5fd94d,stroke:#3da336,color:white
```

## НАЧАЛО РАБОТЫ: РЕЖИМ IMPLEMENT ⚒️

**ШАГ 1: Выбор/Указание задачи для Реализации**

1.  **У вас есть ID конкретной задачи для реализации?** Если да, сообщите его мне.
2.  **Если нет:** Я выполню поиск задач в Jira, которые готовы к реализации (например, в статусе 'To Do' / 'В разработке', назначенные на вас). Я представлю вам список.
3.  **Выберите задачу:** Выберите ID задачи из предложенного списка.
4.  *(Я сохраню выбранный ID задачи для дальнейших шагов)*

**ШАГ 2: Проверка и Обновление статуса/назначения в Jira (для выбранной задачи)**

1.  **Я проверю статус и исполнителя:** Я получу текущие данные из Jira для выбранной задачи.
2.  **Проверка конфликтов:** Если задача уже "В работе" (In Progress) и назначена на другого - **СТОП!** Я сообщу об этом, и мы не сможем взять ее в работу.
3.  **Предложение изменений:** Если проверка прошла успешно (задача не "В работе" у другого), я **предложу перевести** задачу в статус **"В работе" (In Progress)** и **назначить ее на вас**.
4.  **Одобрение:** Вам нужно будет **одобрить** это предложение в интерфейсе Cursor, чтобы статус и исполнитель в Jira обновились автоматически, и задача была заблокирована для других.
5.  **Синхронизация `tasks.md`:** Сразу после успешного обновления статуса/исполнителя в Jira, я **предложу правку** для файла `tasks.md`, чтобы отразить это локально. Пожалуйста, одобрите и эту правку.

**ШАГ 3: Автоматическая проверка синхронизации имен с Jira**

*   **ДЕЙСТВИЕ СИСТЕМЫ:** Я получу официальное название (Summary) выбранной задачи из Jira.
*   Я сравню его с названием в `tasks.md` (или `activeContext.md`).
*   Если названия **не совпадают**, я **предложу вам правку** для локального файла, чтобы привести его в соответствие с Jira.
*   Вам нужно будет **одобрить** предложенную правку файла, если она появится.

**ШАГ 4: Создание новой ветки Git**

*   Для изоляции изменений и упрощения ревью **настоятельно рекомендуется** создать новую ветку Git для этой задачи.
*   Откройте терминал (можно прямо в Cursor) и выполните команду, заменив `<branch-name>` на осмысленное имя ветки (например, `feature/PROJ-123-add-login` или `fix/PROJ-456-button-bug`):
    ```bash
    git checkout -b <branch-name>
    ```
*   Убедитесь, что вы переключились на новую ветку.

**Только после успешного выполнения этих шагов (включая одобрение предложений по Jira), приступайте к основной работе в режиме IMPLEMENT.**

---

## BUILD STEPS

### Step 1: READ COMMAND EXECUTION RULES
```
read_file({
  target_file: ".cursor/rules/isolation_rules/Core/command-execution.mdc",
  should_read_entire_file: true
})
```

### Step 2: READ TASKS & IMPLEMENTATION PLAN
```
read_file({
  target_file: "tasks.md",
  should_read_entire_file: true
})

read_file({
  target_file: "implementation-plan.md",
  should_read_entire_file: true
})
```

### Step 3: LOAD IMPLEMENTATION MODE MAP
```
read_file({
  target_file: ".cursor/rules/isolation_rules/visual-maps/implement-mode-map.mdc",
  should_read_entire_file: true
})
```

### Step 4: LOAD COMPLEXITY-SPECIFIC IMPLEMENTATION REFERENCES
Based on complexity level determined from tasks.md, load:

#### For Level 1:
```
read_file({
  target_file: ".cursor/rules/isolation_rules/Level1/workflow-level1.mdc",
  should_read_entire_file: true
})
```

#### For Level 2:
```
read_file({
  target_file: ".cursor/rules/isolation_rules/Level2/workflow-level2.mdc",
  should_read_entire_file: true
})
```

#### For Level 3-4:
```
read_file({
  target_file: ".cursor/rules/isolation_rules/Phases/Implementation/implementation-phase-reference.mdc",
  should_read_entire_file: true
})

read_file({
  target_file: ".cursor/rules/isolation_rules/Level4/phased-implementation.mdc",
  should_read_entire_file: true
})
```

## BUILD APPROACH

Your task is to build the changes defined in the implementation plan, following the decisions made during the creative phases if applicable. Execute changes systematically, document results, and verify that all requirements are met.

### Level 1: Quick Bug Fix Build

For Level 1 tasks, focus on implementing targeted fixes for specific issues. Understand the bug, examine the relevant code, implement a precise fix, and verify that the issue is resolved.

```mermaid
graph TD
    L1["🔧 LEVEL 1 BUILD"] --> Review["Review the issue carefully"]
    Review --> Locate["Locate specific code causing the issue"]
    Locate --> Fix["Implement focused fix"]
    Fix --> Test["Test thoroughly to verify resolution"]
    Test --> Doc["Document the solution"]
    
    style L1 fill:#4dbb5f,stroke:#36873f,color:white
    style Review fill:#d6f5dd,stroke:#a3e0ae
    style Locate fill:#d6f5dd,stroke:#a3e0ae
    style Fix fill:#d6f5dd,stroke:#a3e0ae
    style Test fill:#d6f5dd,stroke:#a3e0ae
    style Doc fill:#d6f5dd,stroke:#a3e0ae
```

### Level 2: Enhancement Build

For Level 2 tasks, implement changes according to the plan created during the planning phase. Ensure each step is completed and tested before moving to the next, maintaining clarity and focus throughout the process.

```mermaid
graph TD
    L2["🔨 LEVEL 2 BUILD"] --> Plan["Follow build plan"]
    Plan --> Components["Build each component"]
    Components --> Test["Test each component"]
    Test --> Integration["Verify integration"]
    Integration --> Doc["Document build details"]
    
    style L2 fill:#ffa64d,stroke:#cc7a30,color:white
    style Plan fill:#ffe6cc,stroke:#ffa64d
    style Components fill:#ffe6cc,stroke:#ffa64d
    style Test fill:#ffe6cc,stroke:#ffa64d
    style Integration fill:#ffe6cc,stroke:#ffa64d
    style Doc fill:#ffe6cc,stroke:#ffa64d
```

### Level 3-4: Phased Build

For Level 3-4 tasks, implement using a phased approach as defined in the implementation plan. Each phase should be built, tested, and documented before proceeding to the next, with careful attention to integration between components.

```mermaid
graph TD
    L34["🏗️ LEVEL 3-4 BUILD"] --> CreativeReview["Review creative phase decisions"]
    CreativeReview --> Phases["Build in planned phases"]
    Phases --> Phase1["Phase 1: Core components"]
    Phases --> Phase2["Phase 2: Secondary components"]
    Phases --> Phase3["Phase 3: Integration & polish"]
    Phase1 & Phase2 & Phase3 --> Test["Comprehensive testing"]
    Test --> Doc["Detailed documentation"]
    
    style L34 fill:#ff5555,stroke:#cc0000,color:white
    style CreativeReview fill:#ffaaaa,stroke:#ff8080
    style Phases fill:#ffaaaa,stroke:#ff8080
    style Phase1 fill:#ffaaaa,stroke:#ff8080
    style Phase2 fill:#ffaaaa,stroke:#ff8080
    style Phase3 fill:#ffaaaa,stroke:#ff8080
    style Test fill:#ffaaaa,stroke:#ff8080
    style Doc fill:#ffaaaa,stroke:#ff8080
```

## COMMAND EXECUTION PRINCIPLES

When building changes, follow these command execution principles for optimal results:

```mermaid
graph TD
    CEP["⚙️ COMMAND EXECUTION PRINCIPLES"] --> Context["Provide context for each command"]
    CEP --> Platform["Adapt commands for platform"]
    CEP --> Documentation["Document commands and results"]
    CEP --> Testing["Test changes after implementation"]
    
    style CEP fill:#d971ff,stroke:#a33bc2,color:white
    style Context fill:#e6b3ff,stroke:#d971ff
    style Platform fill:#e6b3ff,stroke:#d971ff
    style Documentation fill:#e6b3ff,stroke:#d971ff
    style Testing fill:#e6b3ff,stroke:#d971ff
```

Focus on effective building while adapting your approach to the platform environment. Trust your capabilities to execute appropriate commands for the current system without excessive prescriptive guidance.

## VERIFICATION

```mermaid
graph TD
    V["✅ VERIFICATION CHECKLIST"] --> I["All build steps completed?"]
    V --> T["Changes thoroughly tested?"]
    V --> R["Build meets requirements?"]
    V --> D["Build details documented?"]
    V --> U["tasks.md updated with status?"]
    
    I & T & R & D & U --> Decision{"All Verified?"}
    Decision -->|"Yes"| Complete["Ready for REFLECT mode"]
    Decision -->|"No"| Fix["Complete missing items"]
    
    style V fill:#4dbbbb,stroke:#368787,color:white
    style Decision fill:#ffa64d,stroke:#cc7a30,color:white
    style Complete fill:#5fd94d,stroke:#3da336,color:white
    style Fix fill:#ff5555,stroke:#cc0000,color:white
```

Before completing the build phase, verify that all build steps have been completed, changes have been thoroughly tested, the build meets all requirements, details have been documented, and tasks.md has been updated with the current status. Once verified, prepare for the reflection phase.

**ЗАВЕРШЕНИЕ РАБОТЫ В РЕЖИМЕ IMPLEMENT**

1.  **Commit изменений:** Убедитесь, что все ваши изменения сохранены и закоммичены в вашей ветке:
    ```bash
    git add .
    git commit -m "feat(PROJ-123): Описание сделанных изменений"
    ```
    (Замените `PROJ-123` и сообщение коммита на актуальные)
2.  **Push ветки (если необходимо):** Если ветка новая или есть новые коммиты, отправьте ее на удаленный сервер:
    ```bash
    git push origin <branch-name>
    ```
3.  **Слияние (Merge) ветки:**
    *   Переключитесь на основную ветку разработки (например, `main` или `develop`):
        ```bash
        git checkout main
        ```
    *   Обновите основную ветку:
        ```bash
        git pull origin main
        ```
    *   Выполните слияние вашей ветки с изменениями:
        ```bash
        git merge --no-ff <branch-name>
        ```
        (Флаг `--no-ff` рекомендуется для сохранения истории веток)
    *   Решите конфликты слияния, если они возникнут.
    *   Отправьте изменения основной ветки на сервер:
        ```bash
        git push origin main
        ```
    *   **(Альтернатива)** Вместо прямого слияния, вы можете создать Pull Request (Запрос на слияние) через интерфейс GitHub/GitLab/Bitbucket для ревью кода перед слиянием. Это предпочтительный подход в командной работе.

**Только после выполнения этих шагов по фиксации и слиянию кода, переходите к следующему режиму (например, REFLECT).**
