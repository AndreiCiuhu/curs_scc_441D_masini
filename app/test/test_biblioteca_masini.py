import unittest
from app.lib.biblioteca_masini import get_culoare_bmw

class TestBMW(unittest.TestCase):
    def test_culoare(self):
        self.assertEqual(get_culoare_bmw(), "Culoarea oficiala BMW M este albastru.")

if __name__ == '__main__':
    unittest.main()
