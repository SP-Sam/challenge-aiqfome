from flask import Flask


class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule("/", "index", self.index)

    def index(self):
        return "Desafio técnico aiqfome"

    def run(self):
        return self.app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    app = App()
    app.run()
