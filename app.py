"""
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
