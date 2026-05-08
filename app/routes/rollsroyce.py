from flask import Blueprint

from app.lib.biblioteca_masini import (
    descriere_rollsroyce,
    istoric_rollsroyce,
    motorizare_rollsroyce,
)


rollsroyce_bp = Blueprint("rollsroyce", __name__, url_prefix="/masini/rollsroyce")


@rollsroyce_bp.route("/")
def rollsroyce_index():
    descriere = descriere_rollsroyce()

    return f"""
<html>
<body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">

<h1>Rolls-Royce</h1>

<p><strong>Student:</strong> Neacsu Roxana</p>
<p><strong>Grupa:</strong> 441D</p>
<p><strong>Tema:</strong> Masini</p>

<p>{descriere}</p>

<h2>Informatii disponibile</h2>

<ul>
    <li><a href="/masini/rollsroyce/istoric">Istoric Rolls-Royce</a></li>
    <li><a href="/masini/rollsroyce/motorizare">Motorizare Rolls-Royce</a></li>
</ul>

<br>
<a href="/">Inapoi la pagina principala</a>

</body>
</html>
"""


@rollsroyce_bp.route("/istoric")
def rollsroyce_istoric():
    istoric = istoric_rollsroyce()

    return f"""
<html>
<body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">

<h1>Istoric Rolls-Royce</h1>

<p>{istoric}</p>

<br>
<a href="/masini/rollsroyce">Inapoi la Rolls-Royce</a>

</body>
</html>
"""


@rollsroyce_bp.route("/motorizare")
def rollsroyce_motorizare():
    motorizare = motorizare_rollsroyce()

    return f"""
<html>
<body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">

<h1>Motorizare Rolls-Royce</h1>

<p>{motorizare}</p>

<br>
<a href="/masini/rollsroyce">Inapoi la Rolls-Royce</a>

</body>
</html>
"""
