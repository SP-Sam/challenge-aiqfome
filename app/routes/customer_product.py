from flask import Blueprint

from app.decorators.request_body_validator import request_body_validator
from app.middlewares.auth import auth_middleware
from app.modules.customer_product.customer_product_controller import CustomerProductController
from app.modules.customer_product.customer_product_validator_schemas import associate_product_schema

customer_product = Blueprint("customer_product", __name__, url_prefix="/customer_products")

customer_product_controller = CustomerProductController()

@customer_product.route("", methods=["POST"])
@request_body_validator(associate_product_schema)
@auth_middleware()
def associate_customer_to_product():
    return customer_product_controller.associate_customer_to_product()

@customer_product.route("", methods=["GET"])
@auth_middleware()
def get_favorite_products():
    return customer_product_controller.get_favorite_products()