def modele_bmw():
    return ["m3", "m5", "x5"]

def detalii_bmw(model: str):
    model = model.lower()
    
    # Baza de date simulata pentru a potrivi structura pe care o cere HTML-ul
    masini_db = {
        "m3": {
            "year": 2023, "model": "m3", "class": "compact",
            "cylinders": 6, "displacement": 3.0, "drive": "rwd",
            "fuel_type": "gasoline", "transmission": "manual"
        },
        "m5": {
            "year": 2023, "model": "m5", "class": "midsize",
            "cylinders": 8, "displacement": 4.4, "drive": "awd",
            "fuel_type": "gasoline", "transmission": "automatic"
        },
        "x5": {
            "year": 2023, "model": "x5", "class": "suv",
            "cylinders": 6, "displacement": 3.0, "drive": "awd",
            "fuel_type": "hybrid", "transmission": "automatic"
        }
    }
    
    return masini_db.get(model)
