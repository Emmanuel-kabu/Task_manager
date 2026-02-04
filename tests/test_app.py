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
