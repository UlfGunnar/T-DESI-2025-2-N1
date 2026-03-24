import unittest
from Funcoes.banco import Sacar, Depoisitar


class Testes_Banco(unittest.TestCase):
    def test_sacar(self):
        self.assertEqual(Sacar(100,100), 0)

    def test_depositar(self):
        self.assertEqual(Depoisitar(100,0), 100)


if __name__ == "__main__":
    unittest.main()