from flask import Flask

from routes.test import test_bp

print("Volkswagen")

app= Flask(__name__)
app.register_blueprint(test_bp)

@app.route("/", methods=["GET"])
def index():
    ret = ""

    ret += "<h2>Aplicatie Flask - Marci auto</h2>"
    ret += f"[<a href={url_for('volkswagen')}>Volkswagen</a>]"

    return ret