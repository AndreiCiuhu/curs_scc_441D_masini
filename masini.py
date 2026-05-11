from flask import Flask

from app.routes.test import test_bp
from app.routes.volvo import volvo_bp

app= Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(volvo_bp)

@app.route('/')
def index():
    return """
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">
        <h1>Proiect SCC - 441D - Masini</h1>
        <p>Alegeti o marca:</p>
        <ul>
            <li><a href="/masini/volvo">Volvo</a></li>
        </ul>
    </body>
    </html>
    """