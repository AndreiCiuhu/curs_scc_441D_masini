import sys

from flask import Flask, url_for
from app.lib import biblioteca_masini


app = Flask(__name__)

CSS = """
<style>
    body { font-family: sans-serif; background: #f0f2f5; padding: 20px; }
    .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); max-width: 600px; margin: auto; }
    .btn { display: inline-block; padding: 10px 15px; background: #007bff; color: white; text-decoration: none; border-radius: 5px; margin: 5px; }
    .btn-home { background: #6c757d; }
    pre { background: #e9ecef; padding: 15px; border-radius: 5px; overflow-x: auto; }
    h1 { color: #333; }
</style>
"""

@app.route("/", methods=['GET'])
def index():
    return f"""
    {CSS}
    <div class="card">
        <h1>Masini</h1>
        <h3>Proiect-SCC2026</h3>
        <p>Alege o marcă:</p>
        <a href="{url_for('audi')}" class="btn">Audi</a>
    </div>
    """
    
@app.route("/audi", methods=['GET'])
def audi():
    return f"""
    {CSS}
    <div class="card">
        <a href="{url_for('index')}" class="btn btn-home">🏠 Home</a>
        <h1>Gama Audi</h1>
        <p>Ce informații cauți?</p>
        <a href="{url_for('info_modele')}" class="btn">Vezi Modele</a>
        <a href="{url_for('info_motoare')}" class="btn">Vezi Motoare</a>
    </div>
    """
    
@app.route("/audi/model", methods=['GET'])
def info_modele():
    modele = biblioteca_masini.gaseste_informatii_modele()
    lista_modele = "\n".join(modele)
    
    return f"""
    {CSS}
    <div class="card">
        <a href="{url_for('index')}" class="btn btn-home">🏠 Home</a>
        <a href="{url_for('audi')}" class="btn">🔙 Inapoi</a>
        <h1>Modele Audi</h1>
        <pre>{lista_modele}</pre>
    </div>
    """
    
@app.route("/audi/motoare", methods=['GET'])
def info_motoare():
    motoare = biblioteca_masini.gaseste_informatii_motor()
    lista_motoare = "\n".join(motoare)
    
    return f"""
    {CSS}
    <div class="card">
        <a href="{url_for('index')}" class="btn btn-home">🏠 Home</a>
        <a href="{url_for('audi')}" class="btn">🔙 Inapoi</a>
        <h1>Motoare Audi</h1>
        <pre>{lista_motoare}</pre>
    </div>
    """


    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
