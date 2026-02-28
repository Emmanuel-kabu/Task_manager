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
