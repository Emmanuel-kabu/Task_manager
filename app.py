"""
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

# Valid task statuses for creation, update, and filtering
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

if __name__ == "__main__":
    app.run(debug=True, port=5000)
