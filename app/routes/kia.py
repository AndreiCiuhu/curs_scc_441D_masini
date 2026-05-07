from flask import Blueprint

kia_bp= Blueprint('kia', __name__, url_prefix='/masini/kia')

@kia_bp.route('/', methods=['GET'])
def index():
    return f'Kia'