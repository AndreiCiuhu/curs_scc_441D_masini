import unittest
from unittest.mock import patch, MagicMock
from app.lib.biblioteca_masini import (
    modele_bmw,
    detalii_bmw
)

class TestModeleBmw(unittest.TestCase):

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_modele_bmw_returneaza_lista(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: [{'make': 'bmw', 'model': 'm3', 'year': 2023}]
        )
        rezultat = modele_bmw()
        self.assertIsInstance(rezultat, list)
        self.assertGreater(len(rezultat), 0)

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_modele_bmw_api_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=500)
        rezultat = modele_bmw()
        self.assertEqual(rezultat, [])


class TestDetaliiBmw(unittest.TestCase):

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_detalii_bmw_returneaza_dict(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: [{'make': 'bmw', 'model': 'm3', 'year': 2023}]
        )
        rezultat = detalii_bmw(model='m3')
        self.assertIsInstance(rezultat, dict)
        self.assertEqual(rezultat.get('model'), 'm3')

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_detalii_bmw_fara_model(self, mock_get):
        rezultat = detalii_bmw(model='')
        self.assertEqual(rezultat, {})

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_detalii_bmw_api_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=404)
        rezultat = detalii_bmw(model='m3')
        self.assertEqual(rezultat, {})

if __name__ == '__main__':
    unittest.main()
