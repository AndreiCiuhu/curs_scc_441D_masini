from flask import Blueprint, request
from app.lib.biblioteca_masini import modele_bmw, detalii_bmw

modul_rutare_bmw = Blueprint('sectiune_bmw', __name__, url_prefix='/masini/bmw')

STYLE_CSS = """
<style>
    body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #2c3e50; margin: 0; padding: 30px 15px; }
    .container { max-width: 850px; margin: 0 auto; background: #ffffff; padding: 30px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
    h1 { color: #0066B1; border-bottom: 2px solid #ecf0f1; padding-bottom: 15px; margin-top: 0; }
    h2 { color: #34495e; font-size: 1.2rem; }
    .btn { display: inline-block; background-color: #0066B1; color: white; padding: 10px 20px; text-decoration: none; border-radius: 6px; font-weight: 600; transition: all 0.3s ease; border: none; cursor: pointer; }
    .btn:hover { background-color: #004c85; transform: translateY(-2px); box-shadow: 0 4px 10px rgba(0,102,177,0.2); }
    .btn-secondary { background-color: #95a5a6; margin-top: 20px; }
    .btn-secondary:hover { background-color: #7f8c8d; }
    .grid-modele { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; margin-top: 20px; }
    .card { border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px; transition: transform 0.2s, box-shadow 0.2s; border-top: 4px solid #0066B1; background: #fff; }
    .card:hover { transform: translateY(-5px); box-shadow: 0 8px 15px rgba(0,0,0,0.1); }
    .card p { margin: 8px 0; color: #555; }
    .search-box { display: flex; gap: 10px; margin-top: 15px; }
    input[type="text"] { flex: 1; max-width: 300px; padding: 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px; outline: none; }
</style>
"""

@modul_rutare_bmw.route('/', methods=['GET'])
def start_bmw():
    return f"""
    <html><head><title>Portal BMW</title>{STYLE_CSS}</head>
    <body>
        <div class="container">
            <h1>Platforma Date Tehnice BMW</h1>
            <p>Bayerische Motoren Werke AG, cunoscut sub numele de BMW, este un producator german multinațional.</p>
            <div style="margin: 30px 0; padding: 20px; background: #f8fafc; border-radius: 8px; border-left: 4px solid #0066B1;">
                <h2>Exploreaza Flota</h2>
                <a href="/masini/bmw/modele" class="btn">Vezi toate modelele disponibile</a>
            </div>
            <h2>Cautare avansata model</h2>
            <form action="/masini/bmw/detalii" method="get" class="search-box">
                <input type="text" name="model" placeholder="Introdu un model (ex: x5, m3, i8)" required/>
                <button type="submit" class="btn">Cauta Specificatii</button>
            </form>
        </div>
    </body></html>
    """

@modul_rutare_bmw.route('/modele', methods=['GET'])
def catalog_masini():
    # Variabile noi
    informatii_api = modele_bmw()

    # Logica diferita (evitam if not data return error direct)
    if informatii_api:
        elemente_html = [
            f"""<div class="card">
                <h2 style="margin-top: 0; color: #0066B1;">{v.get('year')} {v.get('make')} {v.get('model').upper()}</h2>
                <p><strong>Motor:</strong> {v.get('displacement')}L</p>
                <p><strong>Combustibil:</strong> {v.get('fuel_type').title()}</p>
                <p><strong>Transmisie:</strong> {v.get('transmission')}</p>
                <p><strong>Putere:</strong> {v.get('horsepower')} CP</p>
            </div>""" for v in informatii_api
        ]
        bloc_modele = f'<div class="grid-modele">{"".join(elemente_html)}</div>'
    else:
        return 'Eroare de retea: Nu s-a putut incarca catalogul BMW.', 500

    return f"""
    <html><head><title>Modele BMW</title>{STYLE_CSS}</head>
    <body>
        <div class="container">
            <h1>Catalog Modele BMW</h1>
            {bloc_modele}
            <a href="/masini/bmw" class="btn btn-secondary">Inapoi la pagina principala</a>
        </div>
    </body></html>
    """

@modul_rutare_bmw.route('/detalii', methods=['GET'])
def fisa_specifica():
    parametru_cautare = request.args.get('model', '').strip()

    if parametru_cautare == '':
        return 'Lipseste indicativul modelului in URL (Exemplu: ?model=x5)', 400

    date_tehnice = detalii_bmw(model=parametru_cautare)

    
    if date_tehnice is None or len(date_tehnice) == 0:
        return f"""
        <html><head>{STYLE_CSS}</head><body><div class="container">
        <h2 style="color: #e74c3c;">Rezultat Nul</h2>
        <p>Sistemul nu a returnat date pentru indicativul: <b>{parametru_cautare}</b>.</p>
        <a href="/masini/bmw" class="btn btn-secondary">Incearca din nou</a>
        </div></body></html>
        """, 404

    return f"""
    <html><head><title>Fisa BMW</title>{STYLE_CSS}</head>
    <body>
        <div class="container">
            <h1>Fisa Tehnica: {date_tehnice.get('year')} BMW {date_tehnice.get('model').upper()}</h1>
            <div style="background: #fff; padding: 20px; border-radius: 8px; border: 1px solid #e2e8f0; margin-top: 20px;">
                <table style="width: 100%; border-collapse: collapse; text-align: left;">
                    <tr style="border-bottom: 1px solid #edf2f7;"><th style="padding: 12px 0;">Clasa Vehicul</th><td style="font-weight: bold;">{date_tehnice.get('class').title()}</td></tr>
                    <tr style="border-bottom: 1px solid #edf2f7;"><th style="padding: 12px 0;">Numar Cilindri</th><td style="font-weight: bold;">{date_tehnice.get('cylinders')}</td></tr>
                    <tr style="border-bottom: 1px solid #edf2f7;"><th style="padding: 12px 0;">Capacitate Cilindrica</th><td style="font-weight: bold;">{date_tehnice.get('displacement')} L</td></tr>
                    <tr style="border-bottom: 1px solid #edf2f7;"><th style="padding: 12px 0;">Tip Tractiune</th><td style="font-weight: bold;">{date_tehnice.get('drive').upper()}</td></tr>
                    <tr style="border-bottom: 1px solid #edf2f7;"><th style="padding: 12px 0;">Combustibil</th><td style="font-weight: bold;">{date_tehnice.get('fuel_type').title()}</td></tr>
                    <tr><th style="padding: 12px 0;">Cutie de Viteze</th><td style="font-weight: bold;">{date_tehnice.get('transmission').upper()}</td></tr>
                </table>
            </div>
            <a href="/masini/bmw" class="btn btn-secondary">Inapoi</a>
        </div>
    </body></html>
    """
