import unittest

from app.lib.biblioteca_masini import gaseste_informatii_modele, gaseste_informatii_motor


class TestBibliotecaMasini(unittest.TestCase):
    def test_gaseste_informatii_modele(self):
        modele = gaseste_informatii_modele()
        self.assertIsInstance(modele, list)
        self.assertIn('A3', modele)
        self.assertIn('Q5', modele)_____________ 

    def test_gaseste_informatii_motor(self):
        motor = gaseste_informatii_motor()
        self.assertIsInstance(motor, list)
        self.assertIn('35TFSI', motor)
        self.assertIn('40TDI', motor)


if __name__ == '__main__':
    unittest.main()
