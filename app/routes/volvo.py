from flask import Blueprint, request

from app.lib.biblioteca_masini import (
    modele_volvo,
    detalii_volvo,
)

volvo_bp= Blueprint('volvo', __name__, url_prefix='/masini/volvo')

@volvo_bp.route('/', methods=['GET'])
def index():
    return """
    <html>
    <body style="font-family: 'Trebuchet MS', Helvetica, sans-serif; max-width: 600px; margin: 40px auto; color: #333; padding: 0 20px;">
        <h1 style="color: #003366;">Descopera Volvo</h1>
        <p style="line-height: 1.5; font-size: 1.1em;">
            Volvo este sinonim cu siguranța și inovația. Explorati gama noastra de vehicule premium suedeze.
        </p>
        <br>
        <a href="/masini/volvo/modele" style="color: #0055a4; text-decoration: none; font-weight: bold;">&gt; Vezi Modelele Disponibile</a>
    </body>
    </html>
    """

@volvo_bp.route('/modele', methods=['GET'])
def modele():
    data= modele_volvo()

    if not data:
        return 'Nu a fost gasit niciun model Volvo', 500

    res= f''
    for masina in data:
        res += f"""
        <div style="margin-bottom: 15px; padding-bottom: 10px; border-bottom: 1px dashed #ccc;">
            <h3 style="margin: 0 0 5px 0;">{masina}</h3>
            <a href="/masini/volvo/detalii?model={masina}" style="color: #0055a4; text-decoration: none;">Mai multe detalii...</a>
        </div>
        """

    return f"""
    <html>
    <body style="font-family: 'Trebuchet MS', Helvetica, sans-serif; max-width: 600px; margin: 40px auto; color: #333; padding: 0 20px;">
        <h1 style="color: #003366;">Gama de Modele Volvo</h1>
        <hr style="border: 1px solid #eee; margin-bottom: 20px;">
        {res}
        <br><br>
        <a href="/masini/volvo" style="color: #666; text-decoration: none;">&laquo; Inapoi la pagina principala</a>
    </body>
    </html>
    """

@volvo_bp.route('/detalii', methods=['GET'])
def detalii():
    model= request.args.get('model', '')

    if not model:
        return f'Specifica un model: /masini/volvo/detalii?model=XC60', 400

    data= detalii_volvo(nume_model=model)

    if "eroare" in data:
        return data["eroare"], 404

    return f"""
    <html>
    <body style="font-family: 'Trebuchet MS', Helvetica, sans-serif; max-width: 600px; margin: 40px auto; color: #333; padding: 0 20px;">
        <h1 style="color: #003366;">Detalii Volvo {model.upper()}</h1>
        <div style="background-color: #f9f9f9; padding: 15px; border: 1px solid #ddd;">
            <p><strong>Categorie:</strong> {data.get('tip')}</p>
            <p style="line-height: 1.5;"><strong>Prezentare generala:</strong><br>{data.get('descriere')}</p>
        </div>
        <br><br>
        <a href="/masini/volvo/modele" style="color: #666; text-decoration: none;">&laquo; Inapoi la lista de modele</a>
    </body>
    </html>
    """