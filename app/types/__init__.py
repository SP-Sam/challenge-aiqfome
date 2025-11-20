from dataclasses import dataclass


@dataclass
class TCustomer:
    name: str
    email: str
    password: str
    is_admin: bool = False

@dataclass
class TProduct:
    title: str
    image: str
    price: float
    review: str
