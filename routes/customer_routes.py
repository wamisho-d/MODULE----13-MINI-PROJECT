from flask import Blueprint, request
from controllers.customer_controller import create_customer, get_customer

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/customer', methods=['POST'])
def create_customer_route():
    data = request.json
    return create_customer(data)

@customer_bp.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer_route(customer_id):
    return get_customer(customer_id)
