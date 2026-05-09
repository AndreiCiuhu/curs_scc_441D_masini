from masini import app, index, alfa_romeo, giulia_quadrifoglio


def test_functie_index():
    with app.test_request_context():
        rezultat = index()

    assert "Mărci auto" in rezultat
    assert "Alfa Romeo" in rezultat
    assert "/alfa_romeo" in rezultat


def test_functie_alfa_romeo():
    with app.test_request_context():
        rezultat = alfa_romeo()

    assert "Alfa Romeo" in rezultat
    assert "Marcă italiană" in rezultat
    assert "Alfa Romeo Giulia Quadrifoglio" in rezultat
    assert "/alfa_romeo/giulia_quadrifoglio" in rezultat


def test_functie_giulia_quadrifoglio():
    with app.test_request_context():
        rezultat = giulia_quadrifoglio()

    assert "Alfa Romeo Giulia Quadrifoglio" in rezultat
    assert "2.9 V6 Bi-Turbo" in rezultat
    assert "510 CP" in rezultat
    assert "sedan sport" in rezultat
    assert "Italia" in rezultat
    assert "Tracțiune" in rezultat