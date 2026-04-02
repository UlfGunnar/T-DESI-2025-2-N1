import sqlite3

def Criar_Tabela():
    try:
        conexao = sqlite3.connect("meu_banco.db")
        cursor = conexao.cursor()

        cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tb_categoria (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        conteudo TEXT NOT NULL
                    )
        """)

        print("tabela criada com sucesso!")

    except sqlite3.Error as erro:
        print(f"Operação cancelada por {erro}")

    finally:
        cursor.close()
        conexao.close()

Criar_Tabela()