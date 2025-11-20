from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.customer_repository import CustomerRepository


class CustomerController:
    def __init__(self):
        self.customer_repository = CustomerRepository()

    def get_customers(self):
        try:
            customers = self.customer_repository.get_customers()

            return jsonify({"status": "SUCCESS", "message": "Clientes buscados com sucesso", "data": customers}), 200
        except SQLAlchemyError:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao buscar clientes" }), 500
