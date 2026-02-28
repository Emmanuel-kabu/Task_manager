# Sprint 2 Review

**Sprint Goal**: Apply Sprint 1 retrospective improvements, deliver delete/filter/health features, and add monitoring/logging.

**Date**: February 28, 2026
**Sprint Duration**: 1 sprint cycle

---

## Sprint Backlog Summary

| Story | Points | Status |
|-------|--------|--------|
| US4 — Delete a Task | 2 | Done |
| US5 — Filter Tasks by Status | 3 | Done |
| US6 — Health Check | 1 | Done |

**Planned Points**: 6
**Completed Points**: 6
**Velocity**: 6 points

---

## Retrospective Improvements Applied

| Improvement | What Was Done |
|-------------|---------------|
| **#1 — Structured Logging** | Integrated Python's `logging` module with timestamp formatting. Every API request (success and failure) is now logged with severity levels (INFO/WARNING). |
| **#2 — Test Isolation** | Added an `autouse` fixture (`clean_tasks`) that clears the task store before and after every test. All tests are fully independent. |

---

## What Was Delivered

### US4 — Delete a Task (DELETE `/tasks/<id>`)
- **Role**: As a user
- **Action**: I want to delete a task by its ID
- **Value**: So that I can remove items I no longer need to track
- Returns `200 OK` with a confirmation message including the deleted task's title.
- Returns `404 Not Found` for non-existent task IDs.
- Deletion is logged with the task title for auditability.

### US5 — Filter Tasks by Status (GET `/tasks?status=<status>`)
- **Role**: As a user
- **Action**: I want to filter my task list by status
- **Value**: So that I can focus on what matters most right now
- Valid statuses: `pending`, `in-progress`, `done`.
- Returns `400 Bad Request` for invalid status values.
- Works seamlessly with the existing GET `/tasks` endpoint.

### US6 — Health Check (GET `/health`)
- **Role**: As a user (or operations team)
- **Action**: I want to check if the service is running
- **Value**: So that I can verify the API is healthy before making requests
- Returns service health status, current ISO-8601 timestamp, and task count.

---

## Monitoring & Logging

Structured logging was added across the entire application:
- **INFO** level: Successful operations (task created, updated, deleted, health check).
- **WARNING** level: Validation failures (missing title, invalid status, task not found).

---

## Testing Summary

| Test Suite | Tests | Status |
|-----------|-------|--------|
| TestCreateTask | 5 | All Pass |
| TestGetTasks | 2 | All Pass |
| TestUpdateTask | 6 | All Pass |
| TestDeleteTask | 3 | All Pass |
| TestFilterTasks | 4 | All Pass |
| TestHealthCheck | 2 | All Pass |
| **Total** | **22** | **All Pass** |

---

## Definition of Done Checklist

- [x] Code complete — all acceptance criteria met for US4, US5, US6
- [x] Retrospective improvements from Sprint 1 applied
- [x] Unit tests written and passing (22/22)
- [x] CI pipeline passes
- [x] Changes committed with clear, incremental messages
- [x] Monitoring/logging implemented

---

## Cumulative Project Summary

| Metric | Value |
|--------|-------|
| Total User Stories Delivered | 6 of 6 |
| Total Story Points Delivered | 14 |
| Total Unit Tests | 22 |
| CI Pipeline | GitHub Actions (test on push/PR) |
| Logging | Python `logging` module (INFO/WARNING) |
| Monitoring | `/health` endpoint |
