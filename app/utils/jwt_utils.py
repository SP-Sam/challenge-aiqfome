import jwt

from app.config import app_config

secret_key = app_config.JWT_SECRET_KEY

class JwtUtils:
    @staticmethod
    def create_token(payload):
        return jwt.encode(payload, secret_key, algorithm="HS256")

    @staticmethod
    def decode_token(token):
        try:
            decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None