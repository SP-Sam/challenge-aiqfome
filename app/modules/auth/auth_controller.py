from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.customer_repository import CustomerRepository
from app.types import TCustomer


class AuthController:
    def __init__(self):
        self.customer_repository = CustomerRepository()

    def register_customer(self):
        request_body = request.get_json()

        new_customer = TCustomer(**request_body)

        try:
            new_customer = self.customer_repository.register_customer(new_customer)

            return jsonify({"status": "SUCCESS", "message": "Cliente registrado com sucesso", "data": new_customer}), 201
        except SQLAlchemyError as db_error:
            error_message = db_error.orig.args[0]

            if "duplicate key" in error_message:
                return  jsonify({"status": "ERROR", "message": "Cliente já registrado", "error": error_message}), 409
            else:
                return  jsonify({"status": "ERROR", "message": "Erro inesperado ao registrar cliente", "error": error_message}), 500
