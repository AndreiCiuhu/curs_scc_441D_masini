import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_NINJAS_KEY')
API_URL = 'https://api.api-ninjas.com/v1/cars'

# Modelele specifice pentru BMW
MODELE_BMW = ['m3', 'm5', 'x5', 'm4', 'x7']

def modele_bmw(model: str = '') -> list:
    params = {'make': 'Bmw'}

    if model:
        params['model'] = model
        res = requests.get(
            API_URL, 
            headers={'X-Api-Key': API_KEY}, 
            params=params
        )
        if res.status_code != 200:
            return []
        return res.json()

    rezultate = []
    for m in MODELE_BMW:
        params['model'] = m
        res = requests.get(
            API_URL, 
            headers={'X-Api-Key': API_KEY}, 
            params=params
        )
        if res.status_code == 200 and res.json():
            rezultate.append(res.json()[0])

    return rezultate

def detalii_bmw(model: str) -> dict:
    # Refolosim functia de mai sus pentru a lua detalii despre un singur model
    res = modele_bmw(model=model)
    return res[0] if res else {}
