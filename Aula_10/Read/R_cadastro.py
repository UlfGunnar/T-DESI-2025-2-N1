import sqlite3
import os

def Mostrar_pessoas():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pasta_dados = os.path.join(base_dir, '..', 'Dados')
    pasta_dados = os.path.normpath(pasta_dados)
    caminho = os.path.join(pasta_dados, 'dados_cadastro.db')
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    conexao = sqlite3.connect(caminho)
    cursor = conexao.cursor() 

    cursor.execute('SELECT * FROM pessoas')
    resultado_bruto = cursor.fetchall()

    resultado_tratado = []
    for linha in resultado_bruto:
        pessoa_dicionario = {
            'id': linha[0],
            'nome': linha[1],
            'idade': linha[2]
        }

        resultado_tratado.append(pessoa_dicionario)

    cursor.close()
    conexao.close()
    return resultado_tratado

    