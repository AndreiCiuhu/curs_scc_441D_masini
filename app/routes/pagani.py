from flask import Blueprint, render_template
from app.lib.biblioteca_masini import descriere_pagani, modele_pagani

pagani_bp=Blueprint('pagani', __name__)

@pagani_bp.route('/masini')
def pagina_temei():
	return "Pagina temei Masini"

@pagani_bp.route('/masini/pagani')
def pagina_pagani():
	return render_template('pagani/pagani.html')

@pagani_bp.route('/masini/pagani/modele')
def culoare():
	return render_template('pagani/modele.html', modele=modele_pagani())

@pagani_bp.route('/masini/pagani/descriere')
def descriere():
	return render_template('pagani/descriere.html', descriere=descriere_pagani())
