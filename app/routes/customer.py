from flask import Blueprint

from app.decorators.request_body_validator import request_body_validator
from app.middlewares.auth import auth_middleware
from app.modules.customer.customer_controller import CustomerController
from app.modules.customer.customer_validator_schemas import update_customer_schema

customer = Blueprint("customer", __name__, url_prefix="/customers")

customer_controller = CustomerController()

@customer.route("", methods=["GET"])
@auth_middleware(admin=True)
def get_customers():
    return customer_controller.get_customers()

@customer.route("/<customer_id>", methods=["GET"])
@auth_middleware(admin=True)
def get_customer_by_id(customer_id):
    return customer_controller.get_customer_by_id(customer_id)

@customer.route("/<customer_id>", methods=["PATCH"])
@auth_middleware(admin=True)
@request_body_validator(update_customer_schema)
def update_customer(customer_id):
    return customer_controller.update_customer(customer_id)

@customer.route("/<customer_id>", methods=["DELETE"])
@auth_middleware(admin=True)
def remove_customer(customer_id):
    return customer_controller.remove_customer(customer_id)