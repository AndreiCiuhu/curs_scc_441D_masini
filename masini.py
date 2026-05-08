from flask import Flask

from routes.test import test_bp

print("Volkswagen")

app= Flask(__name__)
app.register_blueprint(test_bp)

@app.route('/')
def index():
    return 'Masini'