from flask import Blueprint, request
from app.lib.biblioteca_masini import culoare_ferrari, descriere_ferrari

ferrari_bp = Blueprint('ferrari', __name__, url_prefix='/masini/ferrari')

@ferrari_bp.route('/', methods=['GET'])
def index():
    return """
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Ferrari</h1>
        <p>Ferrari este un producator italian de automobile sportive fondat in 1939 de Enzo Ferrari.</p>
        <ul>
            <li><a href="/masini/ferrari/modele">Modele Ferrari</a></li>
        </ul>
        <h2>Cauta detalii model</h2>
        <form action="/masini/ferrari/detalii" method="get">
            <input type="text" name="model" placeholder="Ex: roma" style="padding:8px; font-size:16px;"/>
            <button type="submit" style="padding:8px 16px; font-size:16px; cursor:pointer;">Cauta</button>
        </form>
    </body>
    </html>
    """

@ferrari_bp.route('/modele', methods=['GET'])
def modele():
    modele_lista = ['roma', 'portofino', '488', 'f8', 'sf90']
    res = ''
    for model in modele_lista:
        culoare = culoare_ferrari(model)
        descriere = descriere_ferrari(model)
        res += f"""
        <div style="border:1px solid #ddd; border-radius:8px; padding:16px; margin:12px 0;">
            <h2 style="margin:0 0 8px 0;">{model.upper()}</h2>
            <p>Descriere: {descriere}</p>
            <p>Culoare: {culoare}</p>
        </div>
        """
    return f"""
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Modele Ferrari</h1>
        {res}
        <br>
        <a href="/masini/ferrari">Inapoi la Ferrari</a>
    </body>
    </html>
    """

@ferrari_bp.route('/detalii', methods=['GET'])
def detalii():
    model = request.args.get('model', '')
    if not model:
        return 'Specifica un model: /masini/ferrari/detalii?model=roma', 400
    culoare = culoare_ferrari(model)
    descriere = descriere_ferrari(model)
    if culoare == 'Model negasit' or culoare == 'Culoare nedisponibila':
        return f'Nu a fost gasit niciun rezultat pentru modelul: {model}', 404
    return f"""
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Detalii Ferrari {model.upper()}</h1>
        <div style="border:1px solid #ddd; border-radius:8px; padding:16px;">
            <p>Descriere: {descriere}</p>
            <p>Culoare: {culoare}</p>
        </div>
        <br>
        <a href="/masini/ferrari">Inapoi la Ferrari</a>
    </body>
    </html>
    """
