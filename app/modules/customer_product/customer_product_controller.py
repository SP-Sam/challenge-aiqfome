from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.customer_product_repository import CustomerProductRepository
from app.repositories.product_repository import ProductRepository
from app.services.product_service import fetch_product


class CustomerProductController:
    def __init__(self):
        self.customer_product_repository = CustomerProductRepository()
        self.product_repository = ProductRepository()

    def associate_customer_to_product(self):
        product_id = request.get_json().get("product_id")
        customer_id = request.customer_id

        try:
            self._create_product_if_necessary(product_id)

            self.customer_product_repository.associate_customer_to_product(customer_id, product_id)

            return jsonify({"status": "SUCCESS", "message": "Produto favoritado com sucesso"}), 200
        except SQLAlchemyError as db_error:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao remover cliente do sistema", "error": db_error.orig.args[0]}), 500

    def get_favorite_products(self):
        customer_id = request.customer_id

        try:
            products = self.customer_product_repository.get_favorite_products(customer_id)

            return jsonify({"status": "SUCCESS", "message": "Produtos favoritos buscados com sucesso", "data": products}), 200
        except SQLAlchemyError as db_error:
            return jsonify({"status": "ERROR", "message": "Erro inesperado ao remover cliente do sistema", "error": db_error.orig.args[0]}), 500

    def _create_product_if_necessary(self, product_id):
        if self.product_repository.get_product_by_id(product_id):
            return

        fetched_product = fetch_product(product_id)

        if fetched_product is None:
            raise Exception(f"Product with id {product_id} not found")

        self.product_repository.create_product(fetched_product)
