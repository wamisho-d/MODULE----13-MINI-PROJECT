from models import db, Customer
from flask import jsonify, request

def create_customer(data):
    new_customer = Customer(name=data['name'], email=data['email'], phone_number=data['phone_number'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer created successfully"}), 201

def get_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    return jsonify({
        "id": customer.id,
        "name": customer.name,
        "email": customer.email,
        "phone_number": customer.phone_number
    })
