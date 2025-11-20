from flask import request, jsonify
from cerberus import Validator
from functools import wraps

from app.errors import MissingRequiredFieldsError

def request_body_validator(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            validator = Validator(schema)

            request_body = request.get_json()

            if not validator.validate(request_body):
                error_message = validator.errors

                return (
                    jsonify(
                        {
                            "status": "ERROR",
                            "message": str(error_message),
                            "error": MissingRequiredFieldsError.error,
                        }
                    ),
                    MissingRequiredFieldsError.code,
                )

            return func(*args, **kwargs)

        return wrapper

    return decorator