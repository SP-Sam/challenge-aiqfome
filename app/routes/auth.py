from flask import Blueprint

from app.decorators.request_body_validator import request_body_validator
from app.modules.auth.auth_controller import AuthController
from app.modules.auth.auth_validator_schemas import create_customer_schema

auth = Blueprint("auth", __name__, url_prefix="/auth")

auth_controller = AuthController()


@auth.route("/register", methods=["POST"])
@request_body_validator(create_customer_schema)
def register():
    return auth_controller.register_customer()
