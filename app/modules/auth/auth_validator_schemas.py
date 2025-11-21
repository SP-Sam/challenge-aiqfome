create_customer_schema = {
    "name": {"type": "string", "required": True, "empty": False},
    "email": {"type": "string", "required": True, "empty": False, "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
    "password": {"type": "string", "required": True, "empty": False, "minlength": 5},
    "is_admin": {"type": "boolean", "required": False, "empty": True},
}

login_schema = {
    "email": {"type": "string", "required": True, "empty": False, "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"},
    "password": {"type": "string", "required": True, "empty": False, "minlength": 5},
}