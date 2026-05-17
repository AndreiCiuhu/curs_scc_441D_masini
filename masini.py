from flask import Flask

from app.routes.pagani import pagani_bp
from app.routes.test import test_bp

app= Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(pagani_bp)

@app.route('/')
def index():
    return 'Masini'
