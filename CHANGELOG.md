# Changelog (Jira/Confluence Integration)

This document describes the main changes made to the `cursor-memory-bank` project fork to implement Jira and Confluence integration using MCP tools and flexible configuration.

## New Files

*   **`integration_config.md`**:
    *   Created for centralized storage of integration settings.
    *   Contains placeholders for the Jira project key (`YOUR_JIRA_PROJECT_KEY`) and Confluence space key (`YOUR_CONFLUENCE_SPACE_KEY`).
    *   Includes the default Jira issue type (`Story`).
    *   Contains Jira status mapping for each system operation mode (PLAN, CREATIVE, VAN QA, IMPLEMENT, REFLECT, ARCHIVE).
    *   Includes setup instructions for the user.

## Changed Files

*   **`.cursor/rules/isolation_rules/visual-maps/plan-mode-map.mdc`**:
    *   Added a step to read settings from `integration_config.md`.
    *   Added logic to request **existing** Jira components and labels from the user.
    *   Added semi-autonomous logic for working with Epics:
        *   Request from the user if the task is related to an Epic.
        *   Search for existing Epics by keywords using `mcp_mcp-atlassian_jira_search`.
        *   Offer the user to select an existing Epic, skip, or create a new one.
        *   Create a new Epic if necessary using `mcp_mcp-atlassian_jira_create_issue`.
    *   Added a call to `mcp_mcp-atlassian_jira_create_issue` to create a task (Story) using data from the config, user input (components, labels), and the defined Epic link.
    *   Added logic to write the received Jira issue ID to the `tasks.md` file (in the format `[Jira: KEY-123]`).
    *   Added notes on MCP error handling (retry).

*   **`.cursor/rules/isolation_rules/visual-maps/creative-mode-map.mdc`**:
    *   Added a step to read settings from `integration_config.md` (Jira status, Confluence space key).
    *   Added logic to read the Jira issue ID from `tasks.md`.
    *   Added a call to `mcp_mcp-atlassian_jira_update_issue` to update the Jira issue status according to settings.
    *   Added a call to `mcp_mcp-atlassian_confluence_create_page` to create a design documentation page in the configured Confluence space.
    *   Added notes on MCP error handling.

*   **`.cursor/rules/isolation_rules/visual-maps/qa-mode-map.mdc`**:
    *   Added a step to read settings from `integration_config.md` (Jira status for successful QA).
    *   Added logic to read the Jira issue ID from `tasks.md`.
    *   Added a call to `mcp_mcp-atlassian_jira_update_issue` to update the Jira issue status upon successful validation.
    *   Added notes on MCP error handling.

*   **`.cursor/rules/isolation_rules/visual-maps/reflect-mode-map.mdc`**:
    *   Added a step to read settings from `integration_config.md` (Jira status for reflection completion).
    *   Added logic to read the Jira issue ID from `tasks.md`.
    *   Added a call to `mcp_mcp-atlassian_jira_update_issue` to update the Jira issue status.
    *   Added notes on MCP error handling.

*   **`.cursor/rules/isolation_rules/visual-maps/archive-mode-map.mdc`**:
    *   Added a step to read settings from `integration_config.md` (Confluence space key).
    *   Added logic to check/create the `docs/archive/` directory.
    *   Added logic to create a local summary file in `docs/archive/` using the Jira issue ID.
    *   Added a call to `mcp_mcp-atlassian_confluence_create_page` to create/update a summary page in the configured Confluence space.
    *   Updated checklist and final message to reflect the creation of the local file and Confluence page.
    *   Added notes on MCP error handling.

## Important Notes

*   Before using the system, you **must configure** the `integration_config.md` file, specifying the actual Jira and Confluence keys.
*   For the local documentation saving step in `ARCHIVE` mode to work correctly, ensure that the `docs/` folder exists at the project root or will be created.
*   There were issues saving changes to `plan-mode-map.mdc`; an attempt was made to reapply the changes. It is recommended to check this file.

---

## Integration Logic and Workflow Updates (Session from [Date or Identifier])

During iterative development, the following changes were made to the custom mode instructions (`custom_modes/*.md`) to improve Jira and Git integration:

*   **Transition to semi-automatic Jira integration:**
    *   Instead of manual checks and updates of statuses/assignees in Jira by the user, the system now uses MCP tools (`mcp_mcp-atlassian_jira_*`) to:
        *   Automatically check the statuses of completed tasks in Jira and suggest edits for `tasks.md` in case of discrepancies.
        *   Automatically check task names in Jira and suggest edits for `tasks.md` in case of discrepancies.
        *   Suggest specific actions in Jira (change status, assign) at key points in the process (end of `PLAN`, beginning of `CREATIVE`, beginning of `IMPLEMENT`).
    *   Actions in Jira and edits to `tasks.md` are performed automatically **only after user approval** of the corresponding suggestion in the Cursor interface.
*   **Proactive task selection:**
    *   At the beginning of `VAN`, `PLAN`, `CREATIVE`, `IMPLEMENT` modes, the system can now (using MCP search in Jira) **suggest a list of tasks** suitable for the current stage, instead of always waiting for an ID from the user.
*   **Improved status synchronization:**
    *   After successfully automatically changing the status/assignee of a task in Jira, the system immediately **suggests an edit** for `tasks.md` to update the local task status.
*   **Epic tracking:**
    *   In `PLAN` mode, logic has been added to automatically check the task's link to an Epic in Jira and **suggest an edit** for `tasks.md` to record this link (e.g., in an 'Epic' column).
*   **Checking current tasks:**
    *   At the beginning of `PLAN` mode, a check has been added for tasks in Jira already in "In Progress" / "To Do" status and assigned to the user. The system will suggest continuing work on them before planning new ones.
*   **Git integration:**
    *   Explicit steps have been added to the `CREATIVE` and `IMPLEMENT` mode instructions with a **suggestion to create/check for a Git branch** for the current task.
    *   A detailed block has been added to the end of the `IMPLEMENT` mode instructions with a **suggestion to commit, push, and merge the branch** (or create a Pull Request).

These changes are aimed at reducing manual synchronization efforts, increasing transparency, and improving the integration of the Cursor workflow with Jira and Git. 