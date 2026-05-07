from flask import Blueprint

test_bp = Blueprint('test', __name__, url_prefix='/masini/test')

@test_bp.route('/')
def index():
    return "Aceasta este ruta de test."
