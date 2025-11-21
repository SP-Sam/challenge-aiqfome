from app.config.db import db
from app.models.customer_product import CustomerProduct
from app.models.product import Product


class CustomerProductRepository:
    @staticmethod
    def associate_customer_to_product(customer_id, product_id):
        customer_product = CustomerProduct(customer_id=customer_id, product_id=product_id)

        db.session.add(customer_product)
        db.session.commit()

    @staticmethod
    def get_favorite_products(customer_id):
        query = (db.session.query(Product)
                 .join(CustomerProduct, CustomerProduct.product_id == Product.id)
                 .filter(CustomerProduct.customer_id == customer_id))

        products = query.all()

        return [product.to_dict() for product in products]