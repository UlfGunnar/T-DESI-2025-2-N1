from Create.C_cadastro import *
from Read.R_cadastro import Mostrar_pessoas
from colorama import Fore 
import time
import os

def Mensagem_erro():
    os.system('cls')
    print(Fore.RED + 'Opção Inválida!')
    time.sleep(2)

Criar_conexao()
Criar_Tabela()

while True:
    os.system('cls')
    print(Fore.WHITE +'--- MENU ---\n' 
          '[1] - Cadastrar pessoa\n' 
          '[2] - Listar itens\n' \
          '[3] - Sair')
    
    try:
        opcao = int(input(Fore.LIGHTCYAN_EX + 'Opção: '))

        if opcao > 3 or opcao < 1:
            Mensagem_erro()
            continue

        match opcao:
            case 1:
                os.system('cls')

                try:
                    nome_temp = str(input(Fore.LIGHTCYAN_EX + f'Digite o nome da pessoa: '))
                    idade_temp = int(input(f'Quantos anos {nome_temp} tem?: '))

                    Cadastrar(nome_temp, idade_temp)
                    print(Fore.LIGHTGREEN_EX + "Cadastro Finalizado!")
                    time.sleep(2)

                except ValueError:
                    os.system('cls')
                    print(Fore.RED + 'Dado Inválido!')
                    time.sleep(2)

            case 2:
                os.system('cls')
                lista_pessoas = Mostrar_pessoas()

                print(Fore.WHITE + '--- Pessoas Cadastradas ---')
                for linha in lista_pessoas:
                    print(f'{linha['id']} - nome: {linha['nome']} idade: {linha['idade']}')
                input('ENTER para voltar')

            case 3:
                os.system('cls')
                print(Fore.BLACK + 'Saindo...')
                time.sleep(1)
                Sair()
                break
    
    except ValueError:
        Mensagem_erro()
