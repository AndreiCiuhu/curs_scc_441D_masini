from flask import Blueprint
from app.lib.biblioteca_masini import culoare_ford, descriere_ford

ford_bp=Blueprint('ford', __name__)

@ford_bp.route('/masini')
def pagina_temei():
	return "Pagina temei Masini"

@ford_bp.route('/masini/ford')
def pagina_ford():
	return "Pagina elementului Ford"

@ford_bp.route('/masini/ford/culoare')
def culoare():
	return culoare_ford()

@ford_bp.route('/masini/ford/descriere')
def descriere():
	return descriere_ford()
