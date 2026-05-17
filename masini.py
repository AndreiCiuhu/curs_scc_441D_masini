from flask import Flask
from routes.test import test_bp
from routes.ferrari import ferrari_bp

app = Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(ferrari_bp)

@app.route('/')
def index():
    return """
    <html>
    <body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px; background-color:#ffffff; color:#1a1a1a;">
        <h1 style="color:#cc0000; letter-spacing:3px; border-bottom:3px solid #cc0000; padding-bottom:10px;">Proiect SCC - 441D - Masini</h1>
        <p style="font-size:1.1rem; margin:20px 0 10px;">Alegeti o marca:</p>
        <ul style="list-style:none; padding:0;">
            <li>
                <a href="/masini/ferrari" style="display:inline-block; background-color:#cc0000; color:white; text-decoration:none; padding:10px 24px; border-radius:4px; font-weight:bold; letter-spacing:2px; margin:6px 0;">
                    Ferrari
                </a>
            </li>
        </ul>
    </body>
    </html>
    """
