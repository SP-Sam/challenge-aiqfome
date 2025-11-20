from http.client import HTTPException

from flask import jsonify


class CustomError(HTTPException):
    error = "Erro inesperado"
    description = "Erro inesperado"
    code = 500

    def get_response(self):
        response = jsonify(error=self.error, message=self.description)
        response.status_code = self.code
        return response

class MissingRequiredFieldsError(CustomError):
    error = "Campos obrigatórios não informados"
    description = "Campos obrigatórios não informados ou inválidos"
    code = 417

    def __init__(self, missing_fields=None):
        super().__init__()
        if missing_fields:
            self.missing_fields = missing_fields
            self.description = f'Campos obrigatórios não informados ou inválidos: {", ".join(missing_fields)}'