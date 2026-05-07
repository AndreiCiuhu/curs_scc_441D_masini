import unittest

from unittest.mock import patch, MagicMock

from app.lib.biblioteca_masini import (
    modele_kia,
    detalii_kia
)

class TestModelekia(unittest.TestCase):

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_modele_kia_returneaza_lista(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: [{'make': 'kia', 'model': 'sportage', 'year': 2020}]
        )
        rezultat = modele_kia()
        self.assertIsInstance(rezultat, list)
        self.assertGreater(len(rezultat), 0)

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_modele_kia_api_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=500)
        rezultat = modele_kia()
        self.assertEqual(rezultat, [])


class TestDetaliiKia(unittest.TestCase):

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_detalii_kia_returneaza_dict(self, mock_get):
        mock_get.return_value = MagicMock(
            status_code=200,
            json=lambda: [{'make': 'kia', 'model': 'sportage', 'year': 2020}]
        )
        rezultat = detalii_kia(model='sportage')
        self.assertIsInstance(rezultat, dict)
        self.assertEqual(rezultat.get('model'), 'sportage')

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_detalii_kia_fara_model(self, mock_get):
        rezultat = detalii_kia(model='')
        self.assertEqual(rezultat, {})

    @patch('app.lib.biblioteca_masini.requests.get')
    def test_detalii_kia_api_error(self, mock_get):
        mock_get.return_value = MagicMock(status_code=404)
        rezultat = detalii_kia(model='sportage')
        self.assertEqual(rezultat, {})


if __name__ == '__main__':
    unittest.main()