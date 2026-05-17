from flask import Blueprint

from app.lib.biblioteca_masini import (
    culoare_renault,
    descriere_renault,
    dotari_renault,
    modele_renault,
)

renault_bp = Blueprint("renault", __name__)


@renault_bp.route("/masini")
def masini():
    return "Pagina principala pentru tema Masini."


@renault_bp.route("/masini/renault")
def renault():
    return "Pagina dedicata marcii Renault."


@renault_bp.route("/masini/renault/culoare")
def renault_culoare():
    return culoare_renault()


@renault_bp.route("/masini/renault/descriere")
def renault_descriere():
    return descriere_renault()

@renault_bp.route("/masini/renault/dotari")
def renault_dotari():
    return dotari_renault()


@renault_bp.route("/masini/renault/modele")
def renault_modele():
    return modele_renault()
