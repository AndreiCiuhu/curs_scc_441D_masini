from flask import Blueprint, render_template
from app.lib.biblioteca_masini import descriere_pagani, modele_pagani

pagani_bp=Blueprint('pagani', __name__)


@pagani_bp.route('/pagani')
def pagina_pagani():
	return 'Pagani'

@pagani_bp.route('/pagani/modele')
def culoare():
	return modele_pagani()

@pagani_bp.route('/pagani/descriere')
def descriere():
	return descriere_pagani()
