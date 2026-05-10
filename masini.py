from flask import Flask
from app.routes.mercedes_routes import mercedes_bp

app = Flask(__name__)
app.register_blueprint(mercedes_bp)


@app.route("/")
def index():
    return "Aplicatie Flask pentru tema Masini."


@app.route("/masini")
def masini():
    return "Tema proiectului este: Masini."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
