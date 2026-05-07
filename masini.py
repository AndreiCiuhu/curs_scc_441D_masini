from flask import Flask, redirect

from routes.test import test_bp
from routes.porsche import porsche_bp

app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(porsche_bp)


@app.route("/")
def index():
    return redirect("/masini/porsche/")


@app.route("/masini")
def masini():
    return redirect("/masini/porsche/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
