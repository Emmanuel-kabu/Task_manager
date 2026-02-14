# Sprint 1 Retrospective

**Date**: February 14, 2026

---

## What Went Well

1. **Clear User Stories**: Having well-defined user stories in the standard format (Role, Action, Value) with acceptance criteria from Sprint 0 made implementation straightforward. Each endpoint was built directly from the criteria with no ambiguity.
2. **Incremental Commits**: Breaking work into small, focused commits — one per feature, one per test suite, one per config change — gave a clean history and made it easy to track what was delivered.
3. **Fast Test Feedback**: Using pytest with Flask's test client made writing and running tests very efficient — all 13 tests run in under 1 second.

## What Didn't Go Well

1. **No Logging or Error Tracking**: The application has no structured logging. When debugging test failures during development, I relied on print statements and manual inspection. This slows down debugging and provides no visibility into runtime behavior.
2. **Tests Are Not Isolated from Each Other**: All tests share the same in-memory `tasks` dictionary. Although the fixture clears it between tests, this tight coupling to the global state could cause unexpected interactions if tests run in parallel or if the storage mechanism changes.

---

## Improvements for Sprint 2

| # | Improvement | Action |
|---|------------|--------|
| 1 | **Add structured logging** | Integrate Python's `logging` module into the application so that every API request and error is logged with timestamps and severity levels. This will improve debuggability and satisfy the monitoring requirement. |
| 2 | **Improve test isolation** | Refactor tests to use an `autouse` fixture that clears state before and after each test, so the test suite is fully independent and robust. |

---

## Key Takeaway

The planning done in Sprint 0 paid off — having clear acceptance criteria and a defined DoD meant there was virtually no rework. For Sprint 2, the focus should shift to operational quality (logging, monitoring) while continuing to deliver new features.
