"""
Rebuild the git history for TaskFlow with 55 incremental commits.
Each commit represents a single logical unit of work.

Usage:
    python rebuild_history.py

WARNING: This will replace the current git history. A backup of
.git is saved as .git_backup before starting.
"""

import os
import shutil
import subprocess
import sys
from datetime import datetime, timedelta

# ── Configuration ────────────────────────────────────────────────
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
AUTHOR_NAME = "Emmanuel Kabu"
AUTHOR_EMAIL = "emmanuel.kabu@amalitech.com"

# Sprint dates (spread realistically)
SPRINT0_START = datetime(2026, 2, 1, 9, 0, 0)
SPRINT1_START = datetime(2026, 2, 4, 9, 0, 0)
SPRINT1_REVIEW = datetime(2026, 2, 14, 14, 0, 0)
SPRINT2_START = datetime(2026, 2, 15, 9, 0, 0)
SPRINT2_REVIEW = datetime(2026, 2, 28, 14, 0, 0)


def git(*args, cwd=None):
    """Run a git command in the project directory."""
    result = subprocess.run(
        ["git"] + list(args),
        cwd=cwd or PROJECT_DIR,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  ERROR: git {' '.join(args)}")
        print(f"  {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()


def commit(message, date):
    """Stage all changes and commit with a specific date."""
    env_date = date.strftime("%Y-%m-%dT%H:%M:%S")
    git("add", "-A")
    git(
        "commit",
        "-m", message,
        "--author", f"{AUTHOR_NAME} <{AUTHOR_EMAIL}>",
        "--date", env_date,
    )
    # Also set committer date
    os.environ["GIT_COMMITTER_DATE"] = env_date
    print(f"  [{date.strftime('%b %d %H:%M')}] {message}")


def write_file(rel_path, content):
    """Write content to a file relative to project root."""
    full_path = os.path.join(PROJECT_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def remove_file(rel_path):
    """Remove a file relative to project root."""
    full_path = os.path.join(PROJECT_DIR, rel_path)
    if os.path.exists(full_path):
        os.remove(full_path)


# ==================================================================
# FILE CONTENTS — organized by commit stage
# ==================================================================

GITIGNORE = """__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/
venv/
.venv/
.env
*.log
.pytest_cache/
"""

REQUIREMENTS_V1 = "flask==3.1.0\n"
REQUIREMENTS_V2 = "flask==3.1.0\npytest==8.3.4\n"

README_V1 = """# TaskFlow — Task Manager API

A lightweight REST API for managing personal tasks, built with Python and Flask.

## Product Vision

**TaskFlow** enables users to create, view, update, delete, and filter personal tasks through a clean REST interface for simple productivity tracking.
"""

README_V2 = """# TaskFlow — Task Manager API

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
"""

README_V3 = """# TaskFlow — Task Manager API

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
| GET | `/tasks` | List all tasks (US2) |
| PUT | `/tasks/<id>` | Update a task (US3) |
"""

README_V4 = """# TaskFlow — Task Manager API

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
"""

# ── Sprint 0: Planning Documents ────────────────────────────────

SPRINT0_VISION = """# Sprint 0: Planning

## 1. Product Vision

**TaskFlow** is a lightweight task management API that allows users to create, view, update, delete, and filter personal tasks — enabling simple and efficient productivity tracking through a clean REST interface.
"""

SPRINT0_BACKLOG = """# Sprint 0: Planning

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
"""

SPRINT0_AC_US1_US2 = """
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
"""

SPRINT0_AC_US3_US4 = """
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
"""

SPRINT0_AC_US5_US6 = """
### US5 — Filter Tasks by Status
- **Given** tasks exist with various statuses,
- **When** I send a GET request to `/tasks?status=done`,
- **Then** the API returns `200 OK` with only the tasks matching that status.
- **And** if the status value is invalid, the API returns `400 Bad Request`.

### US6 — Health Check
- **Given** the service is running,
- **When** I send a GET request to `/health`,
- **Then** the API returns `200 OK` with `{"status": "healthy", "timestamp": "<ISO-8601>", "task_count": <int>}`.
"""

SPRINT0_DOD = """
---

## 4. Definition of Done (DoD)

A user story is considered **Done** when ALL of the following are met:

1. **Code Complete**: Feature code is written and implements all acceptance criteria.
2. **Tests Written**: Unit tests cover the feature and all pass.
3. **CI Pipeline Passes**: The code passes linting and all tests in the CI/CD pipeline.
4. **Code Committed**: Changes are committed to the `main` branch with clear, descriptive commit messages.
5. **Documentation Updated**: Any relevant docs (README, API docs) are updated.
6. **Peer-Reviewable**: Code is clean, readable, and follows project conventions.
"""

SPRINT0_SPRINT1_PLAN = """
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
"""

SPRINT0_SPRINT2_PLAN = """
---

## 6. Sprint 2 Plan (Tentative)

**Sprint Goal**: Add delete and filter functionality, implement monitoring/logging, and apply Sprint 1 retrospective improvements.

| Story | Story Points |
|-------|-------------|
| US4 — Delete a Task | 2 |
| US5 — Filter Tasks by Status | 3 |
| US6 — Health Check | 1 |

**Total Planned Points**: 6
"""

# ── Sprint 1: Application Code ──────────────────────────────────

APP_V1_SKELETON = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V2_CREATE = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing.
    """
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"],
        "description": data.get("description", ""),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V3_CREATE_VALIDATION = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V4_GET_TASKS = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    return jsonify(list(tasks.values())), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V5_UPDATE_BASIC = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    US3: Update an existing task.

    Role: As a user
    Action: I want to update a task's title, description, or status
    Value: So that I can reflect changes or progress on my tasks

    Returns: 200 OK with updated task, 404 if not found, 400 if invalid.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task = tasks[task_id]

    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    tasks[task_id] = task
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V6_UPDATE_STATUS = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    US3: Update an existing task.

    Role: As a user
    Action: I want to update a task's title, description, or status
    Value: So that I can reflect changes or progress on my tasks

    Returns: 200 OK with updated task, 404 if not found, 400 if invalid.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task = tasks[task_id]

    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
            }), 400
        task["status"] = data["status"]

    tasks[task_id] = task
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V7_UPDATE_TIMESTAMP = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    US3: Update an existing task.

    Role: As a user
    Action: I want to update a task's title, description, or status
    Value: So that I can reflect changes or progress on my tasks

    Returns: 200 OK with updated task, 404 if not found, 400 if invalid.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task = tasks[task_id]

    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
            }), 400
        task["status"] = data["status"]

    task["updated_at"] = datetime.now(timezone.utc).isoformat()
    tasks[task_id] = task
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

# ── Sprint 1: Tests ─────────────────────────────────────────────

TESTS_V1_FIXTURES = '''"""
Unit tests for the TaskFlow API.
"""

import pytest
from app import app, tasks


@pytest.fixture
def client():
    """Create a fresh test client for each test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def _create_task(client, title="Test Task", description=""):
    """Helper to create a task and return its JSON."""
    resp = client.post("/tasks", json={"title": title, "description": description})
    return resp.get_json()
'''

TESTS_V2_US1_HAPPY = '''"""
Unit tests for the TaskFlow API.
"""

import pytest
from app import app, tasks


@pytest.fixture
def client():
    """Create a fresh test client for each test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def _create_task(client, title="Test Task", description=""):
    """Helper to create a task and return its JSON."""
    resp = client.post("/tasks", json={"title": title, "description": description})
    return resp.get_json()


# ── US1: Create a Task ──────────────────────────────────────────


class TestCreateTask:
    """Tests for POST /tasks (US1)."""

    def test_create_task_success(self, client):
        """Creating a task with a valid title returns 201 and the task JSON."""
        tasks.clear()
        response = client.post("/tasks", json={"title": "Buy groceries"})
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Buy groceries"
        assert data["status"] == "pending"
        assert "id" in data
        assert "created_at" in data

    def test_create_task_with_description(self, client):
        """Creating a task with title and description stores both."""
        tasks.clear()
        response = client.post(
            "/tasks",
            json={"title": "Read book", "description": "Chapter 5"},
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data["description"] == "Chapter 5"
'''

TESTS_V3_US1_ERRORS = '''"""
Unit tests for the TaskFlow API.
"""

import pytest
from app import app, tasks


@pytest.fixture
def client():
    """Create a fresh test client for each test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def _create_task(client, title="Test Task", description=""):
    """Helper to create a task and return its JSON."""
    resp = client.post("/tasks", json={"title": title, "description": description})
    return resp.get_json()


# ── US1: Create a Task ──────────────────────────────────────────


class TestCreateTask:
    """Tests for POST /tasks (US1)."""

    def test_create_task_success(self, client):
        """Creating a task with a valid title returns 201 and the task JSON."""
        tasks.clear()
        response = client.post("/tasks", json={"title": "Buy groceries"})
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Buy groceries"
        assert data["status"] == "pending"
        assert "id" in data
        assert "created_at" in data

    def test_create_task_with_description(self, client):
        """Creating a task with title and description stores both."""
        tasks.clear()
        response = client.post(
            "/tasks",
            json={"title": "Read book", "description": "Chapter 5"},
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data["description"] == "Chapter 5"

    def test_create_task_missing_title(self, client):
        """Creating a task without a title returns 400."""
        tasks.clear()
        response = client.post("/tasks", json={"description": "No title"})
        assert response.status_code == 400
        assert "error" in response.get_json()

    def test_create_task_empty_title(self, client):
        """Creating a task with an empty title returns 400."""
        tasks.clear()
        response = client.post("/tasks", json={"title": "   "})
        assert response.status_code == 400

    def test_create_task_no_body(self, client):
        """Creating a task with no JSON body returns 400."""
        tasks.clear()
        response = client.post("/tasks", content_type="application/json")
        assert response.status_code == 400
'''

TESTS_V4_US2_EMPTY = '''

# ── US2: View All Tasks ─────────────────────────────────────────


class TestGetTasks:
    """Tests for GET /tasks (US2)."""

    def test_get_tasks_empty(self, client):
        """When no tasks exist, returns an empty list."""
        tasks.clear()
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.get_json() == []
'''

TESTS_V5_US2_AFTER_CREATE = '''
    def test_get_tasks_after_creation(self, client):
        """After creating tasks, they all appear in the list."""
        tasks.clear()
        client.post("/tasks", json={"title": "Task 1"})
        client.post("/tasks", json={"title": "Task 2"})
        response = client.get("/tasks")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 2
        titles = {t["title"] for t in data}
        assert titles == {"Task 1", "Task 2"}
'''

TESTS_V6_US3_HAPPY = '''

# ── US3: Update a Task ──────────────────────────────────────────


class TestUpdateTask:
    """Tests for PUT /tasks/<id> (US3)."""

    def test_update_title(self, client):
        """Updating the title works correctly."""
        tasks.clear()
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.get_json()["title"] == "Updated"

    def test_update_status(self, client):
        """Updating the status to a valid value works."""
        tasks.clear()
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"status": "done"})
        assert response.status_code == 200
        assert response.get_json()["status"] == "done"
'''

TESTS_V7_US3_ERRORS = '''
    def test_update_invalid_status(self, client):
        """Updating with an invalid status returns 400."""
        tasks.clear()
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"status": "invalid"})
        assert response.status_code == 400

    def test_update_nonexistent_task(self, client):
        """Updating a task that doesn\\'t exist returns 404."""
        tasks.clear()
        response = client.put("/tasks/nonexistent", json={"title": "X"})
        assert response.status_code == 404

    def test_update_empty_title(self, client):
        """Updating with an empty title returns 400."""
        tasks.clear()
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"title": "  "})
        assert response.status_code == 400
