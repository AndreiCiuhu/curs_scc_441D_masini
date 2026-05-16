"""Teste unittest pentru functiile si rutele Lamborghini."""

import unittest

from app.lib.biblioteca_masini import culoare_lamborghini, descriere_lamborghini
from masini import app


class TestBibliotecaLamborghini(unittest.TestCase):
    """Teste pentru functiile din biblioteca_masini."""

    def test_culoare(self):
        """Verifica functia culoare_lamborghini."""
        rezultat = culoare_lamborghini()
        self.assertIsInstance(rezultat, str)
        self.assertIn('Lamborghini', rezultat)

    def test_descriere(self):
        """Verifica functia descriere_lamborghini."""
        rezultat = descriere_lamborghini()
        self.assertIsInstance(rezultat, str)
        self.assertIn('Lamborghini', rezultat)


class TestRuteLamborghini(unittest.TestCase):
    """Teste pentru rutele Flask Lamborghini."""

    def setUp(self):
        """Creeaza clientul de test Flask."""
        self.client = app.test_client()

    def test_ruta_tema_masini(self):
        """Verifica ruta pentru tema masini."""
        response = self.client.get('/masini')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Pagina temei: Masini', response.data)

    def test_ruta_principala_lamborghini(self):
        """Verifica ruta principala Lamborghini."""
        response = self.client.get('/masini/lamborghini')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lamborghini', response.data)

    def test_ruta_culoare(self):
        """Verifica ruta culoare Lamborghini."""
        response = self.client.get('/masini/lamborghini/culoare')
        self.assertEqual(response.status_code, 200)

    def test_ruta_descriere(self):
        """Verifica ruta descriere Lamborghini."""
        response = self.client.get('/masini/lamborghini/descriere')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
