# Sprint 1 Review

**Sprint Goal**: Deliver the core task creation, viewing, and update functionality, and establish the CI/CD pipeline.

**Date**: February 14, 2026
**Sprint Duration**: 1 sprint cycle

---

## Sprint Backlog Summary

| Story | Points | Status |
|-------|--------|--------|
| US1 — Create a Task | 3 | Done |
| US2 — View All Tasks | 2 | Done |
| US3 — Update a Task | 3 | Done |

**Planned Points**: 8
**Completed Points**: 8
**Velocity**: 8 points

---

## What Was Delivered

### US1 — Create a Task (POST `/tasks`)
- **Role**: As a user
- **Action**: I want to create a new task with a title and optional description
- **Value**: So that I can track things I need to do
- Tasks are assigned a unique UUID, default status `"pending"`, and a creation timestamp.
- Validation rejects requests missing or blank `title` fields with a `400 Bad Request`.

**Example Request**:
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

**Example Response** (201 Created):
```json
{
  "id": "a1b2c3d4-...",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending",
  "created_at": "2026-02-14T10:30:00+00:00"
}
```

### US2 — View All Tasks (GET `/tasks`)
- **Role**: As a user
- **Action**: I want to view all my tasks in a list
- **Value**: So that I can see everything on my plate at a glance
- Returns a JSON array of all tasks.
- Returns an empty array `[]` when no tasks exist.

### US3 — Update a Task (PUT `/tasks/<id>`)
- **Role**: As a user
- **Action**: I want to update a task's title, description, or status
- **Value**: So that I can reflect changes or progress on my tasks
- Status validation ensures only `"pending"`, `"in-progress"`, or `"done"` are accepted.
- Returns `404 Not Found` for non-existent task IDs.
- Adds an `updated_at` timestamp on successful update.

---

## CI/CD Pipeline

A GitHub Actions pipeline (`ci.yml`) was configured to:
1. Trigger on push/PR to `main` branch.
2. Set up Python 3.12.
3. Install dependencies from `requirements.txt`.
4. Run all unit tests with `pytest`.

---

## Testing Summary

| Test Suite | Tests | Status |
|-----------|-------|--------|
| TestCreateTask | 5 | All Pass |
| TestGetTasks | 2 | All Pass |
| TestUpdateTask | 6 | All Pass |
| **Total** | **13** | **All Pass** |

---

## Definition of Done Checklist

- [x] Code complete — all acceptance criteria met
- [x] Unit tests written and passing (13/13)
- [x] CI pipeline configured and functional
- [x] Changes committed with clear, incremental messages
- [x] README updated with API documentation
