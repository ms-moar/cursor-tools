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
        *   Check the status of tasks in Jira and synchronize them with `tasks.md`.
        *   Update task status in Jira at key transition points.
        *   Track assignees and, if necessary, suggest changes (e.g., when taking tasks from others).
    *   Added default mapping from internal Memory Bank modes/phases to Jira statuses.
*   **Direct Confluence integration:**
    *   When archiving a task, the system now creates a summary document both locally and in the configured Confluence space.
*   **Improved task tracking in `tasks.md`:**
    *   Added a requirement to include Jira issue keys for all tasks.
    *   Added functionality to update the file when tasks change status in Jira.

## DevOps Integration (Session from [Current Date])

A new `devops-tools` folder has been added to the project with tools to support continuous integration and deployment:

*   **GitLab CI/CD Integration:**
    *   Added automatic GitLab pipeline status checking in the IMPLEMENT and QA modes.
    *   Integrated GitLab tagging into the ARCHIVE mode for marking completed tasks.
    *   Added validation of GitLab CI/CD configuration in QA mode.
    *   Mode maps updated to include GitLab commands and validation steps.

*   **Vercel Deployment (Optional):**
    *   Added optional integration with Vercel for deployment verification and triggering.
    *   Updated QA mode to check Vercel configuration when applicable.
    *   Added user verification step to confirm if Vercel is used in the project.

*   **Configuration Updates:**
    *   Enhanced `integration_config.md` with GitLab and Vercel configuration sections.
    *   Updated instructions to include the setup of DevOps tools.

*   **Automatic Backup Before Deletion:**
    *   Added a mandatory rule in Cursor's base rule to automatically create backups of files before deleting them.
    *   The backup system uses the dedicated `backup-files/` folder with timestamped copies. 