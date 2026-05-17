import unittest

from app.lib.biblioteca_masini import (
    culoare_renault,
    descriere_renault,
    dotari_renault,
    modele_renault,
)


class TestRenault(unittest.TestCase):

    def test_culoare(self):
        rezultat = culoare_renault()
        self.assertIn("Renault", rezultat)

    def test_descriere(self):
        rezultat = descriere_renault()
        self.assertIn("Renault", rezultat)

    def test_dotari(self):
        rezultat = dotari_renault()
        self.assertIn("Renault", rezultat)

    def test_modele(self):
        rezultat = modele_renault()
        self.assertIn("Renault", rezultat)


if __name__ == "__main__":
    unittest.main()
