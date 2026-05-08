import unittest
from app.lib.biblioteca_masini import culoare_mclaren, descriere_mclaren


class TestMcLaren(unittest.TestCase):

    def test_culoare(self):
        rezultat = culoare_mclaren()
        self.assertIn("McLaren", rezultat)

    def test_descriere(self):
        rezultat = descriere_mclaren()
        self.assertIn("McLaren", rezultat)


if __name__ == "__main__":
    unittest.main()
