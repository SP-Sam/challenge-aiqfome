from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime
from sqlalchemy.orm import relationship

from app.config.db import db


class Customer(db.Model):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    created_at = Column(DateTime, nullable=False, default=lambda: datetime.now())
    updated_at = Column(DateTime, nullable=False, default=lambda: datetime.now(), onupdate=lambda: datetime.now())

    customer_products = relationship(
        "CustomerProduct",
        back_populates="customer",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            email = self.email,
            created_at = self.created_at,
            updated_at = self.updated_at,
        )