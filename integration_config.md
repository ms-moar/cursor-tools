# Integration Configuration for Memory Bank System

This document centralizes all integration settings for the Memory Bank system, including project contexts for Jira, Confluence, and DevOps tools, as well as global rules for task management and estimation.

## Project Contexts

Define different project contexts here. Each context can have its own set of keys and URLs for various integrated services. This allows the AI to switch between different project configurations seamlessly.

**Instructions for AI:** When a mode is activated that interacts with Jira, Confluence, GitLab, or Vercel, you **MUST** first ask the user to specify which `activeProjectContext` they are working with if multiple contexts are defined below. Store this selection and use the corresponding keys/URLs for all operations within that session for that mode.

**Example Context Structure:**

```
- context_name: "Main Project (Alpha)"
  description: "Primary development project for the Alpha release."
  jira_project_key: "ALPHA"
  jira_default_issue_type: "Story" # e.g., Story, Task, Bug
  jira_status_mapping:
    PLAN: "Backlog"
    CREATIVE_START: "To Do" # Status when creative phase begins
    CREATIVE_COMPLETE: "In Progress" # Status when creative (design) is done
    IMPLEMENT_START: "In Progress" # Status when implementation begins
    IMPLEMENT_COMPLETE: "In Review" # Status when implementation is done, awaiting QA/Reflect
    QA_PASS: "Done" # Status if QA passes
    REFLECT_COMPLETE: "Done" # Status after reflection, if it's the final step
    ARCHIVE: "Closed" # Status when task is fully archived
  confluence_space_key: "ALPHADOCS"
  gitlab_project_id: "your_gitlab_project_id_alpha" # or full URL
  gitlab_default_branch: "main"
  vercel_project_id: "your_vercel_project_id_alpha"
  vercel_team_id: "your_vercel_team_id_alpha" # Optional

- context_name: "Internal Tools Project (Omega)"
  description: "Project for developing internal utilities."
  jira_project_key: "OMEGA"
  jira_default_issue_type: "Task"
  jira_status_mapping:
    PLAN: "To Do"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "OMEGATOOLS"
  gitlab_project_id: "your_gitlab_project_id_omega"
  gitlab_default_branch: "develop"
  # Vercel might not be applicable here
  # vercel_project_id: null 
```

**Actual Project Contexts:**

_(User: Please fill in your actual project contexts below, following the example structure.)_

```
- context_name: "YOUR_CONTEXT_NAME_HERE"
  description: "Description for your project context."
  jira_project_key: "YOUR_JIRA_PROJECT_KEY"
  jira_default_issue_type: "Story" 
  jira_status_mapping:
    PLAN: "Backlog"
    CREATIVE_START: "To Do"
    CREATIVE_COMPLETE: "In Progress"
    IMPLEMENT_START: "In Progress"
    IMPLEMENT_COMPLETE: "In Review"
    QA_PASS: "Done" 
    REFLECT_COMPLETE: "Done"
    ARCHIVE: "Closed"
  confluence_space_key: "YOUR_CONFLUENCE_SPACE_KEY"
  gitlab_project_id: "YOUR_GITLAB_PROJECT_ID"
  gitlab_default_branch: "main"
  vercel_project_id: "YOUR_VERCEL_PROJECT_ID"
  vercel_team_id: "YOUR_VERCEL_TEAM_ID"
```

## Global Settings

These settings apply across all project contexts unless overridden within a specific context.

### Local Task Management (`tasks.md`)
*   **Purpose**: `tasks.md` is the primary local file for tracking tasks across different project contexts. It is intended to be managed by the AI system.
*   **AI Role**: The AI is responsible for creating this file if it doesn't exist (based on a defined template), reading it, parsing its content, updating it with new tasks from Jira (for the active context), reflecting status changes from Jira, and proposing edits to the user for confirmation.
*   **Format**: Each task entry in `tasks.md` **MUST** follow this format:
    `- [ ] **[JIRA_PROJECT_KEY:JIRA_ISSUE_ID]** Task Title - *Brief description* - SP_VALUE=[X] (Context: Context Name)`
    *   `JIRA_PROJECT_KEY:JIRA_ISSUE_ID`: e.g., `ALPHA:ALPHA-123`
    *   `SP_VALUE=[X]`: Story Points for the task, where X is an integer or a float (e.g., 0.5, 1, 2.5). Example: `SP_VALUE=3`, `SP_VALUE=0.5`.
    *   `Context: Context Name`: The `context_name` from the "Project Contexts" section this task belongs to.
