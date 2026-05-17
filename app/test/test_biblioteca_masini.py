import unittest
from app.lib.biblioteca_masini import culoare_ferrari, descriere_ferrari

class TestCuloareFerrari(unittest.TestCase):

    def test_model_existent(self):
        rezultat = culoare_ferrari('roma')
        self.assertEqual(rezultat, 'Grigio Titanio')

    def test_model_inexistent(self):
        rezultat = culoare_ferrari('inexistent')
        self.assertEqual(rezultat, 'Culoare nedisponibila')

    def test_fara_model(self):
        rezultat = culoare_ferrari()
        self.assertEqual(rezultat, 'Model negasit')


class TestDescriereFerrari(unittest.TestCase):

    def test_model_existent(self):
        rezultat = descriere_ferrari('sf90')
        self.assertEqual(rezultat, 'Ferrari SF90 Stradale - primul Ferrari hibrid plug-in cu 1000 CP')

    def test_model_inexistent(self):
        rezultat = descriere_ferrari('inexistent')
        self.assertEqual(rezultat, 'Descriere nedisponibila')

    def test_fara_model(self):
        rezultat = descriere_ferrari()
        self.assertEqual(rezultat, 'Model negasit')


if __name__ == '__main__':
    unittest.main()
