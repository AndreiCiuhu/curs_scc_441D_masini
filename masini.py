from flask import Flask

from app.routes.test import test_bp
from app.routes.fiat import fiat_bp

app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(fiat_bp)


@app.route('/')
def index():
    return """
    <h1>Proiect SCC - Masini</h1>
    <p>Student: Dumbrava Teodor</p>
    <p>Marca aleasa: Fiat</p>
    <ul>
        <li><a href="/test">Ruta test</a></li>
        <li><a href="/masini/fiat">Fiat</a></li>
        <li><a href="/masini/fiat/descriere">Descriere Fiat</a></li>
        <li><a href="/masini/fiat/modele">Modele Fiat</a></li>
    </ul>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
