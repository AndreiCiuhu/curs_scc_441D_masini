from flask import Flask

from app.routes.test import test_bp
from app.routes.skoda import skoda_bp

app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(skoda_bp)


@app.route("/", methods=["GET"])
def index():
    return """
    <h1>Proiect SCC 441D - Masini</h1>
    <p>Aplicatie Flask pentru proiectul de Servicii Cloud si Containerizare.</p>
    <p>Functionalitate adaugata: Skoda - Pamfir Cosmin Alexandru.</p>
    <a href="/masini">Deschide pagina Masini</a>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
