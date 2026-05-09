from flask import Flask, url_for


app = Flask(__name__)


def css():
    return """
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #111111, #3b0000);
            color: #f5f5f5;
        }

        .page {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px 20px;
        }

        .card {
            width: 100%;
            max-width: 850px;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 22px;
            padding: 35px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(8px);
        }

        h1 {
            margin-top: 0;
            font-size: 42px;
            color: #ffffff;
        }

        h2 {
            margin-top: 28px;
            color: #ff4b4b;
        }

        p {
            font-size: 18px;
            line-height: 1.6;
            color: #e8e8e8;
        }

        .subtitle {
            color: #cccccc;
            margin-bottom: 30px;
        }

        .btn {
            display: inline-block;
            text-decoration: none;
            background: #c00000;
            color: white;
            padding: 14px 24px;
            border-radius: 12px;
            font-weight: bold;
            border: none;
            cursor: pointer;
            margin: 8px 8px 8px 0;
            transition: 0.2s;
        }

        .btn:hover {
            background: #ff1e1e;
            transform: translateY(-2px);
        }

        .btn-secondary {
            background: transparent;
            border: 1px solid #ff4b4b;
            color: #ffffff;
        }

        .btn-secondary:hover {
            background: #ff4b4b;
        }

        ul {
            padding-left: 0;
            list-style: none;
        }

        li {
            background: rgba(255, 255, 255, 0.09);
            margin-bottom: 10px;
            padding: 14px 16px;
            border-radius: 12px;
            border-left: 4px solid #ff3333;
            font-size: 17px;
        }

        b {
            color: #ffffff;
        }

        .badge {
            display: inline-block;
            background: rgba(255, 0, 0, 0.2);
            color: #ffb3b3;
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 14px;
            margin-bottom: 15px;
        }

        .nav {
            margin-bottom: 25px;
        }
    </style>
    """


@app.route("/", methods=["GET"])
def index():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += '<meta charset="UTF-8">'
    ret += "<title>Marci auto</title>"
    ret += css()
    ret += "</head>"
    ret += "<body>"

    ret += '<div class="page">'
    ret += '<div class="card">'

    ret += '<span class="badge">Proiect Flask</span>'
    ret += "<h1>Mărci auto</h1>"
    ret += '<p class="subtitle">Alege marca auto pentru a vedea informații despre modelul selectat.</p>'

    ret += f'<a class="btn" href="{url_for("alfa_romeo")}">Alfa Romeo</a>'

    ret += "</div>"
    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/alfa_romeo", methods=["GET"])
def alfa_romeo():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += '<meta charset="UTF-8">'
    ret += "<title>Alfa Romeo</title>"
    ret += css()
    ret += "</head>"
    ret += "<body>"

    ret += '<div class="page">'
    ret += '<div class="card">'

    ret += '<div class="nav">'
    ret += f'<a class="btn btn-secondary" href="{url_for("index")}">Acasă</a>'
    ret += "</div>"

    ret += '<span class="badge">Marcă italiană</span>'
    ret += "<h1>Alfa Romeo</h1>"
    ret += "<p>Alfa Romeo este o marcă auto italiană, cunoscută pentru design sportiv, performanță și istorie în motorsport.</p>"

    ret += "<h2>Model ales</h2>"
    ret += f'<a class="btn" href="{url_for("giulia_quadrifoglio")}">Alfa Romeo Giulia Quadrifoglio</a>'

    ret += "</div>"
    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/alfa_romeo/giulia_quadrifoglio", methods=["GET"])
def giulia_quadrifoglio():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += '<meta charset="UTF-8">'
    ret += "<title>Alfa Romeo Giulia Quadrifoglio</title>"
    ret += css()
    ret += "</head>"
    ret += "<body>"

    ret += '<div class="page">'
    ret += '<div class="card">'

    ret += '<div class="nav">'
    ret += f'<a class="btn btn-secondary" href="{url_for("alfa_romeo")}">Înapoi la Alfa Romeo</a>'
    ret += f'<a class="btn btn-secondary" href="{url_for("index")}">Acasă</a>'
    ret += "</div>"

    ret += '<span class="badge">Sedan sport</span>'
    ret += "<h1>Alfa Romeo Giulia Quadrifoglio</h1>"
    ret += "<p>Alfa Romeo Giulia Quadrifoglio este versiunea sportivă de top a modelului Giulia.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Alfa Romeo</li>"
    ret += "<li><b>Model:</b> Giulia Quadrifoglio</li>"
    ret += "<li><b>Tip caroserie:</b> sedan sport</li>"
    ret += "<li><b>Țară de origine:</b> Italia</li>"
    ret += "<li><b>Tracțiune:</b> spate</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 2.9 V6 Bi-Turbo</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 510 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Giulia Quadrifoglio este apreciată pentru combinația dintre performanță, design italian și comportament sportiv pe șosea.</p>"

    ret += "</div>"
    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    return ret


if __name__ == "__main__":
    app.run(debug=True)