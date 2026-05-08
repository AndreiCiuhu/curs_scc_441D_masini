from flask import Flask, url_for

app= Flask(__name__)

css = """
<style>
body { font-family: Arial; background: #eef2f7; text-align: center; padding: 40px; }
h1 { color: #1f3c88; }
button { background: #1f3c88; color: white; border: 0; padding: 12px 24px; margin: 10px; border-radius: 8px; font-size: 16px; cursor: pointer; }
button:hover { background: #0b5ed7; }
a { text-decoration: none; color: #1f3c88; font-weight: bold; }
ul { background: white; max-width: 400px; margin: 30px auto; padding: 20px; border-radius: 12px; list-style: none; box-shadow: 0 4px 10px #aaa; }
ul b { display: block; margin: 10px; padding: 10px; background: #eef3ff; border-radius: 8px; }
</style>
"""

@app.route("/", methods=["GET"])
def index():
    ret = ""

    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Marci auto</title>"
    ret += css
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
    ret += css
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
    ret += css
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
    ret = ""
    ret += "<!DOCTYPE html>"
    ret += "<html>"
    ret += "<head>"
    ret += "<title>Motoare Volkswagen</title>"
    ret += css
    ret += "</head>"
    ret += "<body>"
    ret += f'<a href="{url_for("volkswagen")}">Înapoi la Volkswagen</a><br>'
    ret += f'<a href="{url_for("index")}">Acasă</a><br><br>'
    ret += "<h1>Motoare Volkswagen</h1>"

    ret += "<ul>"
    ret += "<b>1.0 TSI</b>"
    ret += "<b>1.5 TSI</b>"
    ret += "<b>2.0 TSI</b>"
    ret += "<b>1.6 TDI</b>"
    ret += "<b>2.0 TDI</b>"
    ret += "</ul>"
    ret += "</body>"
    ret += "</html>"
    return ret

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)