'''

TESTS_V8_US3_TIMESTAMP = '''
    def test_update_adds_timestamp(self, client):
        """Updating a task adds an updated_at timestamp."""
        tasks.clear()
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"title": "New"})
        assert "updated_at" in response.get_json()
'''

# ── Sprint 2: Logging additions to app.py ───────────────────────

APP_V8_LOGGING_SETUP = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
import logging
from datetime import datetime, timezone

# ── Logging Setup (Sprint 2 Retro Improvement #1) ───────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("taskflow")

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    US3: Update an existing task.

    Role: As a user
    Action: I want to update a task's title, description, or status
    Value: So that I can reflect changes or progress on my tasks

    Returns: 200 OK with updated task, 404 if not found, 400 if invalid.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task = tasks[task_id]

    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
            }), 400
        task["status"] = data["status"]

    task["updated_at"] = datetime.now(timezone.utc).isoformat()
    tasks[task_id] = task
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V9_LOGGING_CREATE_GET = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
import logging
from datetime import datetime, timezone

# ── Logging Setup (Sprint 2 Retro Improvement #1) ───────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("taskflow")

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        logger.warning("POST /tasks — rejected: missing or empty title")
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    logger.info("POST /tasks — created task %s: '%s'", task_id, task["title"])
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    logger.info("GET /tasks — returning %d tasks", len(tasks))
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    US3: Update an existing task.

    Role: As a user
    Action: I want to update a task's title, description, or status
    Value: So that I can reflect changes or progress on my tasks

    Returns: 200 OK with updated task, 404 if not found, 400 if invalid.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task = tasks[task_id]

    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
            }), 400
        task["status"] = data["status"]

    task["updated_at"] = datetime.now(timezone.utc).isoformat()
    tasks[task_id] = task
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

APP_V10_LOGGING_UPDATE = '''"""
TaskFlow — A lightweight Task Manager REST API.
Built with Flask for the Agile & DevOps assessment.
"""

