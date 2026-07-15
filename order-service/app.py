"""
Order Service API.

This module handles microservice order operations including health checks,
retrieving orders, and creating new orders.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5003)
