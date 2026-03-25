"""
    connect() parar abrir o arquivo

    cursor() para criar o executor

    execute() para disparar uma query 

    commit() para confirmar 

    close() para liberar o arquivo
"""

import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))       
pasta_dados = os.path.join(base_dir, '..', 'Dados')       
pasta_dados = os.path.normpath(pasta_dados)                
caminho = os.path.join(pasta_dados, 'dados_main.db') 
os.makedirs(os.path.dirname(caminho), exist_ok=True)

conexao = sqlite3.connect(caminho)
cursor = conexao.cursor()

nome_produto = "Teclado Mecânico"
preco_produto = 250.00

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
preco REAL NOT NULL
)
""")

comando_sql = "INSERT INTO produtos (nome, preco) VALUES (?, ?)"
valores = (nome_produto, preco_produto)
cursor.execute(comando_sql, valores)

conexao.commit()
cursor.close()
conexao.close()
print("Produto persistido com sucesso!")