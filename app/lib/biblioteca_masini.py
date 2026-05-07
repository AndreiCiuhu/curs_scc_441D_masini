# Baza de date simulata cu toate detaliile necesare
masini_db = {
    "m3": {
        "make": "BMW", "model": "M3", "year": 2023, "class": "compact",
        "cylinders": 6, "displacement": 3.0, "drive": "rwd",
        "fuel_type": "Benzina", "transmission": "Manual", "horsepower": 473
    },
    "m5": {
        "make": "BMW", "model": "M5", "year": 2023, "class": "midsize",
        "cylinders": 8, "displacement": 4.4, "drive": "awd",
        "fuel_type": "Benzina", "transmission": "Automat", "horsepower": 600
    },
    "x5": {
        "make": "BMW", "model": "X5", "year": 2023, "class": "suv",
        "cylinders": 6, "displacement": 3.0, "drive": "awd",
        "fuel_type": "Hibrid", "transmission": "Automat", "horsepower": 335
    }
}

def modele_bmw():
    # Returneaza lista cu toate dictionarele de masini
    return list(masini_db.values())

def detalii_bmw(model: str):
    # Returneaza doar dictionarul masinii cerute
    return masini_db.get(model.lower())
