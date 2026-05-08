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
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; text-align: center; }"
    ret += "h1 { color: #222; }"
    ret += "p { font-size: 18px; color: #444; }"
    ret += "button { background-color: #e60000; color: white; border: none; padding: 12px 25px; font-size: 16px; border-radius: 8px; cursor: pointer; margin: 8px; }"
    ret += "button:hover { background-color: #b80000; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += "<h1>Marci auto</h1>"
    ret += "<p>Alege marca auto:</p>"

    ret += f'<a href="{url_for("maserati")}">'
    ret += "<button>Maserati</button>"
    ret += "</a>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/maserati", methods=["GET"])
def maserati():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Maserati</title>"

    ret += "<style>"
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; text-align: center; }"
    ret += "h1 { color: #222; }"
    ret += "h2 { color: #333; margin-top: 30px; }"
    ret += "p { font-size: 18px; color: #444; max-width: 700px; margin: 20px auto; line-height: 1.6; }"
    ret += "button { background-color: #e60000; color: white; border: none; padding: 12px 25px; font-size: 16px; border-radius: 8px; cursor: pointer; margin: 8px; }"
    ret += "button:hover { background-color: #b80000; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Maserati</h1>"
    ret += "<p>Maserati este o marcă auto italiană de lux, cunoscută pentru design elegant, performanță sportivă și modele premium.</p>"

    ret += "<h2>Modele Maserati:</h2>"

    ret += f'<a href="{url_for("maserati_mc20")}">'
    ret += "<button>Maserati MC20</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("maserati_ghibli")}">'
    ret += "<button>Maserati Ghibli</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("maserati_quattroporte")}">'
    ret += "<button>Maserati Quattroporte</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("maserati_levante")}">'
    ret += "<button>Maserati Levante</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("maserati_grecale")}">'
    ret += "<button>Maserati Grecale</button>"
    ret += "</a>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/maserati/mc20", methods=["GET"])
def maserati_mc20():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Maserati MC20</title>"

    ret += "<style>"
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; color: #333; }"
    ret += "h1 { color: #222; text-align: center; }"
    ret += "h2 { color: #e60000; margin-top: 30px; }"
    ret += "p { font-size: 18px; line-height: 1.6; }"
    ret += "ul { background-color: white; padding: 20px 40px; border-radius: 10px; max-width: 600px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }"
    ret += "li { font-size: 16px; margin-bottom: 10px; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "a:hover { color: #b80000; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("maserati")}">Înapoi la Maserati</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Maserati MC20</h1>"
    ret += "<p>Maserati MC20 este un supercar italian, apreciat pentru performanță ridicată și design aerodinamic.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Maserati</li>"
    ret += "<li><b>Model:</b> MC20</li>"
    ret += "<li><b>Tip caroserie:</b> coupe sport</li>"
    ret += "<li><b>Țară de origine:</b> Italia</li>"
    ret += "<li><b>Tracțiune:</b> spate</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 3.0 V6 Twin-Turbo</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 630 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Maserati MC20 oferă accelerație puternică, manevrabilitate sportivă și un aspect agresiv specific supercarurilor.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/maserati/ghibli", methods=["GET"])
def maserati_ghibli():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Maserati Ghibli</title>"

    ret += "<style>"
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; color: #333; }"
    ret += "h1 { color: #222; text-align: center; }"
    ret += "h2 { color: #e60000; margin-top: 30px; }"
    ret += "p { font-size: 18px; line-height: 1.6; }"
    ret += "ul { background-color: white; padding: 20px 40px; border-radius: 10px; max-width: 600px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }"
    ret += "li { font-size: 16px; margin-bottom: 10px; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "a:hover { color: #b80000; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("maserati")}">Înapoi la Maserati</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Maserati Ghibli</h1>"
    ret += "<p>Maserati Ghibli este un sedan premium, cunoscut pentru confort, eleganță și performanță sportivă.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Maserati</li>"
    ret += "<li><b>Model:</b> Ghibli</li>"
    ret += "<li><b>Tip caroserie:</b> sedan</li>"
    ret += "<li><b>Țară de origine:</b> Italia</li>"
    ret += "<li><b>Tracțiune:</b> spate / integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 3.0 V6 Twin-Turbo</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 350 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Maserati Ghibli combină luxul interior cu un motor puternic și un stil elegant italian.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/maserati/quattroporte", methods=["GET"])
