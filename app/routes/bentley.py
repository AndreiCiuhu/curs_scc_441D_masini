from flask import Blueprint
from app.lib.biblioteca_masini import culoare_bentley, descriere_bentley

bentley_bp = Blueprint("bentley", __name__)


def page(title: str, body: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>{title}</title>
        <style>
            body {{
                margin: 0;
                min-height: 100vh;
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(135deg, #020617, #111827);
                color: #f8fafc;
            }}
            .container {{
                max-width: 1000px;
                margin: 50px auto;
                padding: 24px;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 24px;
                padding: 34px;
                box-shadow: 0 22px 70px rgba(0, 0, 0, 0.38);
            }}
            .badge {{
                display: inline-block;
                background: rgba(212, 175, 55, 0.15);
                border: 1px solid rgba(212, 175, 55, 0.45);
                color: #facc15;
                padding: 8px 14px;
                border-radius: 999px;
                font-weight: 700;
                margin-bottom: 18px;
            }}
            h1 {{
                color: #d4af37;
                font-size: 44px;
                margin-top: 0;
                margin-bottom: 16px;
            }}
            p {{
                color: #dbeafe;
                font-size: 18px;
                line-height: 1.7;
            }}
            .links {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 16px;
                margin-top: 28px;
            }}
            a.button {{
                display: block;
                background: #d4af37;
                color: #111827;
                padding: 16px 18px;
                border-radius: 14px;
                text-decoration: none;
                font-weight: bold;
                text-align: center;
                transition: 0.2s ease;
            }}
            a.button:hover {{
                background: #facc15;
                transform: translateY(-3px);
            }}
            .footer {{
                margin-top: 30px;
                color: #94a3b8;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="card">
                {body}
                <p class="footer">Proiect SCC 441D - Masini - Bentley</p>
            </div>
        </div>
    </body>
    </html>
    """


@bentley_bp.route("/masini", methods=["GET"])
def masini():
    body = """
        <span class="badge">Tema proiectului</span>
        <h1>Masini</h1>
        <p>
            Aceasta pagina reprezinta tema generala a proiectului. Fiecare student
            adauga o marca auto si informatii specifice acesteia.
        </p>
        <div class="links">
            <a class="button" href="/masini/bentley">Pagina Bentley</a>
            <a class="button" href="/">Pagina principala</a>
        </div>
    """
    return page("Masini", body)


@bentley_bp.route("/masini/bentley", methods=["GET"])
def bentley():
    body = """
        <span class="badge">Element ales</span>
        <h1>Bentley</h1>
        <p>
            Bentley este marca aleasa pentru implementarea individuala.
            Aplicatia include doua informatii specifice: culoare si descriere.
        </p>
        <div class="links">
            <a class="button" href="/masini/bentley/culoare">Culoare Bentley</a>
            <a class="button" href="/masini/bentley/descriere">Descriere Bentley</a>
        </div>
    """
    return page("Bentley", body)


@bentley_bp.route("/masini/bentley/culoare", methods=["GET"])
def bentley_culoare():
    body = f"""
        <span class="badge">Informatie specifica</span>
        <h1>Culoare Bentley</h1>
        <p>{culoare_bentley()}</p>
        <div class="links">
            <a class="button" href="/masini/bentley">Inapoi la Bentley</a>
            <a class="button" href="/">Pagina principala</a>
        </div>
    """
    return page("Culoare Bentley", body)


@bentley_bp.route("/masini/bentley/descriere", methods=["GET"])
def bentley_descriere():
    body = f"""
        <span class="badge">Informatie specifica</span>
        <h1>Descriere Bentley</h1>
        <p>{descriere_bentley()}</p>
        <div class="links">
            <a class="button" href="/masini/bentley">Inapoi la Bentley</a>
            <a class="button" href="/">Pagina principala</a>
        </div>
    """
    return page("Descriere Bentley", body)
