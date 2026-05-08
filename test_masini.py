from masini import app, modele_volkswagen, motoare_volkswagen


def test_functie_modele_volkswagen():
    with app.test_request_context():
        rezultat = modele_volkswagen()

    assert "Modele Volkswagen" in rezultat
    assert "Golf" in rezultat
    assert "Passat" in rezultat
    assert "Polo" in rezultat
    assert "Tiguan" in rezultat
    assert "Touareg" in rezultat


def test_functie_motoare_volkswagen():
    with app.test_request_context():
        rezultat = motoare_volkswagen()

    assert "Motoare Volkswagen" in rezultat
    assert "1.0 TSI" in rezultat
    assert "1.5 TSI" in rezultat
    assert "2.0 TSI" in rezultat
    assert "1.6 TDI" in rezultat
    assert "2.0 TDI" in rezultat