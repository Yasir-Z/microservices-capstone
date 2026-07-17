"""
User Service API.

This module manages user profiles, handles service health checks,
and provides endpoints to retrieve, create, and delete user details.
"""

import os
from flask import Flask, jsonify, request
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


@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    """Retrieve the list of users or register a new user."""
    if request.method == 'POST':
        data = request.get_json() or {}
        name = data.get('name')
        email = data.get('email')

        if not name or not email:
            return jsonify({"error": "Name and email are required"}), 400

        # Generate a unique auto-incrementing ID
        new_id = max([u["id"] for u in users], default=0) + 1
        new_user = {"id": new_id, "name": name, "email": email}
        users.append(new_user)
        
        return jsonify(new_user), 201

    # Default to GET behavior
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET', 'DELETE'])
def manage_single_user(user_id):
    """Retrieve or delete a single user's information by their ID."""
    global users
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if request.method == 'DELETE':
        # Re-assign users list excluding the deleted user ID
        users = [u for u in users if u["id"] != user_id]
        return jsonify({"message": f"User {user_id} deleted successfully"}), 200

    # Default to GET behavior
    return jsonify(user)


if __name__ == '__main__':
    # Default to secure 127.0.0.1 for local runs; override to 0.0.0.0 in Docker/K8s
    host_ip = os.getenv('HOST_IP', '127.0.0.1')
    # Default to port 5001, but cast to an integer
    port_num = int(os.getenv('PORT', 5001))

    app.run(host=host_ip, port=port_num)  # nosec B104
