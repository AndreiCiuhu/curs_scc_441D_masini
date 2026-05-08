from flask import Blueprint

from app.lib.biblioteca_masini import culoare_skoda, descriere_skoda

skoda_bp = Blueprint("skoda", __name__)


@skoda_bp.route("/masini", methods=["GET"])
def masini():
    return """
    <h1>Proiect SCC 441D - Masini</h1>
    <p>Aceasta este pagina generala pentru tema Masini.</p>
    <p>Element implementat de Pamfir Cosmin Alexandru: Skoda.</p>
    <a href="/masini/skoda">Deschide pagina Skoda</a>
    """


@skoda_bp.route("/masini/skoda", methods=["GET"])
def skoda():
    return """
    <h1>Skoda</h1>
    <p>Pagina dedicata marcii Skoda.</p>
    <ul>
        <li><a href="/masini/skoda/culoare">Culoare Skoda</a></li>
        <li><a href="/masini/skoda/descriere">Descriere Skoda</a></li>
    </ul>
    """


@skoda_bp.route("/masini/skoda/culoare", methods=["GET"])
def culoare():
    return culoare_skoda()


@skoda_bp.route("/masini/skoda/descriere", methods=["GET"])
def descriere():
    return descriere_skoda()