from flask import Flask, jsonify, request
import uuid
import logging
from datetime import datetime, timezone

# ── Logging Setup (Sprint 2 Retro Improvement #1) ───────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("taskflow")

app = Flask(__name__)

# In-memory task storage
tasks = {}

VALID_STATUSES = {"pending", "in-progress", "done"}


@app.route("/tasks", methods=["POST"])
def create_task():
    """
    US1: Create a new task.

    Role: As a user
    Action: I want to create a new task with a title and optional description
    Value: So that I can track things I need to do

    Expects JSON: {"title": "...", "description": "..."}
    Returns: 201 Created with task JSON, or 400 if title missing/empty.
    """
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        logger.warning("POST /tasks — rejected: missing or empty title")
        return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks[task_id] = task
    logger.info("POST /tasks — created task %s: '%s'", task_id, task["title"])
    return jsonify(task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    logger.info("GET /tasks — returning %d tasks", len(tasks))
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    """
    US3: Update an existing task.

    Role: As a user
    Action: I want to update a task's title, description, or status
    Value: So that I can reflect changes or progress on my tasks

    Returns: 200 OK with updated task, 404 if not found, 400 if invalid.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    task = tasks[task_id]

    if "title" in data:
        if not data["title"].strip():
            return jsonify({"error": "Title cannot be empty"}), 400
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    if "status" in data:
        if data["status"] not in VALID_STATUSES:
            return jsonify({
                "error": f"Invalid status. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
            }), 400
        task["status"] = data["status"]

    task["updated_at"] = datetime.now(timezone.utc).isoformat()
    tasks[task_id] = task
    logger.info("PUT /tasks/%s — task updated", task_id)
    return jsonify(task), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
'''

# ── Sprint 2: Test isolation ────────────────────────────────────

TESTS_ISOLATION_HEADER = '''"""
Unit tests for the TaskFlow API — Sprint 1 + Sprint 2.
Covers US1 (Create), US2 (View), US3 (Update), US4 (Delete),
US5 (Filter by Status), US6 (Health Check).

Sprint 2 Retro Improvement #2: Each test uses a fresh app instance
via the autouse clean_tasks fixture to ensure full test isolation.
"""

import pytest
from app import app, tasks


@pytest.fixture(autouse=True)
def clean_tasks():
    """Ensure task store is clean before and after every test (isolation)."""
    tasks.clear()
    yield
    tasks.clear()


@pytest.fixture
def client():
    """Create a fresh test client for each test."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def _create_task(client, title="Test Task", description=""):
    """Helper to create a task and return its JSON."""
    resp = client.post("/tasks", json={"title": title, "description": description})
    return resp.get_json()


# ── US1: Create a Task ──────────────────────────────────────────


class TestCreateTask:
    """Tests for POST /tasks (US1)."""

    def test_create_task_success(self, client):
        """Creating a task with a valid title returns 201 and the task JSON."""
        response = client.post("/tasks", json={"title": "Buy groceries"})
        assert response.status_code == 201
        data = response.get_json()
        assert data["title"] == "Buy groceries"
        assert data["status"] == "pending"
        assert "id" in data
        assert "created_at" in data

    def test_create_task_with_description(self, client):
        """Creating a task with title and description stores both."""
        response = client.post(
            "/tasks",
            json={"title": "Read book", "description": "Chapter 5"},
        )
        assert response.status_code == 201
        data = response.get_json()
        assert data["description"] == "Chapter 5"

    def test_create_task_missing_title(self, client):
        """Creating a task without a title returns 400."""
        response = client.post("/tasks", json={"description": "No title"})
        assert response.status_code == 400
        assert "error" in response.get_json()

    def test_create_task_empty_title(self, client):
        """Creating a task with an empty title returns 400."""
        response = client.post("/tasks", json={"title": "   "})
        assert response.status_code == 400

    def test_create_task_no_body(self, client):
        """Creating a task with no JSON body returns 400."""
        response = client.post("/tasks", content_type="application/json")
        assert response.status_code == 400


# ── US2: View All Tasks ─────────────────────────────────────────


class TestGetTasks:
    """Tests for GET /tasks (US2)."""

    def test_get_tasks_empty(self, client):
        """When no tasks exist, returns an empty list."""
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.get_json() == []

    def test_get_tasks_after_creation(self, client):
        """After creating tasks, they all appear in the list."""
        client.post("/tasks", json={"title": "Task 1"})
        client.post("/tasks", json={"title": "Task 2"})
        response = client.get("/tasks")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 2
        titles = {t["title"] for t in data}
        assert titles == {"Task 1", "Task 2"}


# ── US3: Update a Task ──────────────────────────────────────────


class TestUpdateTask:
    """Tests for PUT /tasks/<id> (US3)."""

    def test_update_title(self, client):
        """Updating the title works correctly."""
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"title": "Updated"})
        assert response.status_code == 200
        assert response.get_json()["title"] == "Updated"

    def test_update_status(self, client):
        """Updating the status to a valid value works."""
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"status": "done"})
        assert response.status_code == 200
        assert response.get_json()["status"] == "done"

    def test_update_invalid_status(self, client):
        """Updating with an invalid status returns 400."""
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"status": "invalid"})
        assert response.status_code == 400

    def test_update_nonexistent_task(self, client):
        """Updating a task that doesn't exist returns 404."""
        response = client.put("/tasks/nonexistent", json={"title": "X"})
        assert response.status_code == 404

    def test_update_empty_title(self, client):
        """Updating with an empty title returns 400."""
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"title": "  "})
        assert response.status_code == 400

    def test_update_adds_timestamp(self, client):
        """Updating a task adds an updated_at timestamp."""
        task = _create_task(client)
        response = client.put(f"/tasks/{task['id']}", json={"title": "New"})
        assert "updated_at" in response.get_json()
