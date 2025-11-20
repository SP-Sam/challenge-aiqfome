from flask import jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import NotFound

from app.repositories.customer_repository import CustomerRepository


class CustomerController:
    def __init__(self):
        self.customer_repository = CustomerRepository()

    def get_customers(self):
        try:
            customers = self.customer_repository.get_customers()

            return jsonify({"status": "SUCCESS", "message": "Clientes buscados com sucesso", "data": customers}), 200
        except SQLAlchemyError as db_error:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao buscar clientes", "error": db_error.orig.args[0]}), 500

    def get_customer_by_id(self, customer_id):
        try:
            customer = self.customer_repository.get_customer_by_id(customer_id)

            return jsonify({"status": "SUCCESS", "message": "Cliente encontrado com sucesso", "data": customer}), 200
        except SQLAlchemyError as db_error:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao buscar cliente", "error": db_error.orig.args[0]}), 500
        except NotFound:
            return jsonify({"status": "ERROR", "message": "Cliente não encontrado"}), 400

    def update_customer(self, customer_id):
        request_body = request.get_json()

        try:
            customer = self.customer_repository.update_customer(customer_id, request_body)

            return jsonify({"status": "SUCCESS", "message": "Informações do cliente atualizadas com sucesso", "data": customer}), 200
        except SQLAlchemyError as db_error:
            error_message = db_error.orig.args[0]

            if "duplicate key" in error_message:
                return jsonify({"status": "ERROR", "message": "Este email já está sendo usado por outro cliente", "error": error_message}), 409
            else:
                return jsonify({"status": "ERROR", "message": "Erro inesperado ao atualizar informações do cliente", "error": error_message}), 500
        except NotFound:
            return jsonify({"status": "ERROR", "message": "Cliente não encontrado"}), 400