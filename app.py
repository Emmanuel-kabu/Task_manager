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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
