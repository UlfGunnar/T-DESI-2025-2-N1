from Model.cliente import Cliente
from colorama import Fore, init
import time
import sqlite3
import os

init()

base_dir = os.path.dirname(os.path.abspath(__file__))
pasta_dados = os.path.join(base_dir, '..', 'Database')
pasta_dados = os.path.normpath(pasta_dados)
caminho = os.path.join(pasta_dados, 'dados_clientes.db')
os.makedirs(os.path.dirname(caminho), exist_ok=True)

class ClienteDAO:
    def __init__(self, db_path: str = caminho):
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
            print(Fore.RED + f'Erro na operação por {erro}')
            time.sleep(2)

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

            print(Fore.LIGHTGREEN_EX + 'Valores inserido na tabela!')
            time.sleep(2)

        except sqlite3.Error as erro:
            print(Fore.RED + f'Erro ao inserir valores por {erro}')
            time.sleep(2)

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
            print(Fore.RED + f'Falha na operação por {erro}')
            time.sleep(2)

        finally:
            cursor.close()
            conexao.close()

    def Buscar_por_id(self, id: int):
        conexao = sqlite3.connect(self.db_path)
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM cliente WHERE id = ?', (id,))
        resultado_bruto = cursor.fetchall()

        if len(resultado_bruto) == 0:
            return None

        return (resultado_bruto[0][0], resultado_bruto[0][1], resultado_bruto[0][2])
    
    def Atualizar(self, cliente: Cliente, id: int):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
        
            cursor.execute('UPDATE cliente SET nome = ?, email = ? WHERE id = ?', (cliente.nome, cliente.email, id))
            conexao.commit()

            print(Fore.LIGHTGREEN_EX + 'Informações do cliente atualizado!')
            time.sleep(2)
    
        except sqlite3.Error as erro:
            print(Fore.RED + f'Falha na atualização do cliente por {erro}')
            time.sleep(2)

        finally:
            cursor.close()
            conexao.close()

    def Delatar(self, id: int):
        try:
            conexao = sqlite3.connect(self.db_path)
            cursor = conexao.cursor()
            
            cursor.execute('DELETE FROM cliente WHERE id = ?', (id,))

            conexao.commit()
            print(Fore.LIGHTGREEN_EX + 'Cliente deletado!')
            time.sleep(2)

        except sqlite3.Error as erro:
            print(Fore.RED + f'Operação cancelada por {erro}')
            time.sleep(2)

        finally:
            cursor.close()
            conexao.close()
