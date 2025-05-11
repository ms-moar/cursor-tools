# Jira and Confluence Integration Settings

## Jira Integration

- **Project Key:** YOUR_JIRA_PROJECT_KEY
- **Default Issue Type:** Story
- **Status Mapping:**
  - PLAN: Backlog
  - CREATIVE: To Do
  - VAN QA: In Progress
  - IMPLEMENT: In Progress
  - REFLECT: Done
  - ARCHIVE: Done

## Project Team (optional)

- **Developers:**
  - Developer 1
  - Developer 2
  - DevOps

## Task Assignment Rules

- Before taking a task that is not assigned to the current user, a confirmation is required.
- When taking a task, the assignee must be changed to the current user.

## Task Estimation (Story Points)

- **Formula:** `1 SP = 8 developer hours = 10 AI minutes`
- **Granularity:** Use fractions if needed (e.g., 0.5 SP for smaller tasks).
- **AI Task Breakdown:** When AI performs a task, it should estimate its work in minutes. This can then be converted to SP for overall task tracking.
  - Example: If AI estimates 30 minutes for a sub-task, that's equivalent to 3 SP for that AI portion.
- **Developer Tasks:** Developer-focused tasks are estimated in ideal developer hours and then converted.
- **Combined Tasks:** For tasks involving both developer and AI work, estimate each part separately and sum the SP.
- **Jira Field:** Ensure you have a custom field for Story Points in your Jira project (e.g., `customfield_10005`). You will need to use this field's ID when creating/updating issues via API/MCP tools. The default field name in Jira is often "Story Points" or "Story Point Estimate".
- **Jira Storage:** Story Points (SP) will be stored as text directly within the Jira issue's **description field**. (e.g., "Story Points: 3" or "SP: 3").

## Confluence Integration

- **Space Key:** YOUR_CONFLUENCE_SPACE_KEY

## DevOps Integration

### GitLab Configuration

- **Project URL:** YOUR_GITLAB_PROJECT_URL
- **Repository URL:** YOUR_GITLAB_REPO_URL
- **CI/CD Pipeline URL:** YOUR_GITLAB_PIPELINE_URL
- **Default Branch:** main

### Vercel Configuration (optional)

- **Project ID:** YOUR_VERCEL_PROJECT_ID
- **Team ID:** YOUR_VERCEL_TEAM_ID
- **Default Production Branch:** main

## Setup Instructions

1. Replace `YOUR_JIRA_PROJECT_KEY` with your Jira project key (e.g., `PROJ`, `MN`, etc.)
2. ~~Identify the **Custom Field ID** for Story Points in your Jira project. Update the placeholder `customfield_10005` in the "Task Estimation" section and ensure MCP tool calls use the correct ID.~~ (Story Points are now stored in the description field of Jira issues.)
3. Replace `YOUR_CONFLUENCE_SPACE_KEY` with your Confluence space key (e.g., `docs`, `mn`, etc.)
4. If necessary, update the status mapping for your Jira workflow.
5. Specify the actual names or logins of developers in the "Project Team" section.
6. Update the GitLab configuration with your project's details.
7. If you use Vercel for deployments, update the Vercel configuration.
8. **Important:** When tasks are created/updated in Jira, their **Story Point (SP)** estimate should be included in the **description field**.

# Integration Settings

## Project Contexts

- **Active Context (Instruction for AI):** At the beginning of a relevant operation (e.g., planning, archiving), if multiple contexts are defined below, the AI MUST ask the user to specify which `context_name` to use for the current operation. The AI will then use the Jira, Confluence, and DevOps settings defined within that selected context.

- **Example Project Context 1 (replace or add more):**
  - `context_name`: "My Main Project (Alpha)"
  - `jira_project_key`: "ALPHA"
  - `jira_default_issue_type`: "Task"
  - `jira_status_mapping`:
    - PLAN: "Backlog"
    - CREATIVE: "To Do"
    - VAN_QA: "In Progress"
    - IMPLEMENT: "In Progress"
    - REFLECT: "Done"
    - ARCHIVE: "Closed"
  - `confluence_space_key`: "ALPHADOCS"
  - `gitlab_project_url`: "https://gitlab.example.com/group/alpha-project"
  - `gitlab_repo_url`: "https://gitlab.example.com/group/alpha-project.git"
  - `gitlab_pipeline_url`: "https://gitlab.example.com/group/alpha-project/-/pipelines"
  - `gitlab_default_branch`: "main"
  - `vercel_project_id` (optional): "prj_alphavercel"
  - `vercel_team_id` (optional): "team_alphateam"
  - `vercel_default_production_branch` (optional): "main"

