import unittest
from app.lib.biblioteca_masini import culoare_toyota, descriere_toyota


class TestToyota(unittest.TestCase):

    def test_culoare(self):
        rezultat = culoare_toyota()
        self.assertIn('Toyota', rezultat)

    def test_descriere(self):
        rezultat = descriere_toyota()
        self.assertIn('Toyota', rezultat)


if __name__ == '__main__':
    unittest.main()