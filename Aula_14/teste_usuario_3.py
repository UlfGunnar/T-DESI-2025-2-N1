import unittest
import sqlite3

class Test_user(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(':memory:')

        print('Preparando ambiente')

    def test_Salvar(self):
        pass
    
    def test_Listar(self):
        pass
    
    def test_Deletar(self):
        pass

    def tearDown(self):
        self.conexao.close()

        print('Limpando')

if __name__ == "__main__":
    unittest.main()