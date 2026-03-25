import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))       # Pega o diretório onde está o script atual (ex: Aula_10/Read)
pasta_dados = os.path.join(base_dir, '..', 'Dados')         # Sobe uma pasta para Aula_10, e entra em dados
pasta_dados = os.path.normpath(pasta_dados)                 # Resolve o caminho absoluto e normaliza para evitar erros
caminho_bd = os.path.join(pasta_dados, 'dados_escola.db')   # Caminho completo para o banco

conexao = sqlite3.connect(caminho_bd)
cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos") 
resultado_bruto = cursor.fetchall()

lista_produtos_tratada = []
for linha in resultado_bruto:
    produto_dicionario = {
        "id": linha[0],
        "nome": linha[1],
        "matricula": linha[2]
    }
    lista_produtos_tratada.append(produto_dicionario)

conexao.close()

print("--- RELATÓRIO DO SISTEMA ---")
for produto in lista_produtos_tratada:
    print(f"[{produto['id']}] Nome: {produto['nome']} | Matrícula: {produto['matricula']}")