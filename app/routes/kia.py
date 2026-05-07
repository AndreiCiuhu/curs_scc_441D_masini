from flask import Blueprint, request

from app.lib.biblioteca_masini import (
    modele_kia,
    detalii_kia,
)

kia_bp= Blueprint('kia', __name__, url_prefix='/masini/kia')

@kia_bp.route('/', methods=['GET'])
def index():
    return """
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Kia</h1>
        <p>Kia este un producator sud-coreean de automobile fondat in 1944.</p>
        <ul>
            <li><a href="/masini/kia/modele">Modele Kia</a></li>
        </ul>
        <h2>Cauta detalii model</h2>
        <form action="/masini/kia/detalii" method="get">
            <input type="text" name="model" placeholder="Ex: sportage" style="padding:8px; font-size:16px;"/>
            <button type="submit" style="padding:8px 16px; font-size:16px; cursor:pointer;">Cauta</button>
        </form>
    </body>
    </html>
    """


@kia_bp.route('/modele', methods=['GET'])
def modele():
    data= modele_kia()

    if not data:
        return 'Nu a fost gasit niciun model', 500

    res= f''
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
        <h1>Modele Kia</h1>
        {res}
        <br>
        <a href="/masini/kia"> Inapoi la Kia</a>
    </body>
    </html>
    """


@kia_bp.route('/detalii', methods=['GET'])
def detalii():
    model= request.args.get('model', '')

    if not model:
        return f'Specifica un model: /masini/kia/detalii?model=sportage', 400

    data= detalii_kia(model=model)

    if not data:
        return f'Nu a fost gasit niciun rezultat pentru modelul: {model}', 404

    return f"""
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Detalii {data.get('year')} Kia {data.get('model').title()}</h1>
        <div style="border:1px solid #ddd; border-radius:8px; padding:16px;">
            <p>Clasa: {data.get('class').title()}</p>
            <p>Cilindri: {data.get('cylinders')}</p>
            <p>Cilindree: {data.get('displacement')}L</p>
            <p>Tractiune: {data.get('drive').upper()}</p>
            <p>Combustibil: {data.get('fuel_type')}</p>
            <p>Transmisie: {data.get('transmission').upper()}</p>
        </div>
        <br>
        <a href="/masini/kia"> Inapoi la Kia</a>
    </body>
    </html>
    """