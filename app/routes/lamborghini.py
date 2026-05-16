"""Rute Flask pentru marca Lamborghini."""

from flask import Blueprint

from app.lib.biblioteca_masini import culoare_lamborghini, descriere_lamborghini

lamborghini_bp = Blueprint('lamborghini', __name__)

STIL_CSS = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        text-align: center;
        padding: 50px;
    }
    h1 { color: #111; }
    .container {
        background-color: #fff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        max-width: 650px;
        margin: auto;
    }
    a {
        display: inline-block;
        margin: 10px;
        padding: 10px 20px;
        background-color: #d4af37;
        color: #111;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
    }
    a:hover { background-color: #b89022; }
    .btn-inapoi {
        background-color: #6c757d;
        color: white;
    }
    .btn-inapoi:hover { background-color: #5a6268; }
</style>
"""


@lamborghini_bp.route('/masini')
def pagina_temei():
    """Afiseaza pagina temei Masini."""
    return f"""
    {STIL_CSS}
    <div class="container">
        <h1>Pagina temei: Masini</h1>
        <p>Aici gasiti informatii despre diverse marci auto.</p>
        <a href="/masini/lamborghini">Mergi la pagina Lamborghini</a>
    </div>
    """


@lamborghini_bp.route('/masini/lamborghini')
def pagina_elementului():
    """Afiseaza pagina principala pentru Lamborghini."""
    return f"""
    {STIL_CSS}
    <div class="container">
        <h1>Marca Lamborghini</h1>
        <p>Bine ati venit la prezentarea producatorului auto Lamborghini!</p>
        <a href="/masini/lamborghini/culoare">Culori reprezentative</a>
        <a href="/masini/lamborghini/descriere">Descriere marca</a>
        <br><br>
        <a href="/masini" class="btn-inapoi">Inapoi la tema</a>
    </div>
    """


@lamborghini_bp.route('/masini/lamborghini/culoare')
def ruta_culoare():
    """Afiseaza culori reprezentative pentru Lamborghini."""
    text_culoare = culoare_lamborghini()
    return f"""
    {STIL_CSS}
    <div class="container">
        <h1>Culori Lamborghini</h1>
        <p><b>{text_culoare}</b></p>
        <a href="/masini/lamborghini" class="btn-inapoi">
            Inapoi la pagina Lamborghini
        </a>
    </div>
    """


@lamborghini_bp.route('/masini/lamborghini/descriere')
def ruta_descriere():
    """Afiseaza descrierea marcii Lamborghini."""
    text_descriere = descriere_lamborghini()
    return f"""
    {STIL_CSS}
    <div class="container">
        <h1>Descriere Lamborghini</h1>
        <p><i>{text_descriere}</i></p>
        <a href="/masini/lamborghini" class="btn-inapoi">
            Inapoi la pagina Lamborghini
        </a>
    </div>
    """
