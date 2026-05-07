from flask import Flask, render_template

from app.routes.test import test_bp

app = Flask(__name__)
app.register_blueprint(test_bp)


@app.route('/')
def index():
    return render_template(
        'page.html',
        title='Acasa/Home',
        content='Va rog sa apasati pe unul dintre butoane pentru a selecta ce doriti sa aflati despre Mazda',
        items=None
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
