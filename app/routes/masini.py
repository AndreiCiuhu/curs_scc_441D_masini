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

    ret += f'<a href="{url_for("toyota")}">'
    ret += "<button>Toyota</button>"
    ret += "</a>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/toyota", methods=["GET"])
def toyota():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Toyota</title>"

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

    ret += "<h1>Toyota</h1>"
    ret += "<p>Toyota este o marcă auto japoneză, cunoscută pentru fiabilitate, eficiență și modele populare la nivel mondial.</p>"

    ret += "<h2>Modele Toyota:</h2>"

    ret += f'<a href="{url_for("toyota_supra")}">'
    ret += "<button>Toyota GR Supra</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("toyota_corolla")}">'
    ret += "<button>Toyota Corolla</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("toyota_camry")}">'
    ret += "<button>Toyota Camry</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("toyota_rav4")}">'
    ret += "<button>Toyota RAV4</button>"
    ret += "</a>"

    ret += f'<a href="{url_for("toyota_hilux")}">'
    ret += "<button>Toyota Hilux</button>"
    ret += "</a>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/toyota/gr_supra", methods=["GET"])
def toyota_supra():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Toyota GR Supra</title>"

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

    ret += f'<a href="{url_for("toyota")}">Înapoi la Toyota</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Toyota GR Supra</h1>"
    ret += "<p>Toyota GR Supra este un model sportiv al mărcii Toyota, apreciat pentru performanță și design modern.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Toyota</li>"
    ret += "<li><b>Model:</b> GR Supra</li>"
    ret += "<li><b>Tip caroserie:</b> coupe sport</li>"
    ret += "<li><b>Țară de origine:</b> Japonia</li>"
    ret += "<li><b>Tracțiune:</b> spate</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 3.0 inline-6 Turbo</li>"
    ret += "<li><b>Combustibil:</b> benzină</li>"
    ret += "<li><b>Putere:</b> aproximativ 340 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Toyota GR Supra este apreciată pentru comportamentul sportiv, accelerația puternică și aspectul agresiv.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/toyota/corolla", methods=["GET"])
def toyota_corolla():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Toyota Corolla</title>"

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

    ret += f'<a href="{url_for("toyota")}">Înapoi la Toyota</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Toyota Corolla</h1>"
    ret += "<p>Toyota Corolla este unul dintre cele mai cunoscute modele Toyota, apreciat pentru consum redus și fiabilitate.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Toyota</li>"
    ret += "<li><b>Model:</b> Corolla</li>"
    ret += "<li><b>Tip caroserie:</b> sedan / hatchback</li>"
    ret += "<li><b>Țară de origine:</b> Japonia</li>"
    ret += "<li><b>Tracțiune:</b> față</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 1.8 Hybrid</li>"
    ret += "<li><b>Combustibil:</b> benzină / hybrid</li>"
    ret += "<li><b>Putere:</b> aproximativ 140 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Toyota Corolla este o mașină potrivită pentru oraș și drumuri lungi, oferind confort și eficiență.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/toyota/camry", methods=["GET"])
def toyota_camry():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Toyota Camry</title>"

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

    ret += f'<a href="{url_for("toyota")}">Înapoi la Toyota</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Toyota Camry</h1>"
    ret += "<p>Toyota Camry este un sedan confortabil, potrivit pentru familie și călătorii lungi.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Toyota</li>"
    ret += "<li><b>Model:</b> Camry</li>"
    ret += "<li><b>Tip caroserie:</b> sedan</li>"
    ret += "<li><b>Țară de origine:</b> Japonia</li>"
    ret += "<li><b>Tracțiune:</b> față</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 2.5 Hybrid</li>"
    ret += "<li><b>Combustibil:</b> benzină / hybrid</li>"
    ret += "<li><b>Putere:</b> aproximativ 218 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Toyota Camry oferă un interior spațios, consum eficient și un nivel ridicat de confort.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/toyota/rav4", methods=["GET"])
def toyota_rav4():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Toyota RAV4</title>"

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

    ret += f'<a href="{url_for("toyota")}">Înapoi la Toyota</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Toyota RAV4</h1>"
    ret += "<p>Toyota RAV4 este un SUV modern, potrivit pentru oraș, familie și drumuri mai dificile.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Toyota</li>"
    ret += "<li><b>Model:</b> RAV4</li>"
    ret += "<li><b>Tip caroserie:</b> SUV</li>"
    ret += "<li><b>Țară de origine:</b> Japonia</li>"
    ret += "<li><b>Tracțiune:</b> față / integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 2.5 Hybrid</li>"
    ret += "<li><b>Combustibil:</b> benzină / hybrid</li>"
    ret += "<li><b>Putere:</b> aproximativ 222 CP</li>"
    ret += "<li><b>Transmisie:</b> automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Toyota RAV4 este apreciată pentru spațiu, siguranță și poziția înaltă la volan.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


@app.route("/toyota/hilux", methods=["GET"])
def toyota_hilux():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Toyota Hilux</title>"

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

    ret += f'<a href="{url_for("toyota")}">Înapoi la Toyota</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Toyota Hilux</h1>"
    ret += "<p>Toyota Hilux este un pickup robust, cunoscut pentru rezistență și capacitate bună pe teren accidentat.</p>"

    ret += "<h2>Informații generale</h2>"
    ret += "<ul>"
    ret += "<li><b>Marcă:</b> Toyota</li>"
    ret += "<li><b>Model:</b> Hilux</li>"
    ret += "<li><b>Tip caroserie:</b> pickup</li>"
    ret += "<li><b>Țară de origine:</b> Japonia</li>"
    ret += "<li><b>Tracțiune:</b> spate / integrală</li>"
    ret += "</ul>"

    ret += "<h2>Motor</h2>"
    ret += "<ul>"
    ret += "<li><b>Motor:</b> 2.8 Diesel</li>"
    ret += "<li><b>Combustibil:</b> motorină</li>"
    ret += "<li><b>Putere:</b> aproximativ 204 CP</li>"
    ret += "<li><b>Transmisie:</b> manuală / automată</li>"
    ret += "</ul>"

    ret += "<h2>Descriere</h2>"
    ret += "<p>Toyota Hilux este potrivită pentru muncă, transport și drumuri dificile, fiind un model foarte rezistent.</p>"

    ret += "</body>"
    ret += "</html>"

    return ret


if __name__ == "__main__":
    app.run(debug=True)