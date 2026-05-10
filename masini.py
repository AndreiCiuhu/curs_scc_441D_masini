from flask import Flask

from app.routes.peugeot import peugeot_bp
from app.routes.test import test_bp

app= Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(peugeot_bp)
@app.route('/')
def index():
    return 'Masini'