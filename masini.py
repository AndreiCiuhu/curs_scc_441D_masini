from flask import Flask

from app.routes.test import test_bp
from app.routes.renault import renault_bp


app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(renault_bp)


@app.route("/")
def index():
    return "Masini"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
