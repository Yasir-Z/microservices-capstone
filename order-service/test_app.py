"""
Unit tests for the Order Service.
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
    assert response.json == {"status": "ok", "service": "order-service"}


def test_get_orders_empty(client):
    """Test that GET /orders starts empty."""
    response = client.get('/orders')
    assert response.status_code == 200
    assert response.json == []


def test_create_order(client):
    """Test that POST /orders successfully creates a new order."""
    payload = {
        "user_id": 1,
        "product_id": 2
    }
    response = client.post('/orders', json=payload)
    assert response.status_code == 201
    
    # Assert return structure
    data = response.json
    assert data["id"] == 1
    assert data["user_id"] == 1
    assert data["product_id"] == 2
    assert data["status"] == "pending"
