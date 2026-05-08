from flask import Flask, url_for

app= Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Marci auto</title>"
    ret += "</head>"
    ret += "<body>"

    ret += "<h1>Marci auto</h1>"
    ret += "<p>Alege marca auto:</p>"

    ret += f'<a href="{url_for("volkswagen")}">'
    ret += "<button>Volkswagen</button>"
    ret += "</a>"

    ret += "</body>"
    ret += "</html>"
    return ret

@app.route("/volkswagen", methods=["GET"])
def volkswagen():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Volkswagen</title>"
    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Volkswagen</h1>"

    ret += "<h2>Alege o secțiune:</h2>"

    ret += f'<a href="{url_for("modele_volkswagen")}">'
    ret += "<button>Modele Volkswagen</button>"
    ret += "</a> "

    ret += f'<a href="{url_for("motoare_volkswagen")}">'
    ret += "<button>Motoare Volkswagen</button>"
    ret += "</a>"

    ret += "</body>"
    ret += "</html>"
    return ret

@app.route("/volkswagen/modele", methods=["GET"])
def modele_volkswagen():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Modele Volkswagen</title>"
    ret += "</head>"
    ret += "<body>"

    ret += f'<a href="{url_for("volkswagen")}">Înapoi la Volkswagen</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'

    ret += "<h1>Modele Volkswagen</h1>"

    ret += "<ul>"
    ret += "<b>Golf</b> "
    ret += "<b>Passat</b>"
    ret += "<b>Polo</b>"
    ret += "<b>Tiguan</b>"
    ret += "<b>Touareg</b>"
    ret += "</ul>"

    ret += "</body>"
    ret += "</html>"
    return ret

@app.route("/volkswagen/motoare", methods=["GET"])
def motoare_volkswagen():
    return ret

if __name__ == "__main__":
    app.run(debug=True)