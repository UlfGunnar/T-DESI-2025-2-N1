import sqlite3
import os

def Criar_conexao():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta_dados = os.path.join(base_dir, '..', 'Dados')
    pasta_dados = os.path.normpath(pasta_dados)
    caminho = os.path.join(pasta_dados, 'dados_cadastro.db')
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    global conexao, cursor
    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor() 

def Criar_Tabela():
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pessoas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL
                    )
                   """)
    
def Cadastrar(nome, idade):
    comando_sql = 'INSERT INTO pessoas (nome, idade) VALUES (?, ?)'
    valores = (nome, idade)
    cursor.execute(comando_sql, valores)
    conexao.commit()

def Sair():
    cursor.close()
    conexao.close()