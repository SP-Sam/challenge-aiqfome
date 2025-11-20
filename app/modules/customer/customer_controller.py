from flask import jsonify
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
        except SQLAlchemyError as error:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao buscar clientes", "error": error.orig.args[0]}), 500

    def get_customer_by_id(self, customer_id):
        try:
            customer = self.customer_repository.get_customer_by_id(customer_id)

            return jsonify({"status": "SUCCESS", "message": "Cliente encontrado com sucesso", "data": customer}), 200
        except SQLAlchemyError as error:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao buscar cliente", "error": error.orig.args[0]}), 500
        except NotFound:
            return jsonify({"status": "ERROR", "message": "Cliente não encontrado"}), 400
