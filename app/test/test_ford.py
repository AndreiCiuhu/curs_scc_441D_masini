import unittest

def culoare_ford():
	return "albastru"

def descriere_ford():
	return "Masina puternica"

class TestFord(unittest.TestCase):

	def test_culoare(self):
		self.assertEqual(culoare_ford(), "albastru")

	def test_descriere(self):
		self.assertEqual(descriere_ford(), "Masina puternica")

if __name__ == '__main__':
	unittest.main()
