from Funções.matematica import Dividir
import unittest

class test_matematica(unittest.TestCase):
    def test_dividir(self):
        with self.assertRaises(ZeroDivisionError):
            Dividir(10, 0)

if __name__ == "__main__":
    unittest.main()