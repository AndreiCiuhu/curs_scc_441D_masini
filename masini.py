from flask import Flask

from app.routes.test import test_bp
from app.routes.bmw import modul_rutare_bmw  

app = Flask(__name__)
app.register_blueprint(test_bp)
app.register_blueprint(modul_rutare_bmw)     
@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Proiect SCC - 441D</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f4f6f9; color: #2c3e50; margin: 0; padding: 40px 20px; display: flex; justify-content: center; }
            .container { background: #ffffff; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); text-align: center; max-width: 600px; width: 100%; border-top: 5px solid #0066B1; }
            h1 { color: #2c3e50; margin-top: 0; margin-bottom: 10px; }
            p { font-size: 1.1rem; color: #7f8c8d; margin-bottom: 30px; }
            .marci-list { display: flex; flex-direction: column; gap: 15px; align-items: center; }
            .btn { display: inline-block; background-color: #0066B1; color: white; padding: 14px 30px; text-decoration: none; border-radius: 8px; font-weight: 600; width: 250px; font-size: 1.1rem; transition: all 0.3s ease; border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .btn:hover { background-color: #004c85; transform: translateY(-3px); box-shadow: 0 6px 15px rgba(0,102,177,0.2); }
            .btn-test { background-color: #95a5a6; }
            .btn-test:hover { background-color: #7f8c8d; box-shadow: 0 6px 15px rgba(149,165,166,0.2); }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Proiect SCC - 441D - Masini</h1>
            <p>Selectati o marca auto pentru a vizualiza datele si specificatiile tehnice:</p>
            <div class="marci-list">
                <a href="/masini/bmw" class="btn">BMW</a>
                <a href="/masini/test" class="btn btn-test">Ruta de Test</a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
