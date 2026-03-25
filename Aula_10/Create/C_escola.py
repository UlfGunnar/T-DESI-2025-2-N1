import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))       
pasta_dados = os.path.join(base_dir, '..', 'Dados')       
pasta_dados = os.path.normpath(pasta_dados)                
caminho = os.path.join(pasta_dados, 'dados_escola.db') 
os.makedirs(os.path.dirname(caminho), exist_ok=True)

conexao = sqlite3.connect(caminho)
cursor = conexao.cursor()

nome_aluno = 'Larissa Bergmann'
matricula_aluno = 2

cursor.execute("""
               CREATE TABLE IF NOT EXISTS alunos (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               matricula INTEGER NOT NULL
               )
               """)

comando_sql = 'INSERT INTO alunos (nome, matricula) VALUES (?, ?)'
valores = (nome_aluno, matricula_aluno)
cursor.execute(comando_sql, valores)

conexao.commit()
cursor.close()
conexao.close()
print("Aluno cadastrado com sucesso!")