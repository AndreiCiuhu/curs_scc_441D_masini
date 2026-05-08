from flask import Flask, url_for



app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Marci auto</title>"

    ret += "<style>"
    ret += "body {"
    ret += "font-family: Arial, sans-serif;"
    ret += "background: linear-gradient(to right, #1e3c72, #2a5298);"
    ret += "margin: 0;"
    ret += "padding: 0;"
    ret += "color: white;"
    ret += "text-align: center;"
    ret += "}"

    ret += ".container {"
    ret += "margin-top: 100px;"
    ret += "}"

    ret += "button {"
    ret += "padding: 15px 30px;"
    ret += "font-size: 18px;"
    ret += "border: none;"
    ret += "border-radius: 10px;"
    ret += "background-color: #ffffff;"
    ret += "color: #1e3c72;"
    ret += "cursor: pointer;"
    ret += "transition: 0.3s;"
    ret += "}"

    ret += "button:hover {"
    ret += "background-color: #dcdcdc;"
    ret += "transform: scale(1.05);"
    ret += "}"

    ret += "a {"
    ret += "text-decoration: none;"
    ret += "}"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += '<div class="container">'

    ret += "<h1>Marci auto</h1>"
    ret += "<p>Alege marca auto:</p>"

    ret += f'<a href="{url_for("dacia")}">'
    ret += "<button>Dacia</button>"
    ret += "</a>"

    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/dacia", methods=["GET"])
def dacia():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Dacia</title>"

    ret += "<style>"
    ret += "body {"
    ret += "font-family: Arial, sans-serif;"
    ret += "background: #f4f4f4;"
    ret += "margin: 0;"
    ret += "padding: 0;"
    ret += "}"

    ret += ".container {"
    ret += "width: 80%;"
    ret += "margin: 50px auto;"
    ret += "background: white;"
    ret += "padding: 30px;"
    ret += "border-radius: 15px;"
    ret += "box-shadow: 0 0 15px rgba(0,0,0,0.2);"
    ret += "}"

    ret += "h1 {"
    ret += "color: #003366;"
    ret += "}"

    ret += "button {"
    ret += "padding: 12px 25px;"
    ret += "font-size: 16px;"
    ret += "border: none;"
    ret += "border-radius: 8px;"
    ret += "background-color: #003366;"
    ret += "color: white;"
    ret += "cursor: pointer;"
    ret += "transition: 0.3s;"
    ret += "}"

    ret += "button:hover {"
    ret += "background-color: #0055aa;"
    ret += "}"

    ret += "a {"
    ret += "text-decoration: none;"
    ret += "color: #003366;"
    ret += "font-weight: bold;"
    ret += "}"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += '<div class="container">'

    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Dacia</h1>"
    ret += "<p>Dacia este o marcă auto românească, cunoscută pentru fiabilitate, preț accesibil și modele practice.</p>"

    ret += "<h2>Model ales:</h2>"

    ret += f'<a href="{url_for("dacia_duster")}">'
    ret += "<button>Dacia Duster</button>"
    ret += "</a>"

    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/dacia/duster", methods=["GET"])
def dacia_duster():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Dacia Duster</title>"

    ret += "<style>"
    ret += "body {"
    ret += "font-family: Arial, sans-serif;"
    ret += "background: linear-gradient(to right, #ece9e6, #ffffff);"
    ret += "margin: 0;"
    ret += "padding: 0;"
    ret += "}"

    ret += ".container {"
    ret += "width: 85%;"
    ret += "margin: 40px auto;"
    ret += "background: white;"
    ret += "padding: 30px;"
    ret += "border-radius: 15px;"
    ret += "box-shadow: 0 0 20px rgba(0,0,0,0.2);"
    ret += "}"

    ret += "h1, h2 {"
    ret += "color: #003366;"
    ret += "}"

    ret += "ul {"
    ret += "list-style-type: none;"
    ret += "padding: 0;"
    ret += "}"

    ret += "li {"
    ret += "padding: 10px;"
    ret += "margin-bottom: 10px;"
    ret += "background: #f4f4f4;"
    ret += "border-radius: 8px;"
    ret += "}"

    ret += "a {"
    ret += "text-decoration: none;"
    ret += "color: #003366;"
    ret += "font-weight: bold;"
    ret += "}"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += '<div class="container">'

    ret += f'<a href="{url_for("dacia")}">Înapoi la Dacia</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Dacia Duster</h1>"

    ret += "<p>Dacia Duster este un SUV popular apreciat pentru robustețe și accesibilitate.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Dacia</li>"
    ret += "<li><b>Model:</b> Duster</li>"
    ret += "<li><b>Tip caroserie:</b> SUV</li>"
    ret += "<li><b>Țară de origine:</b> România</li>"
    ret += "<li><b>Tracțiune:</b> față / integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 1.3 TCe</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 150 CP</li>"
    ret += "<li><b>Transmisie:</b> manuală / automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Dacia Duster este apreciată pentru consum redus, spațiu generos și capacitatea de a merge atât în oraș, cât și pe teren accidentat.</p>"

    ret += "</div>"

    ret += "</body>"
    ret += "</html>"

    return ret


if __name__ == "__main__":
    app.run(debug=True)