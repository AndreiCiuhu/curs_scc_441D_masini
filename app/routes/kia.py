from flask import Blueprint

kia_bp= Blueprint('kia', __name__, url_prefix='/kia')

@kia_bp.route('/', methods=['GET'])
def index():
    return 'Kia'