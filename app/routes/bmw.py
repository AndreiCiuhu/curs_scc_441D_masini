from flask import Blueprint, request

from app.lib.biblioteca_masini import (
    modele_bmw,
    detalii_bmw,
)

bmw_bp = Blueprint('bmw', __name__, url_prefix='/masini/bmw')

@bmw_bp.route('/', methods=['GET'])
def index():
    return """
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>BMW</h1>
        <p>BMW este un producator german de automobile fondat in 1916.</p>
        <ul>
            <li><a href="/masini/bmw/modele">Modele BMW</a></li>
        </ul>
        <h2>Cauta detalii model</h2>
        <form action="/masini/bmw/detalii" method="get">
            <input type="text" name="model" placeholder="Ex: m3" style="padding:8px; font-size:16px;"/>
            <button type="submit" style="padding:8px 16px; font-size:16px; cursor:pointer;">Cauta</button>
        </form>
    </body>
    </html>
    """

@bmw_bp.route('/modele', methods=['GET'])
def modele():
    data = modele_bmw()

    if not data:
        return 'Nu a fost gasit niciun model', 500

    res = f''
    for masina in data:
        res += f"""
        <div style="border:1px solid #ddd; border-radius:8px; padding:16px; margin:12px 0;">
            <h2 style="margin:0 0 8px 0;">{masina.get('year')} {masina.get('make')} {masina.get('model')}</h2>
            <p>Motor: {masina.get('displacement')}L</p>
            <p>Combustibil: {masina.get('fuel_type')}</p>
            <p>Transmisie: {masina.get('transmission')}</p>
            <p>Cai putere: {masina.get('horsepower')} HP</p>
        </div>
        """

    return f"""
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Modele BMW</h1>
        {res}
        <br>
        <a href="/masini/bmw"> Inapoi la BMW</a>
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
        <a href="/masini/bmw"> Inapoi la BMW</a>
    </body>
    </html>
    """
