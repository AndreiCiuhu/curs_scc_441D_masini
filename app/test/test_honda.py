import unittest
from masini import app


class TestHondaRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_honda_home(self):
        response = self.client.get("/masini/honda/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Honda", response.data)

    def test_honda_istoric(self):
        response = self.client.get("/masini/honda/istoric")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Istoric Honda", response.data)

    def test_honda_modele(self):
        response = self.client.get("/masini/honda/modele")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Modele Honda", response.data)


if __name__ == "__main__":
    unittest.main()
