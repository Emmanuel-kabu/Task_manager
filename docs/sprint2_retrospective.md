# Sprint 2 Retrospective (Final)

**Date**: February 28, 2026

---

## What Went Well

1. **Retrospective-Driven Improvement**: Both improvements identified in Sprint 1 were successfully implemented. Structured logging now provides visibility into every API operation, and the test suite is fully isolated with the `autouse` fixture pattern.

2. **Consistent Velocity**: Sprint 1 delivered 8 points and Sprint 2 delivered 6 points, both meeting 100% of planned scope. The slightly lower Sprint 2 estimate was intentional — it accounted for the overhead of applying retrospective improvements alongside feature delivery.

3. **High Test Coverage**: The test suite grew from 13 to 22 tests, covering all 6 user stories including both happy paths and error cases.

4. **Incremental Commit History**: Every commit corresponds to a single logical change — one feature, one test suite, one improvement. No bundled or big-bang commits.

## What Didn't Go Well

1. **In-Memory Storage Limitation**: Using a Python dictionary for storage means all tasks are lost when the server restarts. A persistent database (e.g., SQLite) would be necessary for production.

2. **No Authentication or Authorization**: The API is fully open. A real product would need user authentication and per-user task scoping.

---

## Improvements Applied (from Sprint 1 Retro)

| Improvement | Outcome |
|-------------|---------|
| **#1 — Structured Logging** | Fully implemented. Every endpoint logs its operation with timestamps and severity levels. |
| **#2 — Test Isolation** | Fully implemented. An `autouse` fixture clears the task store before and after each test. All 22 tests are independent. |

---

## Key Lessons Learned

### 1. Planning Pays Off
The time invested in Sprint 0 (defining clear user stories with Role/Action/Value format and acceptance criteria) eliminated ambiguity during execution.

### 2. Small, Frequent Commits Build Trust
Committing after each logical unit of work creates a transparent and auditable history. It also makes debugging easier.

### 3. Retrospectives Must Be Actionable
The Sprint 1 retrospective identified **specific** problems with **specific** actions, making Sprint 2 improvements concrete and verifiable.

### 4. CI/CD Catches Issues Early
Having automated tests in the pipeline means every push is validated, preventing regressions.

### 5. Agile Is About Discipline, Not Ceremony
The value of Agile is in the discipline of planning before building, delivering incrementally, reflecting honestly, and improving continuously.
