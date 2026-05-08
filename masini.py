from app.routes.ford import ford_bp

from flask import Flask

from app.routes.test import test_bp

app= Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(ford_bp)
@app.route('/')
def index():
    return 'Masini'