def maserati_quattroporte():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Maserati Quattroporte</title>"

    ret += "<style>"
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; color: #333; }"
    ret += "h1 { color: #222; text-align: center; }"
    ret += "h2 { color: #e60000; margin-top: 30px; }"
    ret += "p { font-size: 18px; line-height: 1.6; }"
    ret += "ul { background-color: white; padding: 20px 40px; border-radius: 10px; max-width: 600px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }"
    ret += "li { font-size: 16px; margin-bottom: 10px; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "a:hover { color: #b80000; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("maserati")}">Înapoi la Maserati</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Maserati Quattroporte</h1>"
    ret += "<p>Maserati Quattroporte este un sedan de lux de dimensiuni mari, potrivit pentru confort și performanță.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Maserati</li>"
    ret += "<li><b>Model:</b> Quattroporte</li>"
    ret += "<li><b>Tip caroserie:</b> sedan de lux</li>"
    ret += "<li><b>Țară de origine:</b> Italia</li>"
    ret += "<li><b>Tracțiune:</b> spate / integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 3.0 V6 Twin-Turbo</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 430 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Maserati Quattroporte oferă spațiu, rafinament și performanță într-un automobil premium italian.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/maserati/levante", methods=["GET"])
def maserati_levante():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Maserati Levante</title>"

    ret += "<style>"
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; color: #333; }"
    ret += "h1 { color: #222; text-align: center; }"
    ret += "h2 { color: #e60000; margin-top: 30px; }"
    ret += "p { font-size: 18px; line-height: 1.6; }"
    ret += "ul { background-color: white; padding: 20px 40px; border-radius: 10px; max-width: 600px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }"
    ret += "li { font-size: 16px; margin-bottom: 10px; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "a:hover { color: #b80000; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("maserati")}">Înapoi la Maserati</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Maserati Levante</h1>"
    ret += "<p>Maserati Levante este un SUV premium, creat pentru confort, spațiu și performanță.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Maserati</li>"
    ret += "<li><b>Model:</b> Levante</li>"
    ret += "<li><b>Tip caroserie:</b> SUV</li>"
    ret += "<li><b>Țară de origine:</b> Italia</li>"
    ret += "<li><b>Tracțiune:</b> integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 3.0 V6 Twin-Turbo</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 350 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Maserati Levante combină poziția înaltă la volan cu luxul interior și performanța specifică mărcii Maserati.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/maserati/grecale", methods=["GET"])
def maserati_grecale():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Maserati Grecale</title>"

    ret += "<style>"
    ret += "body { font-family: Arial, sans-serif; background-color: #f2f2f2; margin: 0; padding: 40px; color: #333; }"
    ret += "h1 { color: #222; text-align: center; }"
    ret += "h2 { color: #e60000; margin-top: 30px; }"
    ret += "p { font-size: 18px; line-height: 1.6; }"
    ret += "ul { background-color: white; padding: 20px 40px; border-radius: 10px; max-width: 600px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }"
    ret += "li { font-size: 16px; margin-bottom: 10px; }"
    ret += "a { text-decoration: none; color: #e60000; font-weight: bold; }"
    ret += "a:hover { color: #b80000; }"
    ret += "</style>"

    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("maserati")}">Înapoi la Maserati</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Maserati Grecale</h1>"
    ret += "<p>Maserati Grecale este un SUV premium compact, potrivit pentru oraș, familie și drumuri lungi.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Maserati</li>"
    ret += "<li><b>Model:</b> Grecale</li>"
    ret += "<li><b>Tip caroserie:</b> SUV compact</li>"
    ret += "<li><b>Țară de origine:</b> Italia</li>"
    ret += "<li><b>Tracțiune:</b> integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 2.0 Mild Hybrid</li>"
    ret += "<li><b>Combustibil:</b> benzină / mild hybrid</li>"
    ret += "<li><b>Putere:</b> aproximativ 300 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Maserati Grecale oferă confort, tehnologie modernă și performanță într-un SUV premium de dimensiuni mai compacte.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


if __name__ == "__main__":
    app.run(debug=True)