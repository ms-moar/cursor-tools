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