from app.lib.biblioteca_masini import descriere_fiat, modele_fiat


def test_descriere_fiat():
    rezultat = descriere_fiat()
    assert "Fiat" in rezultat
    assert "italian" in rezultat


def test_modele_fiat():
    rezultat = modele_fiat()
    assert "Fiat 500" in rezultat
    assert "Fiat Panda" in rezultat
    assert "Fiat Tipo" in rezultat
