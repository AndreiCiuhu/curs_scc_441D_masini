from flask import Blueprint, render_template
from app.lib.biblioteca_masini import culoare_peugeot, descriere_peugeot

peugeot_bp=Blueprint('peugeot', __name__)

@peugeot_bp.route('/masini')
def pagina_temei():
	return "Pagina temei Masini"

@peugeot_bp.route('/masini/peugeot')
def pagina_ford():
	return render_template('peugeot/peugeot.html')

@peugeot_bp.route('/masini/peugeot/culoare')
def culoare():
	return render_template('peugeot/culoare.html', culoare=culoare_peugeot())

@peugeot_bp.route('/masini/peugeot/descriere')
def descriere():
	return render_template('peugeot/descriere.html', descriere=descriere_peugeot())