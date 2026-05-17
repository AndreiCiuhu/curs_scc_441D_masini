from flask import Blueprint
from app.lib.biblioteca_masini import culoare_ferrari, descriere_ferrari

ferrari_bp = Blueprint('ferrari', __name__, url_prefix='/ferrari')

@ferrari_bp.route('/')
def index():
    return 'Ferrari - Pagina principala'

@ferrari_bp.route('/modele')
def modele():
    modele_lista = ['Roma', 'Portofino', '488', 'F8', 'SF90']
    return '<br>'.join(modele_lista)

@ferrari_bp.route('/culoare/<model>')
def culoare(model):
    return culoare_ferrari(model)

@ferrari_bp.route('/descriere/<model>')
def descriere(model):
    return descriere_ferrari(model)