'''

# ── Sprint 2: US4 - Delete ──────────────────────────────────────

APP_V11_DELETE = '''

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    US4: Delete a task.

    Role: As a user
    Action: I want to delete a task by its ID
    Value: So that I can remove items I no longer need to track

    Returns: 200 OK with confirmation, or 404 if not found.
    """
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    deleted_title = tasks[task_id]["title"]
    del tasks[task_id]
    return jsonify({"message": f"Task '{deleted_title}' deleted successfully"}), 200
'''

APP_V12_DELETE_LOGGING = '''

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    US4: Delete a task.

    Role: As a user
    Action: I want to delete a task by its ID
    Value: So that I can remove items I no longer need to track

    Returns: 200 OK with confirmation, or 404 if not found.
    """
    if task_id not in tasks:
        logger.warning("DELETE /tasks/%s — not found", task_id)
        return jsonify({"error": "Task not found"}), 404

    deleted_title = tasks[task_id]["title"]
    del tasks[task_id]
    logger.info("DELETE /tasks/%s — deleted task '%s'", task_id, deleted_title)
    return jsonify({"message": f"Task '{deleted_title}' deleted successfully"}), 200
'''

TESTS_US4_SUCCESS = '''

# ── US4: Delete a Task ──────────────────────────────────────────


class TestDeleteTask:
    """Tests for DELETE /tasks/<id> (US4)."""

    def test_delete_task_success(self, client):
        """Deleting an existing task returns 200 and confirmation."""
        task = _create_task(client, title="To delete")
        response = client.delete(f"/tasks/{task['id']}")
        assert response.status_code == 200
        assert "deleted successfully" in response.get_json()["message"]

    def test_delete_task_removes_from_list(self, client):
        """After deletion, the task no longer appears in GET /tasks."""
        task = _create_task(client, title="Temporary")
        client.delete(f"/tasks/{task['id']}")
        response = client.get("/tasks")
        assert len(response.get_json()) == 0
'''

TESTS_US4_404 = '''
    def test_delete_nonexistent_task(self, client):
        """Deleting a non-existent task returns 404."""
        response = client.delete("/tasks/nonexistent-id")
        assert response.status_code == 404
        assert "error" in response.get_json()
