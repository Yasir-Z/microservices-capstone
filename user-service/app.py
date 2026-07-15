"""
User Service API.

This module manages user profiles, handles service health checks,
and provides endpoints to retrieve user details.
"""

from flask import Flask, jsonify

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
    app.run(host='0.0.0.0', port=5001)
