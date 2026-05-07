import unittest

from masini import app
from app.lib.biblioteca_masini import (
    descriere_rollsroyce,
    istoric_rollsroyce,
    motorizare_rollsroyce,
)


class TestBibliotecaRollsRoyce(unittest.TestCase):

    def test_descriere_rollsroyce(self):
        rezultat = descriere_rollsroyce()

        self.assertIsInstance(rezultat, str)
        self.assertIn("Rolls-Royce", rezultat)

    def test_istoric_rollsroyce(self):
        rezultat = istoric_rollsroyce()

        self.assertIsInstance(rezultat, str)
        self.assertIn("1904", rezultat)

    def test_motorizare_rollsroyce(self):
        rezultat = motorizare_rollsroyce()

        self.assertIsInstance(rezultat, str)
        self.assertIn("Phantom", rezultat)


class TestRuteRollsRoyce(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_ruta_rollsroyce_principala(self):
        response = self.client.get("/masini/rollsroyce/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Rolls-Royce", response.data)
        self.assertIn(b"Neacsu Roxana", response.data)

    def test_ruta_rollsroyce_istoric(self):
        response = self.client.get("/masini/rollsroyce/istoric")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Istoric Rolls-Royce", response.data)

    def test_ruta_rollsroyce_motorizare(self):
        response = self.client.get("/masini/rollsroyce/motorizare")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Motorizare Rolls-Royce", response.data)


if __name__ == "__main__":
    unittest.main()
