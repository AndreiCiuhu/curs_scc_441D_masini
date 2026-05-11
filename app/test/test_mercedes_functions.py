from app.lib.biblioteca_masini import descriere_mercedes, origine_mercedes, motorizare_mercedes


def test_descriere_mercedes_returneaza_text():
    rezultat = descriere_mercedes()

    assert isinstance(rezultat, str)
    assert "Mercedes-Benz" in rezultat
    assert "producator german" in rezultat
    assert "automobile premium" in rezultat
    assert "tehnologii avansate" in rezultat


def test_origine_mercedes_returneaza_text():
    rezultat = origine_mercedes()

    assert isinstance(rezultat, str)
    assert "Mercedes-Benz" in rezultat
    assert "Germania" in rezultat
    assert "Stuttgart" in rezultat
    assert "industriei auto germane" in rezultat


def test_motorizare_mercedes_returneaza_text():
    rezultat = motorizare_mercedes()

    assert isinstance(rezultat, str)
    assert "Mercedes-Benz" in rezultat
    assert "motorizari" in rezultat
    assert "benzina" in rezultat
    assert "diesel" in rezultat
    assert "hibride" in rezultat
    assert "electrice" in rezultat
