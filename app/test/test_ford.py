import unittest
from app.lib.biblioteca_masini import culoare_ford, descriere_ford

class TestFord(unittest.TestCase):

	def test_culoare(self):
		rezultat = culoare_ford()
		self.assertIn('Ford', rezultat)

	def test_descriere(self):
		rezultat = descriere_ford()
		self.assertIn('Ford', rezultat)

if __name__ == '__main__':
	unittest.main()
