from flask import Flask
from app.routes.bentley import bentley_bp

app = Flask(__name__)
app.register_blueprint(bentley_bp)


@app.route("/", methods=["GET"])
def index():
    return """
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>Proiect SCC - Masini</title>
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(135deg, #020617, #111827);
                color: #f8fafc;
            }
            .container {
                max-width: 900px;
                margin: 60px auto;
                padding: 32px;
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 24px;
                box-shadow: 0 22px 70px rgba(0, 0, 0, 0.38);
            }
            .badge {
                display: inline-block;
                background: rgba(212, 175, 55, 0.15);
                border: 1px solid rgba(212, 175, 55, 0.45);
                color: #facc15;
                padding: 8px 14px;
                border-radius: 999px;
                font-weight: 700;
                margin-bottom: 18px;
            }
            h1 {
                color: #d4af37;
                font-size: 42px;
                margin-top: 0;
            }
            p {
                color: #dbeafe;
                font-size: 18px;
                line-height: 1.7;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 14px 22px;
                background: #d4af37;
                color: #111827;
                text-decoration: none;
                border-radius: 14px;
                font-weight: bold;
            }
            a:hover {
                background: #facc15;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <span class="badge">Flask + Git + Jenkins + Docker</span>
            <h1>Proiect SCC - 441D - Masini</h1>
            <p>
                Aplicatie Flask pentru proiectul de Servicii Cloud si Containerizare.
                Functionalitatea adaugata in acest branch este pentru marca Bentley.
            </p>
            <a href="/masini/bentley">Deschide pagina Bentley</a>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