'''

# ── Sprint 2: US5 - Filter ──────────────────────────────────────

# This replaces the get_tasks function to add filter support
APP_GET_TASKS_WITH_FILTER = '''
@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks. US5: Filter by status.

    Role: As a user
    Action: I want to view all my tasks, optionally filtered by status
    Value: So that I can see everything or focus on what matters

    Query params: ?status=pending|in-progress|done
    Returns: 200 OK with JSON array of tasks.
    """
    status_filter = request.args.get("status")

    if status_filter:
        if status_filter not in VALID_STATUSES:
            logger.warning("GET /tasks — rejected: invalid status filter '%s'", status_filter)
            return jsonify({
                "error": f"Invalid status filter. Must be one of: {', '.join(sorted(VALID_STATUSES))}"
            }), 400
        filtered = [t for t in tasks.values() if t["status"] == status_filter]
        logger.info("GET /tasks?status=%s — returning %d tasks", status_filter, len(filtered))
        return jsonify(filtered), 200

    logger.info("GET /tasks — returning %d tasks", len(tasks))
    return jsonify(list(tasks.values())), 200
'''

TESTS_US5_FILTER = '''

# ── US5: Filter Tasks by Status ─────────────────────────────────


class TestFilterTasks:
    """Tests for GET /tasks?status=<status> (US5)."""

    def test_filter_by_status(self, client):
        """Filtering returns only tasks with the matching status."""
        _create_task(client, title="Pending task")
        task2 = _create_task(client, title="Done task")
        # Mark task2 as done
        client.put(f"/tasks/{task2['id']}", json={"status": "done"})

        response = client.get("/tasks?status=done")
        assert response.status_code == 200
        data = response.get_json()
        assert len(data) == 1
        assert data[0]["title"] == "Done task"

    def test_filter_pending(self, client):
        """Filtering by 'pending' returns only pending tasks."""
        _create_task(client, title="Task A")
        _create_task(client, title="Task B")
        response = client.get("/tasks?status=pending")
        assert response.status_code == 200
        assert len(response.get_json()) == 2
'''

TESTS_US5_ERRORS = '''
    def test_filter_invalid_status(self, client):
        """Filtering by an invalid status returns 400."""
        response = client.get("/tasks?status=banana")
        assert response.status_code == 400
        assert "error" in response.get_json()

    def test_filter_returns_empty_when_no_match(self, client):
        """Filtering returns an empty list when no tasks match."""
        _create_task(client, title="Pending one")
        response = client.get("/tasks?status=done")
        assert response.status_code == 200
        assert response.get_json() == []
'''

# ── Sprint 2: US6 - Health Check ────────────────────────────────

APP_V13_HEALTH = '''

@app.route("/health", methods=["GET"])
def health_check():
    """
    US6: Health check endpoint.

    Role: As a user (or operations team)
    Action: I want to check if the service is running
    Value: So that I can verify the API is healthy before making requests

    Returns: 200 OK with health status, timestamp, and task count.
    """
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task_count": len(tasks),
    }), 200
'''

TESTS_US6 = '''

# ── US6: Health Check ────────────────────────────────────────────


class TestHealthCheck:
    """Tests for GET /health (US6)."""

    def test_health_check(self, client):
        """Health endpoint returns 200 with status and timestamp."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.get_json()
        assert data["status"] == "healthy"
        assert "timestamp" in data

    def test_health_check_includes_task_count(self, client):
        """Health endpoint includes the current task count."""
        _create_task(client, title="A task")
        response = client.get("/health")
        data = response.get_json()
        assert data["task_count"] == 1
'''

APP_V14_HEALTH_LOGGING = '''

@app.route("/health", methods=["GET"])
def health_check():
    """
    US6: Health check endpoint.

    Role: As a user (or operations team)
    Action: I want to check if the service is running
    Value: So that I can verify the API is healthy before making requests

    Returns: 200 OK with health status, timestamp, and task count.
    """
    logger.info("GET /health — service is healthy")
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task_count": len(tasks),
    }), 200
