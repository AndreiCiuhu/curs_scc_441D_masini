import unittest

from app.lib.biblioteca_masini import (
    descriere_renault,
    detalii_model_renault,
    modele_renault,
)


class TestRenault(unittest.TestCase):

    def test_descriere(self):
        rezultat = descriere_renault()
        self.assertIn("Renault", rezultat)

    def test_modele_contine_sase_modele(self):
        modele = modele_renault()

        self.assertIn("clio", modele)
        self.assertIn("megane", modele)
        self.assertIn("captur", modele)
        self.assertIn("austral", modele)
        self.assertIn("arkana", modele)
        self.assertIn("talisman", modele)

    def test_detalii_model_megane(self):
        megane = detalii_model_renault("megane")

        self.assertIsNotNone(megane)
        self.assertEqual(megane["nume"], "Renault Megane")
        self.assertIn("1.5 Blue dCi (115 CP) EDC", megane["motorizari"])
        self.assertIn("climatizare automata", megane["dotari"])

    def test_detalii_model_talisman(self):
        talisman = detalii_model_renault("talisman")

        self.assertIsNotNone(talisman)
        self.assertEqual(talisman["nume"], "Renault Talisman")
        self.assertIn("2.0 Blue dCi (200 CP) EDC", talisman["motorizari"])

    def test_model_inexistent(self):
        rezultat = detalii_model_renault("logan")
        self.assertIsNone(rezultat)


if __name__ == "__main__":
    unittest.main()
