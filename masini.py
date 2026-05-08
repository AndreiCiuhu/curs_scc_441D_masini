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

    ret += f"<a href={url_for('index')}>acasa</a><br><br>"

    ret += "<h2>Volkswagen</h2>"
    return ret

if __name__ == "__main__":
    app.run(debug=True)