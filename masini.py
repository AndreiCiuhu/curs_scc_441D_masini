from flask import Flask

from routes.test import test_bp
from routes.porsche import porsche_bp

app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(porsche_bp)


@app.route("/")
def index():
    return "Masini"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

