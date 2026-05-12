date_volvo = {
    "XC60": {
        "tip": "SUV de dimensiuni medii",
        "descriere": "Un SUV versatil si sigur, extrem de popular pentru familii si calatorii lungi."
    },
    "V50": {
        "tip": "Break compact",
        "descriere": "Un model clasic si practic, recunoscut pentru fiabilitatea sa in traficul urban."
    },
    "V90": {
        "tip": "Break premium",
        "descriere": "O masina eleganta, foarte spatioasa, axata pe lux si confort la superlativ."
    }
}

def modele_volvo():
    """
    Returneaza o lista cu toate modelele Volvo disponibile in baza noastra de date.
    """
    return list(date_volvo.keys())

def detalii_volvo(nume_model):
    """
    Returneaza detalii despre un anumit model de Volvo.
    """
    model_formatat = nume_model.upper()
    
    if model_formatat in date_volvo:
        return date_volvo[model_formatat]
    else:
        return {"eroare": f"Modelul Volvo {nume_model} nu a fost gasit in sistem."}
