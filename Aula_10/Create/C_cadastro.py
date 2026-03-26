import sqlite3
import os

def Criar_Tabela():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta_dados = os.path.join(base_dir, '..', 'Dados')
    pasta_dados = os.path.normpath(pasta_dados)
    caminho = os.path.join(pasta_dados, 'dados_cadastro.db')
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor() 

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
                    )
                   """)
    
    cursor.close()
    conexao.close()
    
def Cadastrar(nome, idade):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta_dados = os.path.join(base_dir, '..', 'Dados')
    pasta_dados = os.path.normpath(pasta_dados)
    caminho = os.path.join(pasta_dados, 'dados_cadastro.db')
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor() 

    comando_sql = 'INSERT INTO pessoas (nome, idade) VALUES (?, ?)'
    valores = (nome, idade)
    cursor.execute(comando_sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()
