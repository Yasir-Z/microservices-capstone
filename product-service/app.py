"""
Product Service API.

This module handles product discovery operations including health checks,
fetching all products, and retrieving specific products by ID.
"""

from flask import Flask, jsonify

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=5002) # nosec B104
