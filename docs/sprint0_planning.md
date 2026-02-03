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

---

## 3. Acceptance Criteria

### US1 — Create a Task
- **Given** a valid JSON payload with `title` (required) and optional `description`,
- **When** I send a POST request to `/tasks`,
- **Then** a new task is created with a unique `id`, `status` defaults to `"pending"`, and the response returns `201 Created` with the task JSON.
- **And** if `title` is missing or empty, the API returns `400 Bad Request` with an error message.

### US2 — View All Tasks
- **Given** tasks exist in the system,
- **When** I send a GET request to `/tasks`,
- **Then** the API returns `200 OK` with a JSON array of all tasks.
- **And** if no tasks exist, the API returns `200 OK` with an empty array `[]`.

### US3 — Update a Task
- **Given** a task with a known `id` exists,
- **When** I send a PUT request to `/tasks/<id>` with updated fields (`title`, `description`, or `status`),
- **Then** the task is updated and the API returns `200 OK` with the updated task JSON.
- **And** if the task `id` does not exist, the API returns `404 Not Found`.
- **And** `status` must be one of `"pending"`, `"in-progress"`, or `"done"`.

### US4 — Delete a Task
- **Given** a task with a known `id` exists,
- **When** I send a DELETE request to `/tasks/<id>`,
- **Then** the task is removed and the API returns `200 OK` with a confirmation message.
- **And** if the task `id` does not exist, the API returns `404 Not Found`.

### US5 — Filter Tasks by Status
- **Given** tasks exist with various statuses,
- **When** I send a GET request to `/tasks?status=done`,
- **Then** the API returns `200 OK` with only the tasks matching that status.
- **And** if the status value is invalid, the API returns `400 Bad Request`.

### US6 — Health Check
- **Given** the service is running,
- **When** I send a GET request to `/health`,
- **Then** the API returns `200 OK` with `{"status": "healthy", "timestamp": "<ISO-8601>", "task_count": <int>}`.

---

## 4. Definition of Done (DoD)

A user story is considered **Done** when ALL of the following are met:

1. **Code Complete**: Feature code is written and implements all acceptance criteria.
2. **Tests Written**: Unit tests cover the feature and all pass.
3. **CI Pipeline Passes**: The code passes linting and all tests in the CI/CD pipeline.
4. **Code Committed**: Changes are committed to the `main` branch with clear, descriptive commit messages.
5. **Documentation Updated**: Any relevant docs (README, API docs) are updated.
6. **Peer-Reviewable**: Code is clean, readable, and follows project conventions.

---

## 5. Sprint 1 Plan

**Sprint Goal**: Deliver the core task creation and viewing functionality, and establish the CI/CD pipeline.

| Story | Story Points |
|-------|-------------|
| US1 — Create a Task | 3 |
| US2 — View All Tasks | 2 |
| US3 — Update a Task | 3 |

**Total Planned Points**: 8

**Key Activities**:
- Set up project structure (Flask app, requirements, tests directory)
- Implement POST `/tasks` endpoint (US1)
- Implement GET `/tasks` endpoint (US2)
- Implement PUT `/tasks/<id>` endpoint (US3)
- Write unit tests for all endpoints
- Set up GitHub Actions CI pipeline
- Conduct Sprint Review and Retrospective

---

## 6. Sprint 2 Plan (Tentative)

**Sprint Goal**: Add delete and filter functionality, implement monitoring/logging, and apply Sprint 1 retrospective improvements.

| Story | Story Points |
|-------|-------------|
| US4 — Delete a Task | 2 |
| US5 — Filter Tasks by Status | 3 |
| US6 — Health Check | 1 |

**Total Planned Points**: 6
