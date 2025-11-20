update_customer_schema = {
    "name": {"type": "string", "required": False, "empty": False},
    "email": {"type": "string", "required": False, "empty": False, 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
    "password": {"type": "string", "required": False, "empty": False, "minlength": 5},
    "is_admin": {"type": "boolean", "required": False, "empty": False},
}