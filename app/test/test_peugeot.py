import unittest

def culoare_peugeot():
	return "albastru"

def descriere_peugeot():
	return "Masina puternica"

class TestFord(unittest.TestCase):

	def test_culoare(self):
		self.assertEqual(culoare_peugeot(), "albastru")

	def test_descriere(self):
		self.assertEqual(descriere_peugeot(), "Masina puternica")

if __name__ == '__main__':
	unittest.main()