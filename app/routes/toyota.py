from flask improt Blueprint

toyota_bp = Blueprint('toyota', __name__)

def culoare_toyota():
    return "Toyota este disponibila in culorile: alb, negru, gri, rosu, albastru."

def descriere_toyota():
    return "Toyota este un producator japonez de autoturisme."

@toyota_bp.route('/')
def index():
    return "Pagina principala pentru Toyota"

@toyota_bp.route('/masini')
def masini():
    return "Pagina temei: Masini Toyota"

@toyota_bp.route('/masini/culoare')
def masini_culoare():
    return culoare_toyota()

@toyota_bp.route('/masini/descriere')
def masini_descriere():
    return descriere_toyota()