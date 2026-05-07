from flask import Blueprint
from app.lib.biblioteca_masini import culoare_mclaren, descriere_mclaren

mclaren_bp = Blueprint("mclaren_bp", __name__)


@mclaren_bp.route("/masini")
def masini():
    return """
    <h1>Tema proiectului: Masini</h1>
    <p>Aceasta aplicatie face parte din proiectul grupei 441D pentru tema Masini.</p>
    <p>Contributia mea individuala este reprezentata de marca McLaren.</p>
    """


@mclaren_bp.route("/masini/mclaren")
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


@mclaren_bp.route("/masini/mclaren/culoare")
def ruta_culoare_mclaren():
    return f"""
    <h1>Culoare McLaren</h1>
    <p>{culoare_mclaren()}</p>
    """


@mclaren_bp.route("/masini/mclaren/descriere")
def ruta_descriere_mclaren():
    return f"""
    <h1>Descriere McLaren</h1>
    <p>{descriere_mclaren()}</p>
    """
