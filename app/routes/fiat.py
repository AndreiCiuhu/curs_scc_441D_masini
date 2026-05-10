from flask import Blueprint
from app.lib.biblioteca_masini import descriere_fiat, modele_fiat

fiat_bp = Blueprint('fiat', __name__, url_prefix='/masini/fiat')


@fiat_bp.route('/')
def fiat():
    return """
    <h1>Fiat - Dumbrava Teodor</h1>
    <p>Fiat este marca auto aleasa pentru proiectul SCC, grupa 441D, tema Masini.</p>
    <ul>
        <li><a href="/masini/fiat/descriere">Descriere Fiat</a></li>
        <li><a href="/masini/fiat/modele">Modele Fiat</a></li>
    </ul>
    """


@fiat_bp.route('/descriere')
def ruta_descriere_fiat():
    return descriere_fiat()


@fiat_bp.route('/modele')
def ruta_modele_fiat():
    return modele_fiat()
