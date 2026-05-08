from flask import Flask

print("Volkswagen")

app= Flask(__name__)
app.register_blueprint(test_bp)

@app.route("/", methods=["GET"])
def index():
    ret = ""

    ret += "<h2>Aplicatie Flask - Marci auto</h2>"
    ret += f"[<a href={url_for('volkswagen')}>Volkswagen</a>]"

    return ret

@app.route("/volkswagen", methods=["GET"])
def volkswagen():
    ret = ""

    ret += f"<a href={url_for('index')}>acasa</a><br><br>"

    ret += "<h2>Volkswagen</h2>"
    return ret