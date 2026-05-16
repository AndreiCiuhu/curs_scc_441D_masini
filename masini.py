"""Aplicatie Flask pentru tema Masini - Lamborghini."""

from flask import Flask

from app.routes.lamborghini import lamborghini_bp
from app.routes.test import test_bp

app = Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(lamborghini_bp)

CSS = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: #f0f2f5;
        padding: 20px;
        text-align: center;
    }
    .card {
        background: white;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        max-width: 500px;
        margin: 50px auto;
    }
    .btn {
        display: inline-block;
        padding: 12px 24px;
        background: #d4af37;
        color: #111;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        margin-top: 20px;
    }
    .btn:hover { background: #b89022; }
    h1 { color: #333; margin-bottom: 5px; }
    h3 { color: #666; margin-top: 0; margin-bottom: 20px; font-weight: normal; }
</style>
"""


@app.route('/')
def index():
    """Afiseaza pagina principala cu meniul aplicatiei."""
    return f"""
    {CSS}
    <div class="card">
        <h1>Proiect SCC - Masini</h1>
        <h3>Grupa 441D</h3>
        <p>Alege o marca pentru a vedea detaliile implementate:</p>
        <a href="/masini/lamborghini" class="btn">Vezi pagina Lamborghini</a>
    </div>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
