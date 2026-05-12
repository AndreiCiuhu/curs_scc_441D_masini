import unittest

from app.lib.biblioteca_masini import (
    modele_volvo,
    detalii_volvo
)

class TestModeleVolvo(unittest.TestCase):

    def test_modele_volvo_returneaza_lista(self):
        rezultat = modele_volvo()
        self.assertIsInstance(rezultat, list)
        self.assertGreater(len(rezultat), 0)
        self.assertIn('XC60', rezultat)


class TestDetaliiVolvo(unittest.TestCase):

    def test_detalii_volvo_succes(self):
        rezultat = detalii_volvo(nume_model='xc60')
        self.assertIsInstance(rezultat, dict)
        self.assertIn('tip', rezultat)
        self.assertIn('descriere', rezultat)

    def test_detalii_volvo_eroare(self):
        rezultat = detalii_volvo(nume_model='Inexistent')
        self.assertIsInstance(rezultat, dict)
        self.assertIn('eroare', rezultat)


if __name__ == '__main__':
    unittest.main()