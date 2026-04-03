from Model.cliente import Cliente
import sqlite3 

class ClienteDAO:
    def __init__(self, db_path: str = 'meu_banco.db'):
        self.db_path = db_path

    def Criar_tabela(self):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()

            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS cliente (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                email TEXT NOT NULL
                                )
                            """)
        
        except sqlite3.Error as erro:
            print(f'Erro na operação por {erro}')

        finally:
            cursor.close()
            conexao.close()

    def Salvar(self, cliente: Cliente):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()

            comando_sql = "INSERT INTO cliente (nome, email) VALUES (?, ?)"
            valores = (cliente.nome, cliente.email)

            cursor.execute(comando_sql, valores)
            conexao.commit()

            print('Valores inserido na tabela!')

        except sqlite3.Error as erro:
            print(f'Erro ao inserir valores por {erro}')

        finally:
            cursor.close()
            conexao.close()
    
    def Listar_todos(self):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()

            cursor.execute('SELECT * FROM cliente')
            resultado_bruto = cursor.fetchall()
            resultado_tratado = []
            
            for linha in resultado_bruto:
                cliente = {
                    'id': linha[0],
                    'nome': linha[1],
                    'email': linha[2]
                }

                resultado_tratado.append(cliente)

            return resultado_tratado

        except sqlite3.Error as erro:
            print(f'Falha na operação por {erro}')

        finally:
            cursor.close()
            conexao.close()

    def Buscar_por_id(self, id: int):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM cliente WHERE id = ?', (id))
        resultado_bruto = cursor.fetchall()

        if resultado_bruto is None:
            return None

        return Cliente(resultado_bruto[0][1], resultado_bruto[0][2])
    
    def Atualizar(self, cliente: Cliente):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
        
            cursor.execute('UPDATE cliente SET nome = ?, email = ? WHERE id = ?', (cliente.nome, cliente.email, cliente.id))
            conexao.commit()

            print('Informações do cliente atualizado!')
    
        except sqlite3.Error as erro:
            print(f'Falha na atualização do cliente por {erro}')

        finally:
            cursor.close()
            conexao.close()

    def Delatar(self, id: int):
        busca_cliente = self.Buscar_por_id(id)

        if busca_cliente is None:
            print("Cliente inexistente!") 
            return False
        
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            
            cursor.execute('DELETE FROM cliente WHERE id = ?', (id))

            conexao.commit()
            print('Cliente deletado!')

        except sqlite3.Error as erro:
            print(f'Operação cancelada por {erro}')

        finally:
            cursor.close()
            conexao.close()

            
        
            






