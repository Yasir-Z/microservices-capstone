"""
Unit tests for the Product Service.
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
    assert response.json == {"status": "ok", "service": "product-service"}


def test_get_all_products(client):
    """Test retrieving the list of all available products."""
    response = client.get('/products')
    assert response.status_code == 200
    assert len(response.json) == 3
    assert response.json[0]["name"] == "Laptop"


def test_get_product_success(client):
    """Test retrieving a single product by its correct ID."""
    response = client.get('/products/2')
    assert response.status_code == 200
    assert response.json == {"id": 2, "name": "Phone", "price": 499}


def test_get_product_not_found(client):
    """Test retrieving a product with an ID that doesn't exist."""
    response = client.get('/products/999')
    assert response.status_code == 404
    assert response.json == {"error": "Product not found"}
