"""
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


# ── US2: View All Tasks ─────────────────────────────────────────


class TestGetTasks:
    """Tests for GET /tasks (US2)."""

    def test_get_tasks_empty(self, client):
        """When no tasks exist, returns an empty list."""
        tasks.clear()
        response = client.get("/tasks")
        assert response.status_code == 200
        assert response.get_json() == []

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
