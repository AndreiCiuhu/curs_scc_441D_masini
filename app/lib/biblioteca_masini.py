def culoare_ferrari(model: str = '') -> str:
    culori = {
        'roma':      'Grigio Titanio',
        'portofino': 'Rosso Corsa',
        '488':       'Giallo Modena',
        'f8':        'Nero Daytona',
        'sf90':      'Bianco Avus',
    }
    model = model.lower()
    if not model:
        return 'Model negasit'
    return culori.get(model, 'Culoare nedisponibila')


def descriere_ferrari(model: str = '') -> str:
    descrieri = {
        'roma':      'Ferrari Roma - gran turismo elegant cu motor V8 de 620 CP',
        'portofino': 'Ferrari Portofino - cabrio sport cu motor V8 de 600 CP',
        '488':       'Ferrari 488 - supercar cu motor V8 turbo de 660 CP',
        'f8':        'Ferrari F8 Tributo - cel mai evoluat V8 din istoria Ferrari',
        'sf90':      'Ferrari SF90 Stradale - primul Ferrari hibrid plug-in cu 1000 CP',
    }
    model = model.lower()
    if not model:
        return 'Model negasit'
    return descrieri.get(model, 'Descriere nedisponibila')
