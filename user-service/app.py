"""
User Service API.

This module manages user profiles, handles service health checks,
and provides endpoints to retrieve user details.
"""

import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load local environment variables from a .env file if it exists
load_dotenv()

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ahmed", "email": "ahmed@example.com"},
    {"id": 2, "name": "Ali", "email": "ali@example.com"}
]


@app.route('/health')
def health():
    """Return the health status of the user service."""
    return jsonify({"status": "ok", "service": "user-service"})


@app.route('/users')
def get_users():
    """Retrieve the list of all registered users."""
    return jsonify(users)


@app.route('/users/<int:user_id>')
def get_user(user_id):
    """Retrieve a single user's information by their ID."""
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    # Default to secure 127.0.0.1 for local runs; override to 0.0.0.0 in Docker/K8s
    host_ip = os.getenv('HOST_IP', '127.0.0.1')
    # Default to port 5001, but cast to an integer
    port_num = int(os.getenv('PORT', 5001))

    app.run(host=host_ip, port=port_num)  # nosec B104
