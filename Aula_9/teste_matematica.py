from Funcoes.matematica import calcular_dobro
import unittest

class TestesMatematica(unittest.TestCase):
    def test_calcular_dobro_positivo(self):
        self.assertEqual(calcular_dobro(5), 10)

    def test_calcular_dobro_negativo(self):
        self.assertEqual(calcular_dobro(-3), -6)

if __name__ == '__main__':
    unittest.main()
