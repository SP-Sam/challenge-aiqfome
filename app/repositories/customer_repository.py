from app.config.db import db
from app.models.customer import Customer
from app.types import TCustomer


class CustomerRepository:
    @staticmethod
    def register_customer(customer: TCustomer):
        new_customer = Customer(
            name=customer.name,
            email=customer.email,
            password=customer.password,
            is_admin=customer.is_admin,
        )

        db.session.add(new_customer)
        db.session.commit()

        return new_customer.to_dict()