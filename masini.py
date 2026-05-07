from flask import Flask

from routes.test import test_bp
from routes.kia import kia_bp

app= Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(kia_bp)

@app.route('/')
def index():
    return 'Masini'