import unittest
from masini import app
from app.lib.biblioteca_masini import culoare_alpine, descriere_alpine, modele_alpine

class TestBibliotecaAlpine(unittest.TestCase):
    def test_culoare(self):
        rezultat = culoare_alpine()
        self.assertIsInstance(rezultat, str)
        self.assertIn('Alpine', rezultat)

    def test_descriere(self):
        rezultat = descriere_alpine()
        self.assertIsInstance(rezultat, str)
        self.assertIn('Alpine', rezultat)

    def test_modele(self):
        rezultat = modele_alpine()
        self.assertIsInstance(rezultat, list)
        self.assertGreater(len(rezultat), 0)
        for model in rezultat:
            self.assertIn('nume', model)
            self.assertIn('descriere', model)
            self.assertIn('caracteristici', model)

class TestRuteAlpine(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_ruta_principala_alpine(self):
        response = self.client.get("/masini/alpine")
        self.assertEqual(response.status_code, 200)

    def test_ruta_culoare(self):
        response = self.client.get("/masini/alpine/culoare")
        self.assertEqual(response.status_code, 200)

    def test_ruta_descriere(self):
        response = self.client.get("/masini/alpine/descriere")
        self.assertEqual(response.status_code, 200)

    def test_ruta_modele(self):
        response = self.client.get("/masini/alpine/modele")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()