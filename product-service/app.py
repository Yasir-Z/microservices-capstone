"""
Product Service API.

This module handles product discovery operations including health checks,
fetching all products, and retrieving specific products by ID.
"""

import os
from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from dotenv import load_dotenv

# Load local environment variables from a .env file if it exists
load_dotenv()

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "product_service_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

@app.after_request
def after_request(response):

    REQUEST_COUNT.labels(
        request.method,
        request.path,
        response.status_code
    ).inc()

    return response

@app.route('/metrics')
def metrics():

    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }

products = [
    {"id": 1, "name": "Laptop", "price": 999},
    {"id": 2, "name": "Phone", "price": 499},
    {"id": 3, "name": "Tablet", "price": 299}
]


@app.route('/health')
def health():
    """Return the health status of the product service."""
    return jsonify({"status": "ok", "service": "product-service"})


@app.route('/products')
def get_products():
    """Retrieve the list of all available products."""
    return jsonify(products)


@app.route('/products/<int:product_id>')
def get_product(product_id):
    """Retrieve a single product by its ID."""
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    # Default to secure 127.0.0.1 for local runs; override to 0.0.0.0 in Docker/K8s
    host_ip = os.getenv('HOST_IP', '127.0.0.1')
    # Default to port 5002, but cast to an integer
    port_num = int(os.getenv('PORT', 5002))

    app.run(host=host_ip, port=port_num)  # nosec B104