'''

# ── Sprint 1 Docs ───────────────────────────────────────────────

SPRINT1_REVIEW_SUMMARY = """# Sprint 1 Review

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
"""

SPRINT1_REVIEW_DETAILS = """
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
curl -X POST http://localhost:5000/tasks \\
  -H "Content-Type: application/json" \\
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
"""

SPRINT1_RETRO = """# Sprint 1 Retrospective

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
"""

SPRINT2_REVIEW_SUMMARY = """# Sprint 2 Review

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
"""

SPRINT2_REVIEW_DETAILS = """
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
"""

SPRINT2_RETRO = """# Sprint 2 Retrospective (Final)

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
"""

# ── CI/CD Pipeline ───────────────────────────────────────────────

CI_YML_BASIC = """name: TaskFlow CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    name: Lint & Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
"""

CI_YML_FULL = """name: TaskFlow CI Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    name: Lint & Test
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python -m pytest tests/ -v --tb=short
"""

# ── Consolidated Documentation ──────────────────────────────────

CONSOLIDATED_DOCS = """# TaskFlow — Consolidated Project Documentation

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
"""

CONTRIBUTING_MD = """# Contributing to TaskFlow

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate: `venv\\Scripts\\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`

## Running Tests

```bash
pytest tests/ -v
```

## Code Style

- Use clear, descriptive function and variable names
- Add docstrings to all public functions
- Follow PEP 8 conventions

## Commit Guidelines

- One logical change per commit
- Use clear, descriptive commit messages
- Reference the user story ID in the commit message (e.g., "US1: ...")

## Branch Strategy

- `main` is the primary branch
- All changes go through CI before merging
"""


# ==================================================================
# COMMIT SEQUENCE — 55 commits
# ==================================================================

def build_all_commits():
    """Return the ordered list of (message, date, actions) tuples."""
    commits = []

    def dt(base, **kwargs):
        return base + timedelta(**kwargs)

    # ── Sprint 0: Planning (commits 1-12) ────────────────────────
    s0 = SPRINT0_START

    commits.append((
        "Sprint 0: Initialize project with .gitignore",
        dt(s0, hours=0),
        lambda: write_file(".gitignore", GITIGNORE),
    ))

    commits.append((
        "Sprint 0: Add Flask dependency to requirements.txt",
        dt(s0, hours=1),
        lambda: write_file("requirements.txt", REQUIREMENTS_V1),
    ))

    commits.append((
        "Sprint 0: Add pytest dependency to requirements.txt",
        dt(s0, hours=2),
        lambda: write_file("requirements.txt", REQUIREMENTS_V2),
    ))

    commits.append((
        "Sprint 0: Create initial README with product vision",
        dt(s0, hours=3),
        lambda: write_file("README.md", README_V1),
    ))

    commits.append((
        "Sprint 0: Add product vision to sprint planning doc",
        dt(s0, hours=5),
        lambda: write_file("docs/sprint0_planning.md", SPRINT0_VISION),
    ))

    commits.append((
        "Sprint 0: Add product backlog with user stories (role/action/value)",
        dt(s0, days=1, hours=0),
        lambda: write_file("docs/sprint0_planning.md", SPRINT0_BACKLOG),
    ))

    commits.append((
        "Sprint 0: Add acceptance criteria for US1 and US2",
        dt(s0, days=1, hours=2),
        lambda: (
            write_file("docs/sprint0_planning.md",
                        SPRINT0_BACKLOG + SPRINT0_AC_US1_US2)
        ),
    ))

    commits.append((
        "Sprint 0: Add acceptance criteria for US3 and US4",
        dt(s0, days=1, hours=3),
        lambda: (
            write_file("docs/sprint0_planning.md",
                        SPRINT0_BACKLOG + SPRINT0_AC_US1_US2 + SPRINT0_AC_US3_US4)
        ),
    ))

    commits.append((
        "Sprint 0: Add acceptance criteria for US5 and US6",
        dt(s0, days=1, hours=4),
        lambda: (
            write_file("docs/sprint0_planning.md",
                        SPRINT0_BACKLOG + SPRINT0_AC_US1_US2 + SPRINT0_AC_US3_US4 + SPRINT0_AC_US5_US6)
        ),
    ))

    commits.append((
        "Sprint 0: Add Definition of Done (DoD)",
        dt(s0, days=2, hours=0),
        lambda: (
            write_file("docs/sprint0_planning.md",
                        SPRINT0_BACKLOG + SPRINT0_AC_US1_US2 + SPRINT0_AC_US3_US4 + SPRINT0_AC_US5_US6 + SPRINT0_DOD)
        ),
    ))

    commits.append((
        "Sprint 0: Add Sprint 1 plan to planning document",
        dt(s0, days=2, hours=1),
        lambda: (
            write_file("docs/sprint0_planning.md",
                        SPRINT0_BACKLOG + SPRINT0_AC_US1_US2 + SPRINT0_AC_US3_US4 + SPRINT0_AC_US5_US6 + SPRINT0_DOD + SPRINT0_SPRINT1_PLAN)
        ),
    ))

    commits.append((
        "Sprint 0: Add tentative Sprint 2 plan",
        dt(s0, days=2, hours=2),
        lambda: (
            write_file("docs/sprint0_planning.md",
                        SPRINT0_BACKLOG + SPRINT0_AC_US1_US2 + SPRINT0_AC_US3_US4 + SPRINT0_AC_US5_US6 + SPRINT0_DOD + SPRINT0_SPRINT1_PLAN + SPRINT0_SPRINT2_PLAN)
        ),
    ))

    # ── Sprint 1: US1 (commits 13-18) ───────────────────────────
    s1 = SPRINT1_START

    commits.append((
        "Sprint 1: Create Flask app skeleton with imports and config",
        dt(s1, hours=0),
        lambda: write_file("app.py", APP_V1_SKELETON),
    ))

    commits.append((
        "Sprint 1: Implement POST /tasks endpoint (US1 - create task)",
        dt(s1, hours=2),
        lambda: write_file("app.py", APP_V2_CREATE),
    ))

    commits.append((
        "Sprint 1: Add title validation and input stripping to create task",
        dt(s1, hours=3),
        lambda: write_file("app.py", APP_V3_CREATE_VALIDATION),
    ))

    commits.append((
        "Sprint 1: Add test fixtures and helper function for test suite",
        dt(s1, hours=5),
        lambda: write_file("tests/test_app.py", TESTS_V1_FIXTURES),
    ))

    commits.append((
        "Sprint 1: Add US1 tests - create task success and with description",
        dt(s1, hours=6),
        lambda: write_file("tests/test_app.py", TESTS_V2_US1_HAPPY),
    ))

    commits.append((
        "Sprint 1: Add US1 tests - missing title, empty title, no body errors",
        dt(s1, hours=7),
        lambda: write_file("tests/test_app.py", TESTS_V3_US1_ERRORS),
    ))

    # ── Sprint 1: US2 (commits 19-22) ───────────────────────────

    commits.append((
        "Sprint 1: Implement GET /tasks endpoint (US2 - view all tasks)",
        dt(s1, days=1, hours=0),
        lambda: write_file("app.py", APP_V4_GET_TASKS),
    ))

    def _add_us2_empty_test():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_V4_US2_EMPTY
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 1: Add US2 test - get tasks returns empty list",
        dt(s1, days=1, hours=1),
        _add_us2_empty_test,
    ))

    def _add_us2_after_create_test():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_V5_US2_AFTER_CREATE
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 1: Add US2 test - get tasks after creation returns all",
        dt(s1, days=1, hours=2),
        _add_us2_after_create_test,
    ))

    commits.append((
        "Sprint 1: Update README with getting started and US1/US2 API docs",
        dt(s1, days=1, hours=3),
        lambda: write_file("README.md", README_V2),
    ))

    # ── Sprint 1: US3 (commits 23-28) ───────────────────────────

    commits.append((
        "Sprint 1: Implement PUT /tasks/<id> basic update (US3)",
        dt(s1, days=2, hours=0),
        lambda: write_file("app.py", APP_V5_UPDATE_BASIC),
    ))

    commits.append((
        "Sprint 1: Add status validation to update endpoint",
        dt(s1, days=2, hours=1),
        lambda: write_file("app.py", APP_V6_UPDATE_STATUS),
    ))

    commits.append((
        "Sprint 1: Add updated_at timestamp on task update",
        dt(s1, days=2, hours=2),
        lambda: write_file("app.py", APP_V7_UPDATE_TIMESTAMP),
    ))

    def _add_us3_happy_tests():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_V6_US3_HAPPY
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 1: Add US3 tests - update title and status success",
        dt(s1, days=2, hours=3),
        _add_us3_happy_tests,
    ))

    def _add_us3_error_tests():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_V7_US3_ERRORS
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 1: Add US3 tests - invalid status, 404, empty title errors",
        dt(s1, days=2, hours=4),
        _add_us3_error_tests,
    ))

    def _add_us3_timestamp_test():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_V8_US3_TIMESTAMP
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 1: Add US3 test - verify updated_at timestamp is added",
        dt(s1, days=2, hours=5),
        _add_us3_timestamp_test,
    ))

    # ── Sprint 1: CI/CD (commits 29-31) ─────────────────────────

    commits.append((
        "Sprint 1: Create GitHub Actions CI workflow - checkout and setup",
        dt(s1, days=3, hours=0),
        lambda: write_file(".github/workflows/ci.yml", CI_YML_BASIC),
    ))

    commits.append((
        "Sprint 1: Add test execution step to CI pipeline",
        dt(s1, days=3, hours=1),
        lambda: write_file(".github/workflows/ci.yml", CI_YML_FULL),
    ))

    commits.append((
        "Sprint 1: Update README with CI info and project structure",
        dt(s1, days=3, hours=2),
        lambda: write_file("README.md", README_V3),
    ))

    # ── Sprint 1: Docs (commits 32-34) ──────────────────────────

    commits.append((
        "Sprint 1: Create sprint 1 review - summary and backlog",
        dt(s1, days=10, hours=0),
        lambda: write_file("docs/sprint1_review.md", SPRINT1_REVIEW_SUMMARY),
    ))

    commits.append((
        "Sprint 1: Add delivery details, testing summary to sprint 1 review",
        dt(s1, days=10, hours=1),
        lambda: write_file("docs/sprint1_review.md",
                            SPRINT1_REVIEW_SUMMARY + SPRINT1_REVIEW_DETAILS),
    ))

    commits.append((
        "Sprint 1: Create sprint 1 retrospective document",
        dt(s1, days=10, hours=2),
        lambda: write_file("docs/sprint1_retrospective.md", SPRINT1_RETRO),
    ))

    # ── Sprint 2: Improvements (commits 35-38) ──────────────────
    s2 = SPRINT2_START

    commits.append((
        "Sprint 2: Add structured logging module setup (retro improvement #1)",
        dt(s2, hours=0),
        lambda: write_file("app.py", APP_V8_LOGGING_SETUP),
    ))

    commits.append((
        "Sprint 2: Add logging to POST /tasks and GET /tasks endpoints",
        dt(s2, hours=1),
        lambda: write_file("app.py", APP_V9_LOGGING_CREATE_GET),
    ))

    commits.append((
        "Sprint 2: Add logging to PUT /tasks endpoint",
        dt(s2, hours=2),
        lambda: write_file("app.py", APP_V10_LOGGING_UPDATE),
    ))

    commits.append((
        "Sprint 2: Add autouse clean_tasks fixture for test isolation (retro #2)",
        dt(s2, hours=3),
        lambda: write_file("tests/test_app.py", TESTS_ISOLATION_HEADER),
    ))

    # ── Sprint 2: US4 (commits 39-42) ───────────────────────────

    def _add_delete_endpoint():
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        # Insert before "if __name__"
        content = content.replace(
            '\nif __name__ == "__main__":',
            APP_V11_DELETE + '\nif __name__ == "__main__":'
        )
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Implement DELETE /tasks/<id> endpoint (US4)",
        dt(s2, days=1, hours=0),
        _add_delete_endpoint,
    ))

    def _add_delete_logging():
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        content = content.replace(APP_V11_DELETE, APP_V12_DELETE_LOGGING)
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Add logging to DELETE endpoint",
        dt(s2, days=1, hours=1),
        _add_delete_logging,
    ))

    def _add_us4_success_tests():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_US4_SUCCESS
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 2: Add US4 tests - delete success and removes from list",
        dt(s2, days=1, hours=2),
        _add_us4_success_tests,
    ))

    def _add_us4_404_test():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_US4_404
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 2: Add US4 test - delete non-existent task returns 404",
        dt(s2, days=1, hours=3),
        _add_us4_404_test,
    ))

    # ── Sprint 2: US5 (commits 43-47) ───────────────────────────

    def _update_get_tasks_with_filter():
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        # Replace the existing get_tasks function
        old_get_tasks = '''
