from flask import Blueprint

from app.decorators.request_body_validator import request_body_validator
from app.modules.customer.customer_controller import CustomerController
from app.modules.customer.customer_validator_schemas import update_customer_schema

customer = Blueprint("customer", __name__, url_prefix="/customer")

customer_controller = CustomerController()

# TODO - ONLY ADMIN
@customer.route("", methods=["GET"])
def get_customers():
    return customer_controller.get_customers()

@customer.route("/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    return customer_controller.get_customer_by_id(customer_id)

@customer.route("/<customer_id>", methods=["PATCH"])
@request_body_validator(update_customer_schema)
def update_customer(customer_id):
    return customer_controller.update_customer(customer_id)