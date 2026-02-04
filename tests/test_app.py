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
