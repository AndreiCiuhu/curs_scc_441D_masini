from flask import Blueprint, redirect

from app.lib.biblioteca_masini import (
    descriere_renault,
    detalii_model_renault,
    modele_renault,
)


renault_bp = Blueprint("renault", __name__)


def pagina_html(titlu: str, continut: str) -> str:
    return f"""
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            margin: 0;
            padding: 0;
        }}

        header {{
            background-color: #facc15;
            color: #111827;
            padding: 20px;
            text-align: center;
        }}

        main {{
            max-width: 950px;
            margin: 30px auto;
            background-color: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}

        h1 {{
            margin-top: 0;
        }}

        h2 {{
            color: #111827;
            margin-bottom: 10px;
        }}

        h3 {{
            margin-top: 25px;
            color: #1f2937;
        }}

        p, li {{
            font-size: 17px;
            line-height: 1.6;
        }}

        ul {{
            padding-left: 25px;
        }}

        .buttons {{
            margin-top: 25px;
        }}

        .button {{
            display: inline-block;
            margin: 8px;
            padding: 12px 18px;
            background-color: #facc15;
            color: #111827;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
        }}

        .button:hover {{
            background-color: #eab308;
        }}

        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }}

        .card {{
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 18px;
            background-color: #f9fafb;
        }}

        .card h3 {{
            margin-top: 0;
        }}

        .section {{
            background-color: #f9fafb;
            border-left: 5px solid #facc15;
            padding: 15px;
            margin-top: 15px;
            border-radius: 6px;
        }}

        footer {{
            text-align: center;
            color: #6b7280;
            margin-top: 30px;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Proiect SCC - Renault</h1>
        <p>Aplicatie Flask containerizata cu Docker</p>
    </header>

    <main>
        {continut}
    </main>

    <footer>
        Florin Cernat - Renault
    </footer>
</body>
</html>
"""


def lista_html(elemente: list[str]) -> str:
    return "".join(f"<li>{element}</li>" for element in elemente)


@renault_bp.route("/masini")
def masini():
    continut = """
        <h2>Pagina principala - Renault</h2>
        <p>Aceasta aplicatie prezinta informatii despre masini. Pentru proiectul SCC a fost aleasa marca Renault.</p>

        <div class="buttons">
            <a class="button" href="/masini/renault">Vezi informatii despre Renault</a>
        </div>
    """
    return pagina_html("Masini", continut)


@renault_bp.route("/masini/renault")
def renault():
    continut = """
        <h2>Renault</h2>
        <p>Renault este marca aleasa pentru implementarea functionalitatii.</p>

        <div class="buttons">
            <a class="button" href="/masini">Inapoi la pagina principala</a>
            <a class="button" href="/masini/renault/descriere">Descriere Renault</a>
            <a class="button" href="/masini/renault/modele">Modele Renault</a>
        </div>
    """
    return pagina_html("Renault", continut)


@renault_bp.route("/masini/renault/descriere")
def renault_descriere():
    continut = f"""
        <h2>Descriere Renault</h2>
        <p>{descriere_renault()}</p>

        <div class="buttons">
            <a class="button" href="/masini/renault">Inapoi la Renault</a>
        </div>
    """
    return pagina_html("Descriere Renault", continut)


@renault_bp.route("/masini/renault/modele")
def renault_modele():
    carduri = ""

    for model_id, model in modele_renault().items():
        carduri += f"""
            <div class="card">
                <h3>{model["nume"]}</h3>
                <p>{model["descriere"]}</p>
                <a class="button" href="/masini/renault/modele/{model_id}">Vezi detalii</a>
            </div>
        """

    continut = f"""
        <h2>Modele Renault</h2>
        <p>Alege un model Renault pentru a vedea informatii despre culori, motorizari, dotari si utilizare recomandata.</p>

        <div class="card-grid">
            {carduri}
        </div>

        <div class="buttons">
            <a class="button" href="/masini/renault">Inapoi la Renault</a>
        </div>
    """
    return pagina_html("Modele Renault", continut)


@renault_bp.route("/masini/renault/modele/<model_id>")
def renault_model_detalii(model_id):
    model = detalii_model_renault(model_id)

    if model is None:
        continut = """
            <h2>Model indisponibil</h2>
            <p>Modelul cautat nu exista in catalogul Renault al proiectului.</p>

            <div class="buttons">
                <a class="button" href="/masini/renault/modele">Inapoi la Modele Renault</a>
            </div>
        """
        return pagina_html("Model indisponibil", continut), 404

    continut = f"""
        <h2>{model["nume"]}</h2>

        <div class="section">
            <h3>Tip caroserie</h3>
            <p>{model["tip_caroserie"]}</p>
        </div>

        <div class="section">
            <h3>Descriere</h3>
            <p>{model["descriere"]}</p>
        </div>

        <div class="section">
            <h3>Culori posibile</h3>
            <ul>
                {lista_html(model["culori"])}
            </ul>
        </div>

        <div class="section">
            <h3>Motorizari posibile</h3>
            <ul>
                {lista_html(model["motorizari"])}
            </ul>
        </div>

        <div class="section">
            <h3>Dotari posibile</h3>
            <ul>
                {lista_html(model["dotari"])}
            </ul>
        </div>

        <div class="section">
            <h3>Informatii generale</h3>
            <ul>
                {lista_html(model["informatii_generale"])}
            </ul>
        </div>

        <div class="buttons">
            <a class="button" href="/masini/renault/modele">Inapoi la Modele Renault</a>
            <a class="button" href="/masini/renault">Inapoi la Renault</a>
        </div>
    """
    return pagina_html(model["nume"], continut)


@renault_bp.route("/masini/renault/culoare")
def renault_culoare():
    return redirect("/masini/renault/modele")


@renault_bp.route("/masini/renault/dotari")
def renault_dotari():
    return redirect("/masini/renault/modele")
