import unittest

from app.lib.biblioteca_masini import culoare_skoda, descriere_skoda


class TestBibliotecaMasiniSkoda(unittest.TestCase):

    def test_culoare_skoda(self):
        rezultat = culoare_skoda()
        self.assertIsInstance(rezultat, str)
        self.assertIn("Skoda", rezultat)
        self.assertIn("culori", rezultat)

    def test_descriere_skoda(self):
        rezultat = descriere_skoda()
        self.assertIsInstance(rezultat, str)
        self.assertIn("Skoda", rezultat)
        self.assertIn("Volkswagen", rezultat)


if __name__ == "__main__":
    unittest.main()
