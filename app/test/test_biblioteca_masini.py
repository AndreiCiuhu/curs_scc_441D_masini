import unittest

from app.lib.biblioteca_masini import culoare_bentley, descriere_bentley


class TestBentley(unittest.TestCase):

    def test_culoare_bentley(self):
        rezultat = culoare_bentley()
        self.assertIn("Bentley", rezultat)

    def test_descriere_bentley(self):
        rezultat = descriere_bentley()
        self.assertIn("Bentley", rezultat)


if __name__ == "__main__":
    unittest.main()
