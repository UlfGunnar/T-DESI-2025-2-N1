import unittest
import sqlite3

class Paciente:
    def __init__(self, cpf, nome, ano_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.ano_nascimento = ano_nascimento

class Paciente_DAO:
    def __init__(self, conexao):
        self.conexao = conexao

    def Salvar(self, paciente):
        cursor = self.conexao.cursor()

        cursor.execute('INSERT INTO Paciente (cpf, nome, ano_nascimento) VALUES (?, ?, ?)', (paciente.cpf, paciente.nome, paciente.ano_nascimento))
        self.conexao.commit()

    def Buscar_por_CPF(self, cpf_usuario):
        cursor = self.conexao.cursor()

        cursor.execute('SELECT * FROM Paciente WHERE cpf = ?', (cpf_usuario,))
        busca_usuario = cursor.fetchone()

        if not busca_usuario:
            return None
        
        return busca_usuario
    
    def Atualizar(self, cpf_usuario, novo_nome):
        cursor = self.conexao.cursor()
        
        cursor.execute('UPDATE Paciente SET nome = ? WHERE cpf = ?', (novo_nome, cpf_usuario))
        self.conexao.commit()

    def Deletar(self, cpf_usuario):
        cursor = self.conexao.cursor()

        cursor.execute('DELETE FROM Paciente WHERE cpf = ?', (cpf_usuario,))
        self.conexao.commit()
    
class Teste_Paciente_DAO(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(':memory:')
        self.conexao.execute(
                            """CREATE TABLE IF NOT EXISTS Paciente (
                                cpf TEXT PRIMARY KEY,
                                nome TEXT NOT NULL,
                                ano_nascimento TEXT NOT NULL
                               )"""
                            )
        self.dao = Paciente_DAO(self.conexao)

    def test_Paciente_DAO(self):
        usuario_original = Paciente("80133157970", "Ulf Gunnar", "31032005")
        self.dao.Salvar(usuario_original)
        usuario_recuperado = self.dao.Buscar_por_CPF(usuario_original.cpf)

        self.assertIsNotNone(usuario_recuperado)
        self.assertEqual(usuario_original.nome, usuario_recuperado[1])

        usuario_atualizado = self.dao.Atualizar(usuario_original.cpf, "Ulf Gunnar Silva Pettersson")
        usuario_recuperado = self.dao.Buscar_por_CPF(usuario_original.cpf)

        self.assertEqual(usuario_recuperado[1], "Ulf Gunnar Silva Pettersson")

        self.dao.Deletar(usuario_original.cpf)
        usuario_recuperado = self.dao.Buscar_por_CPF(usuario_original.cpf)

        self.assertIsNone(usuario_recuperado)


    def tearDown(self):
        self.conexao.close()

if __name__ == "__main__":
    unittest.main()

