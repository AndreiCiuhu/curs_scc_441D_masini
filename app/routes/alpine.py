from flask import Blueprint
from app.lib.biblioteca_masini import culoare_alpine, descriere_alpine, modele_alpine

alpine_bp = Blueprint("alpine", __name__)

stil_css = """
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f6f8;
        margin: 0;
        padding: 40px;
        color: #222;
    }

    .container {
        max-width: 900px;
        margin: auto;
        background: white;
        padding: 35px;
        border-radius: 12px;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
    }

    h1 {
        color: #0055a4;
        margin-bottom: 10px;
    }

    h2 {
        color: #003d7a;
        margin-top: 30px;
    }

    p {
        font-size: 17px;
        line-height: 1.6;
    }

    .buttons {
        margin-top: 25px;
    }

    .btn {
        display: inline-block;
        padding: 10px 18px;
        margin: 6px;
        background-color: #0055a4;
        color: white;
        text-decoration: none;
        border-radius: 6px;
    }

    .btn:hover {
        background-color: #003d7a;
    }

    .btn-secondary {
        background-color: #666;
    }

    .card {
        background-color: #f8f9fb;
        border-left: 5px solid #0055a4;
        padding: 18px;
        margin: 15px 0;
        border-radius: 8px;
    }

    .card h3 {
        margin-top: 0;
        color: #0055a4;
    }

    ul {
        font-size: 17px;
        line-height: 1.8;
    }
</style>
"""


@alpine_bp.route("/masini")
def pagina_masini():
    return f"""
    {stil_css}
    <div class="container">
        <h1>Mașini sport și mărci auto</h1>

        <p>
            Industria auto include numeroase mărci specializate în performanță,
            design și tehnologii moderne. Unele mărci sunt orientate spre confort,
            altele spre utilitate, iar altele spre experiențe sportive de condus.
        </p>

        <p>
            Alpine face parte din categoria mărcilor auto sportive, fiind cunoscută
            pentru automobile ușoare, agile și construite pentru plăcerea condusului.
        </p>

        <div class="card">
            <h3>Alpine</h3>
            <p>
                Marcă franceză de automobile sport, asociată cu performanța,
                motorsportul și modelul emblematic Alpine A110.
            </p>
        </div>

        <div class="buttons">
            <a class="btn" href="/masini/alpine">Vezi prezentarea Alpine</a>
            <a class="btn btn-secondary" href="/">Înapoi la pagina principală</a>
        </div>
    </div>
    """


@alpine_bp.route("/masini/alpine")
def pagina_alpine():
    return f"""
    {stil_css}
    <div class="container">
        <h1>Alpine</h1>

        <p>
            Alpine este o marcă franceză de automobile sport, recunoscută pentru
            modele compacte, greutate redusă și comportament dinamic. Marca este
            apreciată pentru modul în care combină designul elegant cu performanța.
        </p>

        <div class="card">
            <h3>Origine</h3>
            <p>Franța</p>
        </div>

        <div class="card">
            <h3>Segment</h3>
            <p>Automobile sport compacte</p>
        </div>

        <div class="card">
            <h3>Model reprezentativ</h3>
            <p>Alpine A110</p>
        </div>

        <h2>Informații disponibile</h2>

        <div class="buttons">
            <a class="btn" href="/masini/alpine/culoare">Culori Alpine</a>
            <a class="btn" href="/masini/alpine/descriere">Descriere Alpine</a>
            <a class="btn" href="/masini/alpine/modele">Modele Alpine</a>
        </div>

        <br>
        <a class="btn btn-secondary" href="/masini">Înapoi la mașini</a>
        <a class="btn btn-secondary" href="/">Pagina principală</a>
    </div>
    """


@alpine_bp.route("/masini/alpine/culoare")
def pagina_culoare_alpine():
    return f"""
    {stil_css}
    <div class="container">
        <h1>Culori Alpine</h1>

        <p>{culoare_alpine()}</p>

        <div class="card">
            <h3>Bleu Alpine</h3>
            <p>
                Culoarea emblematică a mărcii, asociată cu identitatea sportivă Alpine.
            </p>
        </div>

        <div class="card">
            <h3>Noir Profond</h3>
            <p>
                O culoare elegantă, potrivită pentru un aspect sobru și sportiv.
            </p>
        </div>

        <div class="card">
            <h3>Blanc Irisé</h3>
            <p>
                O variantă luminoasă și modernă, care evidențiază liniile caroseriei.
            </p>
        </div>

        <br>
        <a class="btn btn-secondary" href="/masini/alpine">Înapoi la Alpine</a>
    </div>
    """


@alpine_bp.route("/masini/alpine/descriere")
def pagina_descriere_alpine():
    return f"""
    {stil_css}
    <div class="container">
        <h1>Descriere Alpine</h1>

        <p>{descriere_alpine()}</p>

        <div class="card">
            <h3>Performanță</h3>
            <p>
                Modelele Alpine sunt construite pentru agilitate, greutate redusă
                și răspuns rapid la comenzi.
            </p>
        </div>

        <div class="card">
            <h3>Design</h3>
            <p>
                Designul Alpine combină elemente moderne cu influențe din modelele
                clasice ale mărcii.
            </p>
        </div>

        <div class="card">
            <h3>Experiență de condus</h3>
            <p>
                Mașinile Alpine sunt orientate spre șofer și oferă o experiență
                sportivă, dar utilizabilă și pe drumurile publice.
            </p>
        </div>

        <br>
        <a class="btn btn-secondary" href="/masini/alpine">Înapoi la Alpine</a>
    </div>
    """


@alpine_bp.route("/masini/alpine/modele")
def pagina_modele_alpine():
    modele = modele_alpine()

    cards = ""
    for model in modele:
        cards += f"""
        <div class="card">
            <h3>{model["nume"]}</h3>
            <p>{model["descriere"]}</p>
            <p><b>Caracteristici:</b> {model["caracteristici"]}</p>
        </div>
        """

    return f"""
    {stil_css}
    <div class="container">
        <h1>Modele Alpine</h1>

        <p>
            Alpine are în gamă mai multe versiuni ale modelului A110, fiecare
            fiind orientată către un anumit tip de experiență: confort, sportivitate
            sau performanță maximă.
        </p>

        {cards}

        <br>
        <a class="btn btn-secondary" href="/masini/alpine">Înapoi la Alpine</a>
    </div>
    """