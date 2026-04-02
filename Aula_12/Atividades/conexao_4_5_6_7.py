import sqlite3

def Criar_conexao(caminho):
    try:
        conex = sqlite3.connect(caminho)

        print('Conexão feita!')
        return (True, conex)

    except sqlite3.Error as erro:
        with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula_12\Atividades\erros_log.txt', 'w') as erros_log:
            msg = f'Falha na conexão por {erro}'
            erros_log.write(msg)

        return (False, print('Erro na conexão'))
    
def executar_ddl(conexao,query_sql):
    try:
       cursor = conexao.cursor() 
       cursor.execute(query_sql)

       print('Tabela criada')

    except sqlite3.Error as erro:
        print(f'Erro na operação {erro}')

if __name__ == "__main__":
    conn = Criar_conexao(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula_12\Database\meu_banco.db')

    if conn[0] == False:
        print('Iniciando o programa em modo offline...')

    else:
        comando = """
                    CREATE TABLE IF NOT EXISTS pessoa (
                        CPF INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL
                    )
                """

        executar_ddl(conn[1],comando)