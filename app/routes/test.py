from flask import Blueprint, render_template

from app.lib.biblioteca_masini import istoric_mazda, motorizari_mazda

test_bp = Blueprint('test', __name__)


@test_bp.route('/masini')
def masini():
    return render_template(
        'page.html',
        title='Mazda',
        content='Va rog sa apasati pe unul dintre butoane pentru a selecta ce doriti sa aflati despre Mazda',
        items=None
    )


@test_bp.route('/masini/mazda')
def mazda():
    return render_template(
        'page.html',
        title='Acasa/Home',
        content='Va rog sa apasati pe unul dintre butoane pentru a selecta ce doriti sa aflati despre Mazda',
        items=None
    )


@test_bp.route('/masini/mazda/istoric')
def ruta_istoric_mazda():
    return render_template(
        'page.html',
        title='Istoric Mazda',
        content=istoric_mazda(),
        items=None
    )


@test_bp.route('/masini/mazda/motorizare')
def ruta_motorizare_mazda():
    return render_template(
        'page.html',
        title='Motorizare Mazda',
        content='Exemple de motoare importante fabricate de Mazda:',
        items=motorizari_mazda()
    )
