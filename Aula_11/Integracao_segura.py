import sqlite3

def deletar_funcionario(id):
    try: 
        id = int(input("Digite o ID do funcionario: "))

        conexao = sqlite3.connect('funcionarios.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM funcionarios WHERE id = ?', (id))
        pesquisa_funcionario = cursor.fetchall()

        if not pesquisa_funcionario:
            print('ID não exite!')
            return False
        
        else:
            opcao = str(input('Você tem certeza que quer deletar? [s/n]: '))
            
            if opcao == 's':
                cursor.execute('DELETE FROM funcionario WHERE id = ?', (id))
                cursor.commit()
                print('Funcionario deletado!')
                return True
            
            elif opcao == 'n':
                return False

    except sqlite3.Error as erro:
        print(f'Operação cancelada por {erro}')

    finally:
        cursor.close()
        conexao.close()

while True:
    id_func = int(input('Digite o ID do funcionário para deletar: '))

    deletar_funcionario(id_func)
    