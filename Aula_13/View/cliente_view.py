from Model.cliente import Cliente
from dao.cliente_dao import ClienteDAO
from colorama import Fore, init
import time
import os

dao = ClienteDAO()
init()

def Menu():
    while True:
        os.system('cls')
        print(Fore.CYAN + '--- GERENCIAMENTO DE CLIENTES ---\n' 
              '[1] - Cadastrar\n' 
              '[2] - Listar\n' 
              '[3] - Procurar\n'
              '[4] - Sair\n')
         
        try:
            opcao = int(input('Opção: '))
        
        except ValueError:
            Aviso_campo()
            continue

    
        if opcao > 4 or opcao < 1:
           print(Fore.RED + 'Opção inválida! Digite uma opção entre 1 e 4. Voltando ao menu...')
           time.sleep(2)
           continue

        match opcao:
            case 1:
                os.system('cls')
                print(Fore.CYAN + '--- CADASTRO DE CLIENTES ---')
                nome_cliente = str(input('Digite o nome do cliente: ')).strip()
                email_cliente = str(input('Digite o email do cliente: ')).strip()

                if not nome_cliente or not email_cliente:
                    Aviso_campo()
                    continue

                tuple_cliente = Cliente(nome_cliente, email_cliente)
                dao.Salvar(tuple_cliente)

            case 2:
                Lista_cliente = dao.Listar_todos()
                
                os.system('cls')
                print(Fore.CYAN + '--- LISTA DE CLIENTES ---\n')

                print(f"{'ID'} {'Nome':<20} {'Email':<30}")
                print("-" * 55)
                for linha in Lista_cliente:
                    print(f"{linha['id']:03} {linha['nome']:<20} {linha['email']:<30}")

                print()
                input('ENTER para voltar ao MENU')

            case 3:
                os.system('cls')
                print('--- BUSCA DE CLIENTES ---')

                try:
                    id_busca =  int(input(Fore.CYAN + 'Digite o ID que queira buscar: '))

                except ValueError:
                    Aviso_campo()
                    continue

                busca_cliente = dao.Buscar_por_id(id_busca)

                if busca_cliente is None:
                    print(Fore.RED + 'Cliente inexistente! Voltando ao menu...')
                    time.sleep(2)
                    continue
                
                print()
                print('--- RESULTADO ---')
                print(Fore.CYAN + f'[{busca_cliente[0]:03}] nome: {busca_cliente[1]:<20} email: {busca_cliente[2]:<30}\n')
                
                Sub_menu(id_busca)

            case 4:
                os.system('cls')
                print(Fore.BLACK + 'Saindo...')
                time.sleep(2)
                break

                
def Sub_menu(id_cliente):
    print(Fore.CYAN + '--- UTILIDADES ---\n'
          '[1] - Atualizar\n' \
          '[2] - Deletar\n' \
          '[3] - Voltar')
    
    try:
        sub_opcao = int(input('Opção: '))

    except ValueError:
        Aviso_campo()
        return False

    if sub_opcao > 3 or sub_opcao < 1:
        print(Fore.RED + 'Opção inválida! Digite uma opção entre 1 e 3. Voltando ao menu...')
        return False

    match sub_opcao:
        case 1:
            os.system('cls')
            print(Fore.CYAN + '--- ATUALIZAR DADOS ---')
            novo_nome = str(input('Novo nome: '))
            novo_email = str(input('Novo email: '))

            if not novo_nome or not novo_email:
                Aviso_campo()
                return False
            
            novo_cliente = Cliente(novo_nome, novo_email)
            dao.Atualizar(novo_cliente, id_cliente)

        case 2:
            dao.Delatar(id_cliente)

def Aviso_campo():
    print(Fore.RED + 'Por favor, preencha os campos! Voltando ao menu...')
    time.sleep(2)
    
        







                