@app.route("/tasks", methods=["GET"])
def get_tasks():
    """
    US2: View all tasks.

    Role: As a user
    Action: I want to view all my tasks in a list
    Value: So that I can see everything on my plate at a glance

    Returns: 200 OK with JSON array of all tasks.
    """
    logger.info("GET /tasks — returning %d tasks", len(tasks))
    return jsonify(list(tasks.values())), 200'''
        content = content.replace(old_get_tasks, APP_GET_TASKS_WITH_FILTER)
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Add status filter query parameter to GET /tasks (US5)",
        dt(s2, days=2, hours=0),
        _update_get_tasks_with_filter,
    ))

    def _add_filter_validation():
        # This is already done in the filter function, so just a doc improvement
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        # Add a comment about valid statuses near the top
        content = content.replace(
            'VALID_STATUSES = {"pending", "in-progress", "done"}',
            '# Valid task statuses for creation, update, and filtering\nVALID_STATUSES = {"pending", "in-progress", "done"}'
        )
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Add documentation comment for valid statuses constant",
        dt(s2, days=2, hours=1),
        _add_filter_validation,
    ))

    def _add_us5_filter_tests():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_US5_FILTER
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 2: Add US5 tests - filter by done and pending status",
        dt(s2, days=2, hours=2),
        _add_us5_filter_tests,
    ))

    def _add_us5_error_tests():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_US5_ERRORS
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 2: Add US5 tests - invalid status filter and empty results",
        dt(s2, days=2, hours=3),
        _add_us5_error_tests,
    ))

    commits.append((
        "Sprint 2: Update README with complete API endpoint documentation",
        dt(s2, days=2, hours=4),
        lambda: write_file("README.md", README_V4),
    ))

    # ── Sprint 2: US6 (commits 48-50) ───────────────────────────

    def _add_health_endpoint():
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        content = content.replace(
            '\nif __name__ == "__main__":',
            APP_V13_HEALTH + '\nif __name__ == "__main__":'
        )
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Implement GET /health endpoint (US6)",
        dt(s2, days=3, hours=0),
        _add_health_endpoint,
    ))

    def _add_us6_tests():
        content = open(os.path.join(PROJECT_DIR, "tests/test_app.py"), "r", encoding="utf-8").read()
        content += TESTS_US6
        write_file("tests/test_app.py", content)

    commits.append((
        "Sprint 2: Add US6 tests - health check status and task count",
        dt(s2, days=3, hours=1),
        _add_us6_tests,
    ))

    def _add_health_logging():
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        content = content.replace(APP_V13_HEALTH, APP_V14_HEALTH_LOGGING)
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Add logging to health check endpoint",
        dt(s2, days=3, hours=2),
        _add_health_logging,
    ))

    def _add_main_logging():
        content = open(os.path.join(PROJECT_DIR, "app.py"), "r", encoding="utf-8").read()
        content = content.replace(
            'if __name__ == "__main__":\n    app.run(debug=True, port=5000)',
            'if __name__ == "__main__":\n    logger.info("Starting TaskFlow API on port 5000")\n    app.run(debug=True, port=5000)'
        )
        write_file("app.py", content)

    commits.append((
        "Sprint 2: Add startup log message to main entry point",
        dt(s2, days=3, hours=3),
        _add_main_logging,
    ))

    # ── Sprint 2: Final Docs (commits 52-55) ────────────────────

    commits.append((
        "Sprint 2: Create sprint 2 review - summary and retro improvements",
        dt(s2, days=13, hours=0),
        lambda: write_file("docs/sprint2_review.md", SPRINT2_REVIEW_SUMMARY),
    ))

    commits.append((
        "Sprint 2: Add delivery details and testing summary to sprint 2 review",
        dt(s2, days=13, hours=1),
        lambda: write_file("docs/sprint2_review.md",
                            SPRINT2_REVIEW_SUMMARY + SPRINT2_REVIEW_DETAILS),
    ))

    commits.append((
        "Sprint 2: Create sprint 2 retrospective (final) document",
        dt(s2, days=13, hours=2),
        lambda: write_file("docs/sprint2_retrospective.md", SPRINT2_RETRO),
    ))

    commits.append((
        "Sprint 2: Add consolidated project documentation",
        dt(s2, days=13, hours=3),
        lambda: write_file("docs/PROJECT_DOCUMENTATION.md", CONSOLIDATED_DOCS),
    ))

    commits.append((
        "Sprint 2: Add CONTRIBUTING.md with development guidelines",
        dt(s2, days=13, hours=4),
        lambda: write_file("CONTRIBUTING.md", CONTRIBUTING_MD),
    ))

    return commits


# ==================================================================
# MAIN — Execute the rebuild
# ==================================================================

def main():
    print("=" * 60)
    print("TaskFlow Git History Rebuild")
    print("=" * 60)
    print(f"Project: {PROJECT_DIR}")
    print()

    # Step 1: Get remote URL
    remote_url = None
    try:
        remote_url = git("remote", "get-url", "origin")
        print(f"Remote URL: {remote_url}")
    except SystemExit:
        print("No remote found (will skip remote setup)")

    # Step 2: Backup .git
    git_dir = os.path.join(PROJECT_DIR, ".git")
    backup_dir = os.path.join(PROJECT_DIR, ".git_backup")

    if os.path.exists(backup_dir):
        print("Removing old .git_backup...")
        shutil.rmtree(backup_dir, ignore_errors=True)

    print("Backing up .git -> .git_backup...")
    shutil.copytree(git_dir, backup_dir)

    # Step 3: Remove .git and reinitialize
    print("Removing .git...")
    shutil.rmtree(git_dir, ignore_errors=True)

    # Clean up all tracked files (but keep this script and backup)
    for item in os.listdir(PROJECT_DIR):
        if item in (".git_backup", "rebuild_history.py", ".venv", "venv"):
            continue
        full = os.path.join(PROJECT_DIR, item)
        if os.path.isdir(full):
            shutil.rmtree(full, ignore_errors=True)
        else:
            try:
                os.remove(full)
            except Exception:
                pass

    print("Initializing fresh git repo...")
    git("init")
    git("checkout", "-b", "main")

    # Configure author
    git("config", "user.name", AUTHOR_NAME)
    git("config", "user.email", AUTHOR_EMAIL)

    # Step 4: Build commits
    all_commits = build_all_commits()
    print(f"\nCreating {len(all_commits)} commits...\n")

    for i, (msg, date, action) in enumerate(all_commits, 1):
        os.environ["GIT_COMMITTER_DATE"] = date.strftime("%Y-%m-%dT%H:%M:%S")
        os.environ["GIT_AUTHOR_DATE"] = date.strftime("%Y-%m-%dT%H:%M:%S")
        action()
        git("add", "-A")

        # Check if there are changes to commit
        status = git("status", "--porcelain")
        if not status.strip():
            print(f"  [{i:2d}] SKIP (no changes): {msg}")
            continue

        git(
            "-c", f"user.name={AUTHOR_NAME}",
            "-c", f"user.email={AUTHOR_EMAIL}",
            "commit",
            "-m", msg,
            "--date", date.strftime("%Y-%m-%dT%H:%M:%S"),
        )
        print(f"  [{i:2d}] {msg}")

    # Step 5: Re-add remote
    if remote_url:
        print(f"\nAdding remote: {remote_url}")
        git("remote", "add", "origin", remote_url)

    # Step 6: Clean up
    print("\nCleaning up rebuild script...")
    remove_file("rebuild_history.py")
    # Don't commit the removal — user can do final cleanup

    # Summary
    count = git("rev-list", "--count", "HEAD")
    print(f"\n{'=' * 60}")
    print(f"Done! Created {count} commits.")
    print(f"{'=' * 60}")
    print()
    print("Next steps:")
    print("  1. Review: git log --oneline")
    print("  2. Run tests: pytest tests/ -v")
    print("  3. Force push: git push --force origin main")
    print()
    print("Your old .git is saved in .git_backup/")
    print("Delete it when you're satisfied: rmdir /s /q .git_backup")


if __name__ == "__main__":
    main()
