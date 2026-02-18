"""
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

    def test_delete_nonexistent_task(self, client):
        """Deleting a non-existent task returns 404."""
        response = client.delete("/tasks/nonexistent-id")
        assert response.status_code == 404
        assert "error" in response.get_json()


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