*   **Synchronization**: The AI should strive to keep `tasks.md` synchronized with Jira for the tasks relevant to the active contexts.

### Project Team (optional)
You can list default team members here if tasks are often assigned to the same group.
*   **Developers**:
    *   Developer 1 (Default Assignee)
    *   Developer 2
*   **DevOps**:
    *   DevOps Engineer 1
*   **QA**:
    *   QA Specialist 1

### Task Assignment Rules
*   Before taking a task that is assigned to another user in Jira, the AI must confirm with the current user.
*   If the current user decides to take the task, the AI must propose changing the assignee in Jira to the current user.

### Task Estimation (Story Points)
*   **Formula Guideline**: `1 SP (Story Point) = approximately 8 developer hours = approximately 10 AI minutes` (This is a loose guideline for the AI's internal understanding and relative estimation, not a strict conversion for human team members).
*   **AI-Driven Estimation**: The AI is responsible for providing the **final SP estimate** for tasks during the `PLAN` mode. This estimate is based on its analysis and is not typically subject to user review for adjustment, though the user can override if necessary.
*   **Storage in Jira**: Story Points **MUST** be stored as plain text within the **description field** of the Jira issue (Epic or Story/Task) using the exact format: `SP_VALUE=[X]`.
    *   `SP_VALUE=`: This is the key prefix. It must be uppercase S, P, _, V, A, L, U, E, followed by an equals sign. No spaces before or after the equals sign are preferred.
    *   `[X]`: This is the actual Story Points value. It can be an integer (e.g., 1, 2, 3, 5, 8, 13) or a float using a period as a decimal separator (e.g., 0.5, 1.5, 2.5).
    *   Examples: `SP_VALUE=3`, `SP_VALUE=0.5`, `SP_VALUE=8`.
*   **Small Epics**: For Epics estimated by the AI to be "small" (e.g., total SP of sub-tasks < 7 SP), individual sub-tasks should NOT be created as separate Jira issues. Instead, the list of sub-tasks and their individual SPs (each formatted as `SP_VALUE=X`) should be documented within the description of the parent Epic Jira issue. The Epic itself will also have its total SP recorded in its description using the `SP_VALUE=X` format.

## Setup Instructions

1.  **Configure Project Contexts**:
    *   Duplicate the example context structure under "Actual Project Contexts".
    *   Replace placeholder values (e.g., `YOUR_JIRA_PROJECT_KEY`, `YOUR_CONFLUENCE_SPACE_KEY`, `YOUR_GITLAB_PROJECT_ID`, `YOUR_VERCEL_PROJECT_ID`) with your actual project details for each context you work with.
    *   Adjust `jira_status_mapping` for each context to match your Jira workflow statuses precisely. The provided statuses are examples.
    *   Ensure `context_name` is unique for each defined context.

2.  **Review Global Settings**:
    *   Modify the `Project Team` list if needed.
    *   Understand the `Task Assignment Rules`.
    *   Understand the `Task Estimation (Story Points)` guidelines, especially how SPs are estimated by the AI and stored in Jira task descriptions using the `SP_VALUE=[X]` format.

3.  **`tasks.md` Management**:
    *   The AI will manage the `tasks.md` file. If it's missing, the AI should create it based on a standard template (see "Local Task Management" section).
    *   Ensure the AI understands to parse and update `tasks.md` according to the specified format, especially the `SP_VALUE=[X]` and `(Context: Context Name)` parts.

4.  **Inform the AI**:
    *   Once configured, ensure the AI is aware of this `integration_config.md` file and is instructed to use it as the primary source for all integration parameters and global settings.
    *   Remind the AI to always ask for the `activeProjectContext` when starting modes that use these integrations.

This centralized configuration will help streamline operations and ensure consistency across different tools and project phases. 