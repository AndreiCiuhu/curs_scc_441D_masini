from flask import Blueprint
from app.lib.biblioteca_masini import descriere_honda, istoric_honda, modele_honda

honda_bp = Blueprint("honda", __name__, url_prefix="/masini/honda")


def pagina_honda(titlu, subtitlu, continut):
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>{titlu}</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #111111, #2b2b2b);
                color: #f5f5f5;
            }}

            .container {{
                width: 85%;
                max-width: 1000px;
                margin: 60px auto;
                background: #ffffff;
                color: #222222;
                border-radius: 18px;
                overflow: hidden;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
            }}

            .header {{
                background: linear-gradient(135deg, #cc0000, #8b0000);
                padding: 45px;
                text-align: center;
                color: white;
            }}

            .brand {{
                font-size: 18px;
                letter-spacing: 5px;
                text-transform: uppercase;
                opacity: 0.9;
            }}

            h1 {{
                margin: 15px 0 10px;
                font-size: 46px;
            }}

            .subtitle {{
                font-size: 18px;
                opacity: 0.95;
            }}

            .content {{
                padding: 40px;
                line-height: 1.7;
                font-size: 18px;
            }}

            .cards {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }}

            .card {{
                background: #f4f4f4;
                border-left: 5px solid #cc0000;
                padding: 22px;
                border-radius: 12px;
            }}

            .card h3 {{
                margin-top: 0;
                color: #cc0000;
            }}

            .nav {{
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
                margin-top: 30px;
            }}

            .nav a {{
                text-decoration: none;
                background: #cc0000;
                color: white;
                padding: 12px 18px;
                border-radius: 8px;
                font-weight: bold;
            }}

            .nav a:hover {{
                background: #990000;
            }}

            .footer {{
                text-align: center;
                padding: 20px;
                background: #eeeeee;
                color: #555555;
                font-size: 14px;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <div class="header">
                <div class="brand">Proiect SCC - Masini</div>
                <h1>{titlu}</h1>
                <div class="subtitle">{subtitlu}</div>
            </div>

            <div class="content">
                {continut}
            </div>

            <div class="footer">
                Anton Darius | Grupa 441D | Marca aleasa: Honda
            </div>
        </div>
    </body>
    </html>
    """


@honda_bp.route("/")
def honda_home():
    continut = """
        <p>
            Honda este o marca japoneza cunoscuta pentru masini fiabile,
            eficiente si practice. In aceasta sectiune sunt prezentate cateva
            informatii despre marca Honda, istoricul acesteia si cateva modele
            reprezentative.
        </p>

        <div class="cards">
            <div class="card">
                <h3>Fiabilitate</h3>
                <p>Honda este apreciata pentru masini durabile si costuri bune de intretinere.</p>
            </div>

            <div class="card">
                <h3>Eficienta</h3>
                <p>Modelele Honda sunt cunoscute pentru motoare eficiente si consum echilibrat.</p>
            </div>

            <div class="card">
                <h3>Modele populare</h3>
                <p>Civic, Accord, CR-V, HR-V si Jazz sunt printre cele mai cunoscute modele.</p>
            </div>
        </div>

        <div class="nav">
            <a href="/masini/honda/istoric">Vezi istoricul Honda</a>
            <a href="/masini/honda/modele">Vezi modelele Honda</a>
        </div>
    """

    return pagina_honda(
        "Honda",
        "Marca japoneza orientata spre fiabilitate, eficienta si tehnologie practica.",
        continut
    )


@honda_bp.route("/istoric")
def honda_istoric():
    continut = f"""
        <p>{istoric_honda()}</p>

        <div class="cards">
            <div class="card">
                <h3>Origine</h3>
                <p>Honda a aparut in Japonia si s-a dezvoltat initial prin productia de motociclete.</p>
            </div>

            <div class="card">
                <h3>Extindere</h3>
                <p>Ulterior, compania a intrat puternic in industria auto internationala.</p>
            </div>

            <div class="card">
                <h3>Imagine globala</h3>
                <p>Astazi, Honda este o marca recunoscuta la nivel mondial pentru fiabilitate.</p>
            </div>
        </div>

        <div class="nav">
            <a href="/masini/honda/">Inapoi la Honda</a>
            <a href="/masini/honda/modele">Vezi modelele</a>
        </div>
    """

    return pagina_honda(
        "Istoric Honda",
        "O scurta prezentare a evolutiei marcii Honda.",
        continut
    )


@honda_bp.route("/modele")
def honda_modele():
    continut = f"""
        <p>{modele_honda()}</p>

        <div class="cards">
            <div class="card">
                <h3>Honda Civic</h3>
                <p>Model compact, popular pentru fiabilitate si utilizare zilnica.</p>
            </div>

            <div class="card">
                <h3>Honda Accord</h3>
                <p>Sedan confortabil, potrivit pentru drumuri lungi si utilizare familiala.</p>
            </div>

            <div class="card">
                <h3>Honda CR-V</h3>
                <p>SUV practic, apreciat pentru spatiu, confort si versatilitate.</p>
            </div>
        </div>

        <div class="nav">
            <a href="/masini/honda/">Inapoi la Honda</a>
            <a href="/masini/honda/istoric">Vezi istoricul</a>
        </div>
    """

    return pagina_honda(
        "Modele Honda",
        "Cateva dintre cele mai cunoscute modele produse de Honda.",
        continut
    )
