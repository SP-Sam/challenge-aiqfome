from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric
from sqlalchemy.orm import relationship

from app.config.db import db


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    image = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    review = Column(Text)

    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now())

    product_customers = relationship(
        "CustomerProduct",
        back_populates="product",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def to_dict(self):
        return dict(
            id = self.id,
            title = self.title,
            image = self.image,
            price = self.price,
            review = self.review,
            created_at = self.created_at,
        )