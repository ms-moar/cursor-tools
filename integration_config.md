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
2. Replace `YOUR_CONFLUENCE_SPACE_KEY` with your Confluence space key (e.g., `docs`, `mn`, etc.)
3. If necessary, update the status mapping for your Jira workflow.
4. Specify the actual names or logins of developers in the "Project Team" section.
5. Update the GitLab configuration with your project's details.
6. If you use Vercel for deployments, update the Vercel configuration.
7. **Important:** For each task in the tasks.md file, the corresponding Jira issue key must be specified and kept up-to-date. 