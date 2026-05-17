from flask import Blueprint, render_template
from app.lib.biblioteca_masini import descriere_pagani, modele_pagani

pagani_bp=Blueprint('pagani', __name__)


@pagani_bp.route('/pagani')
def pagina_pagani():
	return render_template('pagani/pagani.html')

@pagani_bp.route('/pagani/modele')
def culoare():
	return render_template(modele_pagani())

@pagani_bp.route('/pagani/descriere')
def descriere():
	return render_template(descriere_pagani())
