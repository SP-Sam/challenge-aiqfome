from app.config.db import db
from app.models.customer import Customer
from app.types import TCustomer
from app.utils.password_utils import PasswordUtils


class CustomerRepository:
    @staticmethod
    def register_customer(customer: TCustomer):
        encrypted_password = PasswordUtils.encrypt_password(customer.password)

        new_customer = Customer(
            name=customer.name,
            email=customer.email,
            password=encrypted_password,
            is_admin=customer.is_admin,
        )

        db.session.add(new_customer)
        db.session.commit()

        return new_customer.to_dict()

    @staticmethod
    def get_customers():
        customers = Customer.query.all()

        return [customer.to_dict() for customer in customers]

    @staticmethod
    def get_customer_by_id(customer_id):
        customer = db.session.query(Customer).filter(Customer.id == customer_id).first_or_404()

        return customer.to_dict()

    @staticmethod
    def get_customer_by_email(customer_email):
        customer = db.session.query(Customer).filter(Customer.email == customer_email).scalar()

        return customer

    @staticmethod
    def update_customer(customer_id, data):
        customer = db.session.query(Customer).filter(Customer.id == customer_id).first_or_404()

        for key, value in data.items():
            if key == 'password':
                setattr(customer, key, PasswordUtils.encrypt_password(value))
            else:
                setattr(customer, key, value)

        db.session.commit()

        return customer.to_dict()

    @staticmethod
    def remove_customer(customer_id):
        customer = db.session.query(Customer).filter(Customer.id == customer_id).first_or_404()

        db.session.delete(customer)

        db.session.commit()