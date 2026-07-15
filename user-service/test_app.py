"""
Unit tests for the User Service.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client


def test_health_endpoint(client):
    """Test that GET /health returns the correct status."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok", "service": "user-service"}


def test_get_all_users(client):
    """Test retrieving the list of all registered users."""
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]["name"] == "Ahmed"


def test_get_user_success(client):
    """Test retrieving a single user by their correct ID."""
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json == {"id": 1, "name": "Ahmed", "email": "ahmed@example.com"}


def test_get_user_not_found(client):
    """Test retrieving a user with an ID that doesn't exist."""
    response = client.get('/users/99')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}
