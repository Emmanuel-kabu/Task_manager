# TaskFlow — Task Manager API

A lightweight REST API for managing personal tasks, built with Python and Flask.

## Product Vision

**TaskFlow** enables users to create, view, update, delete, and filter personal tasks through a clean REST interface for simple productivity tracking.

## Tech Stack

- **Language**: Python 3.10+
- **Framework**: Flask
- **Testing**: pytest
- **CI/CD**: GitHub Actions

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python app.py
```

The API will be available at `http://localhost:5000`.

### 3. Run tests

```bash
pytest tests/ -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/tasks` | Create a new task (US1) |
| GET | `/tasks` | List all tasks (US2), optionally filter by `?status=` (US5) |
| PUT | `/tasks/<id>` | Update a task (US3) |
| DELETE | `/tasks/<id>` | Delete a task (US4) |
| GET | `/health` | Health check (US6) |

## Project Structure

```
Agile_project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── CONTRIBUTING.md        # Contribution guidelines
├── tests/
│   └── test_app.py        # Unit tests (22 tests)
├── docs/
│   ├── sprint0_planning.md
│   ├── sprint1_review.md
│   ├── sprint1_retrospective.md
│   ├── sprint2_review.md
│   ├── sprint2_retrospective.md
│   └── PROJECT_DOCUMENTATION.md   # Consolidated project documentation
└── .github/
    └── workflows/
        └── ci.yml         # CI/CD pipeline
```

## Documentation

All project documentation is consolidated in the `docs/` folder:

- **[Sprint 0 Planning](docs/sprint0_planning.md)** — Product vision, backlog, acceptance criteria, DoD
- **[Sprint 1 Review](docs/sprint1_review.md)** — Sprint 1 delivery summary
- **[Sprint 1 Retrospective](docs/sprint1_retrospective.md)** — Sprint 1 reflection and improvements
- **[Sprint 2 Review](docs/sprint2_review.md)** — Sprint 2 delivery summary
- **[Sprint 2 Retrospective](docs/sprint2_retrospective.md)** — Final retrospective and lessons learned
- **[Consolidated Documentation](docs/PROJECT_DOCUMENTATION.md)** — Complete project documentation in one place

## Agile Artifacts

All planning documents, sprint reviews, and retrospectives are in the `docs/` folder. See the [Consolidated Documentation](docs/PROJECT_DOCUMENTATION.md) for a full overview of the agile process, user stories, and project outcomes.
