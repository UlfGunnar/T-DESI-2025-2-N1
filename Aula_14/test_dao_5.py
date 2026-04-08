import unittest
import sqlite3

class Produto:
    def __init__(self, nome, quantidade_estoque):
        self.nome = nome
        self.quantidade_estoque = quantidade_estoque

class ProdutoDAO:
    def __init__(self, conexao):
         self.conexao = conexao

    def Salvar(self, produto: Produto):
        cursor = self.conexao.cursor()
        cursor.execute('INSERT INTO produto (nome, quantidade_estoque) VALUES (?, ?)', (produto.nome, produto.quantidade_estoque))

        self.conexao.commit()

        produto.id = cursor.lastrowid
        return produto

    def buscar_por_id(self, id_produto):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM produto WHERE id = ?", (id_produto,))
        linha = cursor.fetchone()
        
        return linha

class Teste_ProdutoDAO(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(':memory:')
        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade_estoque INTEGER NOT NULL
            )
        """)   
        self.dao = ProdutoDAO(self.conexao)
    
    def test_salvar_e_busca(self):
        Produto_01 = Produto('Corote', 67)
        Produto_salvo = self.dao.Salvar(Produto_01)

        Produto_recuperado = self.dao.buscar_por_id(Produto_salvo.id)

        self.assertIsNotNone(Produto_recuperado)
        self.assertEqual(Produto_01.nome, Produto_recuperado[1])
        self.assertEqual(Produto_01.quantidade_estoque, Produto_recuperado[2])
        
    def tearDown(self):
        self.conexao.close()

if __name__ == '__main__':
    unittest.main()


