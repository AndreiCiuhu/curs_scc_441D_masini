from flask import Flask
from app.routes.mclaren import mclaren_bp

app = Flask(__name__)

app.register_blueprint(mclaren_bp)


@app.route("/")
def index():
    return """
    <h1>Proiect SCC - 441D - Masini</h1>
    <p>Aplicatie Flask pentru tema Masini.</p>
    <p>Contributie individuala: McLaren - Stefan Poting</p>
    <ul>
        <li><a href="/masini">Tema Masini</a></li>
        <li><a href="/masini/mclaren">Pagina McLaren</a></li>
        <li><a href="/masini/mclaren/culoare">Culoare McLaren</a></li>
        <li><a href="/masini/mclaren/descriere">Descriere McLaren</a></li>
    </ul>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
