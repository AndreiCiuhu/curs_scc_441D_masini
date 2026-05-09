from flask import Blueprint
from app.lib.biblioteca_masini import descriere_honda, istoric_honda, modele_honda

honda_bp = Blueprint("honda", __name__, url_prefix="/masini/honda")


@honda_bp.route("/")
def honda_home():
    return """
    <h1>Honda</h1>
    <p>Honda este o marca japoneza cunoscuta pentru masini fiabile, eficiente si practice.</p>

    <ul>
        <li><a href="/masini/honda/istoric">Istoric Honda</a></li>
        <li><a href="/masini/honda/modele">Modele Honda</a></li>
    </ul>
    """


@honda_bp.route("/istoric")
def honda_istoric():
    return f"""
    <h1>Istoric Honda</h1>
    <p>{istoric_honda()}</p>
    <a href="/masini/honda/">Inapoi la pagina Honda</a>
    """


@honda_bp.route("/modele")
def honda_modele():
    return f"""
    <h1>Modele Honda</h1>
    <p>{modele_honda()}</p>
    <a href="/masini/honda/">Inapoi la pagina Honda</a>
    """
