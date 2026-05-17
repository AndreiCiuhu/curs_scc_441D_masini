from flask import Blueprint, request
from app.lib.biblioteca_masini import culoare_ferrari, descriere_ferrari

ferrari_bp = Blueprint('ferrari', __name__, url_prefix='/masini/ferrari')

STYLE = """
    body {
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 40px auto;
        padding: 0 20px;
        background-color: #ffffff;
        color: #1a1a1a;
    }
    h1 {
        color: #cc0000;
        letter-spacing: 3px;
        border-bottom: 3px solid #cc0000;
        padding-bottom: 10px;
    }
    h2 { color: #cc0000; margin: 0 0 8px 0; }
    a {
        display: inline-block;
        background-color: #cc0000;
        color: white;
        text-decoration: none;
        padding: 8px 20px;
        border-radius: 4px;
        font-weight: bold;
        margin-top: 10px;
    }
    a:hover { background-color: #ff0000; }
    .card {
        border: 2px solid #cc0000;
        border-radius: 8px;
        padding: 16px;
        margin: 12px 0;
    }
    input {
        padding: 8px;
        font-size: 16px;
        border: 2px solid #cc0000;
        border-radius: 4px;
        outline: none;
    }
    button {
        padding: 8px 16px;
        font-size: 16px;
        background-color: #cc0000;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
    }
    button:hover { background-color: #ff0000; }
"""

@ferrari_bp.route('/', methods=['GET'])
def index():
    return f"""
    <html>
    <head><style>{STYLE}</style></head>
    <body>
        <h1>Ferrari</h1>
        <p>Ferrari este un producator italian de automobile sportive fondat in 1939 de Enzo Ferrari.</p>
        <ul style="list-style:none; padding:0;">
            <li><a href="/masini/ferrari/modele">Modele Ferrari</a></li>
        </ul>
        <h2 style="margin-top:30px;">Cauta detalii model</h2>
        <form action="/masini/ferrari/detalii" method="get">
            <input type="text" name="model" placeholder="Ex: roma"/>
            <button type="submit">Cauta</button>
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
        <div class="card">
            <h2>{model.upper()}</h2>
            <p>Descriere: {descriere}</p>
            <p>Culoare: {culoare}</p>
        </div>
        """
    return f"""
    <html>
    <head><style>{STYLE}</style></head>
    <body>
        <h1>Modele Ferrari</h1>
        {res}
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
    if culoare in ('Model negasit', 'Culoare nedisponibila'):
        return f'Nu a fost gasit niciun rezultat pentru modelul: {model}', 404
    return f"""
    <html>
    <head><style>{STYLE}</style></head>
    <body>
        <h1>Detalii Ferrari {model.upper()}</h1>
        <div class="card">
            <p>Descriere: {descriere}</p>
            <p>Culoare: {culoare}</p>
        </div>
        <a href="/masini/ferrari">Inapoi la Ferrari</a>
    </body>
    </html>
    """
