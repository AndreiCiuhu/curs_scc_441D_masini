from flask import Blueprint
from app.lib.biblioteca_masini import get_culoare_bmw, get_descriere_bmw

bmw_bp = Blueprint('bmw_bp', __name__)

@bmw_bp.route('/masini/bmw')
def pagina_bmw():
    return "Pagina principală BMW"

@bmw_bp.route('/masini/bmw/culoare')
def culoare():
    return get_culoare_bmw()

@bmw_bp.route('/masini/bmw/descriere')
def descriere():
    return get_descriere_bmw()
