# Programa que tem a função de criar uma tabela com SQL

import sqlite3
import os

def Criar_tabela():
    try:
        dir_name = os.path.dirname(os.path.abspath(__file__))
        pasta_dados = os.path.join(dir_name, 'Dados')
        os.makedirs(pasta_dados, exist_ok=True)
        caminho_db = os.path.join(pasta_dados, 'meu_banco.db')

        conexao = sqlite3.connect(caminho_db)
        cursor = conexao.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS tb_produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
                )""")
        
        print('Tabela criada com sucesso!')

    except sqlite3.Error as erro:
        print(f'Operação cancelada por {erro}')

    finally:
        cursor.close()
        conexao.close()

Criar_tabela()
