from flask import Blueprint
from app.lib.biblioteca_masini import (
    culoare_hyundai,
    descriere_hyundai
)

hyundai_bp = Blueprint('hyundai', __name__)

@hyundai_bp.route('/masini')
def masini():
    return 'Pagina masini'

@hyundai_bp.route('/masini/hyundai')
def hyundai():
    return 'Pagina Hyundai'

@hyundai_bp.route('/masini/hyundai/culoare')
def culoare():
    return culoare_hyundai()

@hyundai_bp.route('/masini/hyundai/descriere')
def descriere():
    return descriere_hyundai()
