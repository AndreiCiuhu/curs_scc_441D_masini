from flask import Flask
from app.routes.hyundai import hyundai_bp

app = Flask(__name__)

app.register_blueprint(hyundai_bp)

@app.route('/')
def home():
    return 'Pagina principala - aplicatia masini'

if __name__ == '__main__':
    app.run(debug=True)