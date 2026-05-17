from flask import Flask
from app.routes.ferrari import ferrari_bp 
from routes.test import test_bp

app= Flask(__name__)
app.register_blueprint(ferrari_bp)


@app.route('/')
def index():
    return 'Masini'
