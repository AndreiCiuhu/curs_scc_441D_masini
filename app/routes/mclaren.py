from flask import Blueprint

from app.lib.biblioteca_masini import culoare_mclaren, descriere_mclaren


mclaren_bp = Blueprint("mclaren", __name__)


@mclaren_bp.route("/masini/mclaren", methods=["GET"])
def mclaren():
    return """
    <h1>McLaren</h1>
    <p>Elementul ales pentru proiect este marca McLaren.</p>
    <p>In aceasta sectiune sunt prezentate informatii despre culoare si descriere.</p>
    <ul>
        <li><a href="/masini/mclaren/culoare">Culoare McLaren</a></li>
        <li><a href="/masini/mclaren/descriere">Descriere McLaren</a></li>
    </ul>
    """


@mclaren_bp.route("/masini/mclaren/culoare", methods=["GET"])
def ruta_culoare_mclaren():
    return f"""
    <h1>Culoare McLaren</h1>
    <p>{culoare_mclaren()}</p>
    <p><a href="/masini/mclaren">Inapoi la McLaren</a></p>
    """


@mclaren_bp.route("/masini/mclaren/descriere", methods=["GET"])
def ruta_descriere_mclaren():
    return f"""
    <h1>Descriere McLaren</h1>
    <p>{descriere_mclaren()}</p>
    <p><a href="/masini/mclaren">Inapoi la McLaren</a></p>
    """
