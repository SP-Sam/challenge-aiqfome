import bcrypt


class PasswordUtils:
    @staticmethod
    def encrypt_password(password):
        salt = bcrypt.gensalt()
        encrypted_password = bcrypt.hashpw(password.encode("utf-8"), salt)

        return encrypted_password.decode("utf-8")

    @staticmethod
    def check_password(password, encrypted_password):
        return bcrypt.checkpw(password.encode("utf-8"), encrypted_password.encode("utf-8"))