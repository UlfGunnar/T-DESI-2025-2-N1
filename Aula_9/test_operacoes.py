import unittest
from Funcoes.operacoes import somar, par_impar

class TestesOperacoes(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(10, 5), 15)
    
    def test_par(self):
        self.assertTrue(par_impar(2))
        
    def test_impar(self):
        self.assertFalse(par_impar(7))

if __name__ == '__main__':
    unittest.main()