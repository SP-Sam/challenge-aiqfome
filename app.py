from flask import Flask

from app.config import app_config
from app.config.db import db

from app.models.customer import Customer
from app.models.product import Product
from app.models.customer_product import CustomerProduct


class App:
    def __init__(self, config):
        self.app = Flask(__name__)
        self.app.config.from_object(config)
        self.db = db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def run(self):
        return self.app.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    app = App(app_config)
    app.run()