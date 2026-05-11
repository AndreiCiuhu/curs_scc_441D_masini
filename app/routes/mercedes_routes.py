from flask import Blueprint, render_template
from app.lib.biblioteca_masini import descriere_mercedes, origine_mercedes, motorizare_mercedes

mercedes_bp = Blueprint("mercedes", __name__)


@mercedes_bp.route("/masini/mercedes")
def mercedes_home():
    return render_template(
        "mercedes.html",
        titlu="Mercedes-Benz",
        subtitlu="Proiect Flask pentru tema Masini",
        sectiune="Prezentare",
        continut=(
            "Mercedes-Benz este o marca auto germana asociata cu eleganta, "
            "confortul, siguranta si tehnologia avansata."
        )
    )


@mercedes_bp.route("/masini/mercedes/descriere")
def mercedes_descriere():
    return render_template(
        "mercedes.html",
        titlu="Mercedes-Benz",
        subtitlu="Proiect Flask pentru tema Masini",
        sectiune="Descriere Mercedes-Benz",
        continut=descriere_mercedes()
    )


@mercedes_bp.route("/masini/mercedes/origine")
def mercedes_origine():
    return render_template(
        "mercedes.html",
        titlu="Mercedes-Benz",
        subtitlu="Proiect Flask pentru tema Masini",
        sectiune="Origine Mercedes-Benz",
        continut=origine_mercedes()
    )


@mercedes_bp.route("/masini/mercedes/motorizare")
def mercedes_motorizare():
    return render_template(
        "mercedes.html",
        titlu="Mercedes-Benz",
        subtitlu="Proiect Flask pentru tema Masini",
        sectiune="Motorizare Mercedes-Benz",
        continut=motorizare_mercedes()
    )
