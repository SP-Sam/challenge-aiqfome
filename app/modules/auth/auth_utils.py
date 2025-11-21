from app.errors import AuthFailedError
from app.repositories.customer_repository import CustomerRepository
from app.utils.jwt_utils import JwtUtils
from app.utils.password_utils import PasswordUtils


class AuthUtils:
    def __init__(self):
        self.customer_repository = CustomerRepository()

    @staticmethod
    def check_password_match(password, encrypted_password):
        if not PasswordUtils.check_password(password, encrypted_password):
            raise AuthFailedError()

    def generate_token(self, email, password):
        customer = self.customer_repository.get_customer_by_email(email)

        if not customer:
            raise AuthFailedError()

        self.check_password_match(password, customer.password)

        token = JwtUtils.create_token(customer.to_dict())

        return token
