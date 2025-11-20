from flask import Flask


class App:
    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        return self.app.run(debug=True, host="0.0.0.0")

if __name__ == "__main__":
    app = App()
    app.run()