from flask import Blueprint

from app.modules.customer.customer_controller import CustomerController

customer = Blueprint("customer", __name__, url_prefix="/customer")

customer_controller = CustomerController()

# TODO - ONLY ADMIN
@customer.route("", methods=["GET"])
def get_customers():
    return customer_controller.get_customers()

@customer.route("/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    return customer_controller.get_customer_by_id(customer_id)