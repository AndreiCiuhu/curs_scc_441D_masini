from flask import Blueprint

from lib.biblioteca_masini import descriere_porsche, modele_porsche, istorie_porsche_911

porsche_bp = Blueprint("porsche", __name__, url_prefix="/masini/porsche")


def pagina(titlu, continut):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{titlu}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 0 20px;
                background: white;
                color: black;
            }}

            nav {{
                margin-bottom: 30px;
                border-bottom: 1px solid #cccccc;
                padding-bottom: 10px;
            }}

            nav a {{
                margin-right: 15px;
                color: black;
                text-decoration: none;
                font-weight: bold;
            }}

            nav a:hover {{
                text-decoration: underline;
            }}

            h1 {{
                font-size: 36px;
                margin-bottom: 10px;
            }}

            h2 {{
                margin-top: 30px;
            }}

            .box {{
                border: 1px solid #cccccc;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 4px;
            }}

            p {{
                line-height: 1.5;
            }}
        </style>
    </head>

    <body>
        <nav>
            <a href="/masini/porsche">Porsche</a>
            <a href="/masini/porsche/modele">Modele</a>
        </nav>

        {continut}
    </body>
    </html>
    """


@porsche_bp.route("/")
def porsche():
    continut = f"""
    <h1>Porsche</h1>

    <div class="box">
        <h2>Descriere</h2>
        <p>{descriere_porsche()}</p>
    </div>

    <div class="box">
        <h2>1. Modelele Porsche</h2>
        <p>
            Aceasta sectiune prezinta cateva modele importante Porsche,
            impreuna cu detalii precum motor, putere, tractiune si combustibil.
        </p>
        <p>
            <a href="/masini/porsche/modele">Vezi modelele Porsche</a>
        </p>
    </div>

    <div class="box">
        <h2>2. Istoria Porsche 911</h2>
        <p>
            Aceasta sectiune prezinta cateva generatii emblematice ale modelului Porsche 911,
            unul dintre cele mai cunoscute automobile sport din lume.
        </p>
        <p>
            <a href="/masini/porsche/istorie-911">Vezi istoria Porsche 911</a>
        </p>
    </div>

    """

    return pagina("Porsche", continut)


@porsche_bp.route("/modele")
def modele():
    masini = modele_porsche()

    continut = """
    <h1>Modele Porsche</h1>

    <p>
        Mai jos sunt afisate cateva modele Porsche, impreuna cu detaliile lor principale.
    </p>
    """

    for masina in masini:
        continut += f"""
        <div class="box">
            <h2>{masina["marca"]} {masina["model"]}</h2>

            <p><strong>An:</strong> {masina["an"]}</p>
            <p><strong>Categorie:</strong> {masina["categorie"]}</p>
            <p><strong>Motor:</strong> {masina["motor"]}</p>
            <p><strong>Putere:</strong> {masina["putere"]}</p>
            <p><strong>Tractiune:</strong> {masina["tractiune"]}</p>
            <p><strong>Combustibil:</strong> {masina["combustibil"]}</p>
        </div>
        """

    return pagina("Modele Porsche", continut)

@porsche_bp.route("/istorie-911")
def istorie_911():
    generatii = istorie_porsche_911()

    continut = """
    <h1>Istoria Porsche 911</h1>

    <p>
        Porsche 911 este unul dintre cele mai importante modele din istoria marcii Porsche.
        De-a lungul timpului, modelul a pastrat forma generala si ideea de masina sport,
        dar a primit imbunatatiri majore la nivel tehnic si tehnologic.
    </p>
    """

    for generatie in generatii:
        continut += f"""
        <div class="box">
            <h2>{generatie["generatie"]}</h2>
            <p><strong>Perioada:</strong> {generatie["perioada"]}</p>
            <p>{generatie["descriere"]}</p>
        </div>
        """

    return pagina("Istoria Porsche 911", continut)
