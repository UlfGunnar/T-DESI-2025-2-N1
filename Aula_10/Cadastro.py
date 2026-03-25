from Create.C_cadastro import *
from Read.R_cadastro import *
import os

Criar_conexao()
Criar_Tabela()

while True:
    os.system('cls')
    print('--- MENU ---\n' 
          '[1] - Cadastrar pessoa\n' 
          '[2] - Listar itens\n' \
          '[3] - Sair')
    opcao = int(input('Opção: '))

    match opcao:
        case 1:
            os.system('cls')

            nome_temp = str(input('Digite o nome da pessoa: '))
            idade_temp = int(input(f'Quantos anos {nome_temp} tem?: '))

            Cadastrar(nome_temp, idade_temp)

        case 2:
            pass

        case 3:
            Sair()
            break

