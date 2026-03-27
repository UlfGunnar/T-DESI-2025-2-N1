import sqlite3

def mudar_perfil_funcionario():
    try: 
        id = int(input("Digite o seu ID: "))
        novo_email = str(input('Digite seu novo email: '))
        novo_telefone = str(input('Digite seu telefone: '))

        conexao = sqlite3.connect('funcionarios.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id))
        pesquisa_funcionario = cursor.fetchall()

        if not pesquisa_funcionario:
            print('ID não exite!')
            return False
        
        cursor.execute('UPDATE produto SET email = ?, telefone = ? WHERE id = ?', (novo_email, novo_telefone,id))
        cursor.commit()
        print('Linha atualizada!')
        return True

    except sqlite3.Error as erro:
        print(f'Operação cancelada por {erro}')

    finally:
        cursor.close()
        conexao.close()
    