- **Example Project Context 2 (add as needed):**
  - `context_name`: "Secondary Project (Beta Support)"
  - `jira_project_key`: "BETA"
  - `jira_default_issue_type`: "Bug"
  - `jira_status_mapping`:
    # ... (can have different status mapping if needed)
    - PLAN: "Open"
    - IMPLEMENT: "Fixing"
    - REFLECT: "Resolved"
    - ARCHIVE: "Closed"
  - `confluence_space_key`: "BETASUP"
  # ... (GitLab/Vercel specific to Beta, if different)

## Global Settings (Apply to all contexts unless overridden within a context)

### Local Task Management (`tasks.md`)
- **Purpose**: `tasks.md` serves as a local, human-readable central list of tasks across different project contexts. It mirrors key information from Jira and is used by the AI to understand current work items without constant Jira API calls for simple listings.
- **Format per Task Line**: Each task in `tasks.md` should follow this general format:
  `- [Status (e.g., x for done)] **[JIRA_PROJECT_KEY:JIRA_ISSUE_ID]** [Module Prefix (optional)] Task Title - *Brief description (optional)* - **SP: Y** (Context: [Context Name])`
  - Example: `- [ ] **[ALPHA:ALPHA-123]** [Auth] Implement MFA - *Add multi-factor auth* - **SP: 5** (Context: My Main Project (Alpha))`
- **Synchronization**: The AI is responsible for proposing updates to `tasks.md` to keep it synchronized with Jira regarding task status, title, SP, and its associated Project Context. This includes adding new tasks created in Jira and updating existing ones.

### Project Team (optional)
- **Developers:**
  - Developer 1
  - Developer 2
  - DevOps

### Task Assignment Rules
- Before taking a task that is not assigned to the current user, a confirmation is required.
- When taking a task, the assignee must be changed to the current user.

### Task Estimation (Story Points)
- **Formula:** `1 SP = 8 developer hours = 10 AI minutes`
- **Granularity:** Use fractions if needed (e.g., 0.5 SP for smaller tasks).
- **AI Task Breakdown:** When AI performs a task, it should estimate its work in minutes. This can then be converted to SP for overall task tracking.
- **Developer Tasks:** Developer-focused tasks are estimated in ideal developer hours and then converted.
- **Combined Tasks:** For tasks involving both developer and AI work, estimate each part separately and sum the SP.
- **Jira Storage:** Story Points (SP) will be stored as text directly within the Jira issue's **description field**. (e.g., "Story Points: 3" or "SP: 3").

## Setup Instructions

1.  **Define Project Contexts:**
    *   Under `## Project Contexts`, create one or more project context blocks.
    *   For each context, provide a unique `context_name`, and fill in specific `jira_project_key`, `confluence_space_key`, GitLab, and Vercel details.

2.  **Local Task File (`tasks.md`):**
    *   The system will aim to create and maintain a `tasks.md` file in the root of your workspace.
    *   This file will list tasks from your various Jira projects (as defined in `Project Contexts`).
    *   Ensure the AI has instructions (in its mode rules) to correctly parse and update tasks in this file using the format: `- [ ] **[JIRA_PROJECT_KEY:JIRA_ISSUE_ID]** Task Title - SP: Y (Context: [Context Name])`.
    *   This file helps the AI track tasks locally and reduces reliance on frequent Jira API calls for task listing and basic details.

3.  **Review Global Settings:**
    *   Update `Project Team`, `Task Assignment Rules`, and `Task Estimation (Story Points)` if needed.

4.  **How the AI will use Project Contexts:**
    *   When working on a specific task identified by its `JIRA_PROJECT_KEY:JIRA_ISSUE_ID` from `tasks.md`, the AI will look up the corresponding `Project Context` in this configuration file to get the correct Jira, Confluence, and DevOps settings.
    *   If initiating a new task or operation not tied to an existing entry in `tasks.md`, and multiple `Project Contexts` are defined, the AI **MUST ask you** which `context_name` to use.

5.  **Story Points in Jira & `tasks.md`:**
    *   Story Points are stored in the **description field** of Jira issues.
    *   The SP value should also be reflected in the `tasks.md` entry for visibility (e.g., `SP: Y`).

6.  **GitLab and Vercel:**
    *   Ensure URLs and IDs for GitLab and Vercel are correct for each project context.

7.  **Important Note on AI Behavior:**
    *   The AI's ability to correctly manage `tasks.md` and use project contexts depends on the rules in `.cursor/rules/`. These rules will need to be updated/restored to reflect `tasks.md` as the SOT for the task list and to correctly handle multi-context operations. 