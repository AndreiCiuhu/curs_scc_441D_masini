import os
import requests

from dotenv import load_dotenv

load_dotenv()
API_KEY= os.getenv('API_NINJAS_KEY')
API_URL = 'https://api.api-ninjas.com/v1/cars'

MODELE_KIA = ['sportage', 'sorento', 'rio', 'stinger', 'telluride']


def modele_kia(model: str = '') -> list:
    params= {'make': 'Kia'}

    if model:
        params['model']= model

        res= requests.get(
            API_URL, 
            headers= {'X-Api-Key': API_KEY}, 
            params= params
        )
        if res.status_code != 200:
            return []
        
        return res.json()

    rezultate= []
    for m in MODELE_KIA:
        params['model']= m

        res= requests.get(
            API_URL, 
            headers= {'X-Api-Key': API_KEY}, 
            params= params
        )
        if res.status_code == 200 and res.json():
            rezultate.append(res.json()[0])

    return rezultate


def detalii_kia(model: str = '') -> dict:
    if not model:
        return {}

    params= {'make': 'Kia', 'model': model}

    res= requests.get(
        API_URL,
        headers={'X-Api-Key': API_KEY},
        params=params
    )

    if res.status_code != 200 or not res.json():
        return {}

    return res.json()[0]