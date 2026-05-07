from flask import Blueprint, request
from app.lib.biblioteca_masini import (
    modele_bmw,
    detalii_bmw,
)

# Adaugam url_prefix cum a facut colegul tau
bmw_bp = Blueprint('bmw', __name__, url_prefix='/masini/bmw')

@bmw_bp.route('/', methods=['GET'])
def index():
    # Cream lista de link-uri (res) folosind functia modele_bmw
    modele = modele_bmw()
    res = "<ul>" + "".join([f'<li><a href="/masini/bmw/detalii?model={m}">BMW {m.upper()}</a></li>' for m in modele]) + "</ul>"
    
    return f"""
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Modele BMW Disponibile</h1>
        {res}
    </body>
    </html>
    """

@bmw_bp.route('/detalii', methods=['GET'])
def detalii():
    model = request.args.get('model', '')

    if not model:
        return f'Specifica un model: /masini/bmw/detalii?model=m3', 400

    data = detalii_bmw(model=model)

    if not data:
        return f'Nu a fost gasit niciun rezultat pentru modelul: {model}', 404

    return f"""
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Detalii {data.get('year')} BMW {data.get('model').title()}</h1>
        <div style="border:1px solid #ddd; border-radius:8px; padding:16px;">
            <p>Clasa: {data.get('class').title()}</p>
            <p>Cilindri: {data.get('cylinders')}</p>
            <p>Cilindree: {data.get('displacement')}L</p>
            <p>Tractiune: {data.get('drive').upper()}</p>
            <p>Combustibil: {data.get('fuel_type')}</p>
            <p>Transmisie: {data.get('transmission').upper()}</p>
        </div>
        <br>
        <a href="/masini/bmw">← Inapoi la BMW</a>
    </body>
    </html>
    """
