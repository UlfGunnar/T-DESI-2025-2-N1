import sqlite3 

def Criar_Tabela():
    try:
        conexao = sqlite3.connect('modelagem.db')
        cursor = conexao.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tb_autor (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL
                       )
                    """)
        
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tb_livro (
                            ID_LIVRO INTEGER PRIMARY KEY AUTOINCREMENT,
                            titulo TEXT NOT NULL,
                            fk_id_autor INTEGER,
                            FOREIGN KEY (fk_id_autor) REFERENCES tb_autor(ID)
                       )
                    """)
        
    except sqlite3.Error as erro:
        print(f'Erro na criação das tabelas por {erro}')

    finally:
        cursor.close()
        conexao.close()

Criar_Tabela()
    