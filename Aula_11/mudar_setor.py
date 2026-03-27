import sqlite3

def mudar_setor_funcionario():
    try: 
        id = int(input("Digite o seu ID: "))
        novo_setor = str(input('Digite seu novo setor: '))

        conexao = sqlite3.connect('funcionarios.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id))
        pesquisa_funcionario = cursor.fetchall()

        if not pesquisa_funcionario:
            print('ID não exite!')
            return False
        
        cursor.execute('UPDATE produto SET setor = ? WHERE id = ?', (novo_setor, id))
        cursor.commit()
        print('Linha atualizada!')
        return True

    except sqlite3.Error as erro:
        print(f'Operação cancelada por {erro}')

    finally:
        cursor.close()
        conexao.close()
    