import unittest
from app.lib.biblioteca_masini import (
    culoare_hyundai,
    descriere_hyundai
)

class TestHyundai(unittest.TestCase):

    def test_culoare(self):
        rezultat = culoare_hyundai()
        self.assertIn('Hyundai', rezultat)

    def test_descriere(self):
        rezultat = descriere_hyundai()
        self.assertIn('Hyundai', rezultat)

if __name__ == '__main__':
    unittest.main()
