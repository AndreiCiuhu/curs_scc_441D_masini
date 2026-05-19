import unittest
from app.lib.biblioteca_masini import culoare_dacia, descriere_dacia

class TestDacia(unittest.TestCase):

    def test_culoare(self):
        rezultat = culoare_dacia()
        self.assertIn('Dacia', rezultat)

    def test_descriere(self):
        rezultat = descriere_dacia()
        self.assertIn('Dacia', rezultat)

if __name__ == '__main__':
    unittest.main()