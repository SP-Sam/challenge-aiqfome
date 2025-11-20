from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.config.db import db


class CustomerProduct(db.Model):
    __tablename__ = "customer_product"

    customer_id = Column(
        Integer,
        ForeignKey("customer.id", ondelete="CASCADE"),
        primary_key=True
    )
    product_id = Column(
        Integer,
        ForeignKey("product.id", ondelete="CASCADE"),
        primary_key=True
    )
    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now())

    customer = relationship("Customer", back_populates="customer_products")
    product = relationship("Product", back_populates="product_customers")