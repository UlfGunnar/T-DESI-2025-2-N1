from modelagem_8 import Criar_Tabela
import sqlite3

def Excluir_tabela():
    try:
        conexao = sqlite3.connect('modelagem.db')
        cursor = conexao.cursor()

        cursor.execute("""
                        DROP TABLE IF EXISTS tb_autor
                    """)

        print('Tabela excluida!')

    except sqlite3.Error as erro:
        print(f'Erro na operação por {erro}')

    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    Criar_Tabela()
    Excluir_tabela()

    try:
        conexao = sqlite3.connect('modelagem.db')
        cursor = conexao.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tb_autor (
                            id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            nascimento DATE
                        )
                        """)
        
        print('Tabela criada!')

    except sqlite3.Error as erro:
        print(f'Tabela não craida por {erro}')

    finally:
        cursor.close()
        conexao.close()


      
