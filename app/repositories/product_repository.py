from app.config.db import db
from app.models.product import Product
from app.types import TProduct


class ProductRepository:
    @staticmethod
    def create_product(product: TProduct):
        product_to_add = Product(
            id=product.id,
            title=product.title,
            image=product.image,
            price=product.price,
            review=product.review,
        )

        db.session.add(product_to_add)
        db.session.commit()


    @staticmethod
    def get_product_by_id(product_id):
        return db.session.query(Product).filter(Product.id == product_id).scalar()