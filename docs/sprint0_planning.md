# Sprint 0: Planning

## 1. Product Vision

**TaskFlow** is a lightweight task management API that allows users to create, view, update, delete, and filter personal tasks — enabling simple and efficient productivity tracking through a clean REST interface.

---

## 2. Product Backlog (User Stories)

All user stories follow the standard format: **As a [role], I want [action], so that [value]**.

| ID  | Role | Action | Value | Priority | Story Points |
|-----|------|--------|-------|----------|-------------|
| US1 | As a user | I want to create a new task | so that I can track things I need to do | High | 3 |
| US2 | As a user | I want to view all my tasks | so that I can see everything on my plate | High | 2 |
| US3 | As a user | I want to update a task | so that I can change its title, description, or status | High | 3 |
| US4 | As a user | I want to delete a task | so that I can remove items I no longer need | Medium | 2 |
| US5 | As a user | I want to filter tasks by status | so that I can focus on what matters | Medium | 3 |
| US6 | As a user | I want a health-check endpoint | so that I can verify the service is running | Low | 1 |

### User Story Details

#### US1 — Create a Task
- **Role**: As a user
- **Action**: I want to create a new task with a title and optional description
- **Value**: So that I can track things I need to do

#### US2 — View All Tasks
- **Role**: As a user
- **Action**: I want to view all my tasks in a list
- **Value**: So that I can see everything on my plate at a glance

#### US3 — Update a Task
- **Role**: As a user
- **Action**: I want to update a task's title, description, or status
- **Value**: So that I can reflect changes or progress on my tasks

#### US4 — Delete a Task
- **Role**: As a user
- **Action**: I want to delete a task by its ID
- **Value**: So that I can remove items I no longer need to track

#### US5 — Filter Tasks by Status
- **Role**: As a user
- **Action**: I want to filter my task list by status (pending, in-progress, done)
- **Value**: So that I can focus on what matters most right now

#### US6 — Health Check
- **Role**: As a user (or operations team)
- **Action**: I want to check if the service is running
- **Value**: So that I can verify the API is healthy before making requests
