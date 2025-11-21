from functools import wraps

from flask import request

from app.errors import AuthRequiredError, UnauthorizedError
from app.utils.jwt_utils import JwtUtils


def auth_middleware(admin=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            authorization = request.headers.get("Authorization")

            if not authorization or not authorization.startswith("Bearer "):
                return AuthRequiredError().get_response()

            token = authorization.split("Bearer ")[1]

            if not token:
                return AuthRequiredError().get_response()

            token_data = JwtUtils.decode_token(token)

            if not token_data:
                return AuthRequiredError().get_response()

            if admin and token_data.get("is_admin") is False:
                return UnauthorizedError().get_response()

            request.customer_id = token_data.get("id")

            return func(*args, **kwargs)

        return wrapper

    return decorator
