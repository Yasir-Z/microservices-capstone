"""
Order Service API.

This module handles microservice order operations including health checks,
retrieving orders, and creating new orders.
"""

import os
from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from dotenv import load_dotenv

# Load local environment variables from a .env file if it exists
load_dotenv()

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "order_service_requests_total",
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

orders = []


@app.route('/health')
def health():
    """Return the health status of the order service."""
    return jsonify({"status": "ok", "service": "order-service"})


@app.route('/orders')
def get_orders():
    """Retrieve the list of all orders."""
    return jsonify(orders)


@app.route('/orders', methods=['POST'])
def create_order():
    """Create a new order and append it to the orders database."""
    data = request.json or {}
    order = {
        "id": len(orders) + 1,
        "user_id": data.get("user_id"),
        "product_id": data.get("product_id"),
        "status": "pending"
    }
    orders.append(order)
    return jsonify(order), 201


if __name__ == '__main__':
    # Default to secure 127.0.0.1 for local runs; override to 0.0.0.0 in Docker/K8s
    host_ip = os.getenv('HOST_IP', '127.0.0.1')
    # Default to port 5003, but cast to an integer
    port_num = int(os.getenv('PORT', 5003))

    app.run(host=host_ip, port=port_num)  # nosec B104
