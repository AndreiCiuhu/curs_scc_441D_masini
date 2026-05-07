from flask import Blueprint

from app.lib.biblioteca_masini import modele_kia

kia_bp= Blueprint('kia', __name__, url_prefix='/masini/kia')

@kia_bp.route('/', methods=['GET'])
def index():
    return f'Kia'

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
    </body>
    </html>
    """