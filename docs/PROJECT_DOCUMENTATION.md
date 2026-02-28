# TaskFlow — Consolidated Project Documentation

> This document brings together all project documentation in one structured location.
> For sprint-specific details, see the individual documents in the `docs/` folder.

---

## Table of Contents

1. [Product Vision](#1-product-vision)
2. [User Stories (Product Backlog)](#2-user-stories-product-backlog)
3. [Acceptance Criteria](#3-acceptance-criteria)
4. [Definition of Done](#4-definition-of-done)
5. [Sprint 1 Summary](#5-sprint-1-summary)
6. [Sprint 1 Retrospective Summary](#6-sprint-1-retrospective-summary)
7. [Sprint 2 Summary](#7-sprint-2-summary)
8. [Sprint 2 Retrospective Summary](#8-sprint-2-retrospective-summary)
9. [API Reference](#9-api-reference)
10. [Testing Summary](#10-testing-summary)
11. [CI/CD Pipeline](#11-cicd-pipeline)
12. [Project Metrics](#12-project-metrics)

---

## 1. Product Vision

**TaskFlow** is a lightweight task management API that allows users to create, view, update, delete, and filter personal tasks — enabling simple and efficient productivity tracking through a clean REST interface.

---

## 2. User Stories (Product Backlog)

All user stories follow the standard format: **As a [role], I want [action], so that [value]**.

| ID | Role | Action | Value | Priority | Points |
|----|------|--------|-------|----------|--------|
| US1 | As a user | I want to create a new task | so that I can track things I need to do | High | 3 |
| US2 | As a user | I want to view all my tasks | so that I can see everything on my plate | High | 2 |
| US3 | As a user | I want to update a task | so that I can change its title, description, or status | High | 3 |
| US4 | As a user | I want to delete a task | so that I can remove items I no longer need | Medium | 2 |
| US5 | As a user | I want to filter tasks by status | so that I can focus on what matters | Medium | 3 |
| US6 | As a user | I want a health-check endpoint | so that I can verify the service is running | Low | 1 |

---

## 3. Acceptance Criteria

### US1 — Create a Task
- Given a valid JSON payload with `title` (required) and optional `description`
- When I send POST to `/tasks`
- Then a new task is created with unique `id`, status defaults to `"pending"`, returns `201`
- And if `title` is missing/empty, returns `400`

### US2 — View All Tasks
- Given tasks exist, When I send GET to `/tasks`, Then returns `200` with all tasks
- And if no tasks exist, returns `200` with empty array

### US3 — Update a Task
- Given a task exists, When I send PUT to `/tasks/<id>` with updates, Then returns `200` with updated task
- And if task not found, returns `404`; if invalid status, returns `400`

### US4 — Delete a Task
- Given a task exists, When I send DELETE to `/tasks/<id>`, Then returns `200` with confirmation
- And if task not found, returns `404`

### US5 — Filter Tasks by Status
- Given tasks exist, When I send GET to `/tasks?status=done`, Then returns only matching tasks
- And if invalid status, returns `400`

### US6 — Health Check
- Given the service is running, When I send GET to `/health`, Then returns `200` with health status

---

## 4. Definition of Done

A user story is Done when:
1. Code implements all acceptance criteria
2. Unit tests written and passing
3. CI pipeline passes
4. Changes committed with clear messages
5. Documentation updated
6. Code is clean and peer-reviewable

---

## 5. Sprint 1 Summary

**Goal**: Deliver core task CRUD (create, read, update) and establish CI/CD.

| Story | Points | Status |
|-------|--------|--------|
| US1 — Create a Task | 3 | Done |
| US2 — View All Tasks | 2 | Done |
| US3 — Update a Task | 3 | Done |

**Velocity**: 8/8 points (100%)
**Tests**: 13 passing

---

## 6. Sprint 1 Retrospective Summary

**What went well**: Clear user stories, incremental commits, fast test feedback.
**What to improve**: No logging (added in Sprint 2), test isolation concerns (fixed in Sprint 2).

---

## 7. Sprint 2 Summary

**Goal**: Add delete/filter/health features, apply retro improvements (logging + test isolation).

| Story | Points | Status |
|-------|--------|--------|
| US4 — Delete a Task | 2 | Done |
| US5 — Filter Tasks by Status | 3 | Done |
| US6 — Health Check | 1 | Done |

**Velocity**: 6/6 points (100%)
**Tests**: 22 passing

---

## 8. Sprint 2 Retrospective Summary

**Improvements applied**: Structured logging (INFO/WARNING), autouse test fixture for isolation.
**Lessons learned**: Planning eliminates rework, small commits build trust, retrospectives must be actionable.

---

## 9. API Reference

### POST `/tasks` — Create a Task
```json
Request:  {"title": "Buy groceries", "description": "Milk, eggs"}
Response: {"id": "uuid", "title": "...", "status": "pending", "created_at": "ISO-8601"}
```

### GET `/tasks` — List All Tasks
```json
Response: [{"id": "...", "title": "...", "status": "...", ...}]
```

### GET `/tasks?status=done` — Filter by Status
Valid values: `pending`, `in-progress`, `done`

### PUT `/tasks/<id>` — Update a Task
```json
Request:  {"title": "New title", "status": "done"}
Response: {"id": "...", "title": "New title", "status": "done", "updated_at": "ISO-8601"}
```

### DELETE `/tasks/<id>` — Delete a Task
```json
Response: {"message": "Task 'Buy groceries' deleted successfully"}
```

### GET `/health` — Health Check
```json
Response: {"status": "healthy", "timestamp": "ISO-8601", "task_count": 5}
```

---

## 10. Testing Summary

| Suite | Tests | Coverage |
|-------|-------|----------|
| US1 — Create | 5 | Happy path + error cases |
| US2 — View | 2 | Empty + populated |
| US3 — Update | 6 | Title, status, errors, timestamp |
| US4 — Delete | 3 | Success, removal, 404 |
| US5 — Filter | 4 | Valid filter, invalid, empty |
| US6 — Health | 2 | Status, task count |
| **Total** | **22** | **All pass** |

---

## 11. CI/CD Pipeline

GitHub Actions pipeline (`.github/workflows/ci.yml`):
- Triggers on push/PR to `main`
- Sets up Python 3.12
- Installs dependencies
- Runs `pytest tests/ -v`

---

## 12. Project Metrics

| Metric | Value |
|--------|-------|
| User Stories Delivered | 6/6 |
| Story Points Delivered | 14 |
| Sprint Velocity | Sprint 1: 8, Sprint 2: 6 |
| Unit Tests | 22 |
| Test Pass Rate | 100% |
| CI/CD | GitHub Actions |
| Logging | Python logging (INFO/WARNING) |
| Monitoring | `/health` endpoint |
