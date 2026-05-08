from flask import Flask

from app.routes.test import test_bp
from app.routes.rollsroyce import rollsroyce_bp

app = Flask(__name__)

app.register_blueprint(test_bp)
app.register_blueprint(rollsroyce_bp)


@app.route('/')
def index():
    return """
<html>

<body style="font-family:Arial, sans-serif; max-width:800px; margin:40px auto; padding:0 20px;">

<h1>Proiect SCC - 441D - Masini</h1>

<p>Alegeti o marca:</p>

<ul>
<li><a href="/masini/rollsroyce">Rolls-Royce - Neacsu Roxana</a></li>
<li><a href="/masini/test">Ruta de Test</a></li>
</ul>

</body>

</html>
"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
