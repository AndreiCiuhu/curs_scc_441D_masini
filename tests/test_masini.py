from app.lib.biblioteca_masini import istoric_mazda, motorizari_mazda


def test_istoric_mazda():
    rezultat = istoric_mazda()
    assert "Mazda" in rezultat


def test_motorizari_mazda():
    rezultat = motorizari_mazda()
    assert len(rezultat) >= 3
    assert "Skyactiv" in " ".join(rezultat)
