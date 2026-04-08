import unittest
from Aula_14.Funções.matematica import Somar

class Test_matematica(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(Somar(2, 2), 4)

if __name__ == "__main__":
    unittest.main()