import unittest

from masini import app
from lib.biblioteca_masini import (
    modele_porsche,
    istorie_porsche_911,
)


class TestPorscheFiereaCosmin(unittest.TestCase):

    def test_modele_porsche(self):
        rezultat = modele_porsche()

        self.assertIsInstance(rezultat, list)
        self.assertGreater(len(rezultat), 0)
        self.assertEqual(rezultat[0]["marca"], "Porsche")

    def test_istorie_porsche_911(self):
        rezultat = istorie_porsche_911()

        self.assertIsInstance(rezultat, list)
        self.assertGreaterEqual(len(rezultat), 3)
        self.assertIn("generatie", rezultat[0])

    def test_ruta_porsche(self):
        client = app.test_client()
        response = client.get("/masini/porsche/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Porsche", response.data)

    def test_ruta_modele_porsche(self):
        client = app.test_client()
        response = client.get("/masini/porsche/modele")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Porsche 911", response.data)

    def test_ruta_istorie_porsche_911(self):
        client = app.test_client()
        response = client.get("/masini/porsche/istorie-911")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Istoria Porsche 911", response.data)


if __name__ == "__main__":
    unittest.main()
