# Programa que simula o uso de um Caixa eletrônico (Programação de aplicativos 03/03/2026)

import os
import time

LIMITE_DIARIO = 500
Saldo = 1000

def ERROR_Opcao(): 
    os.system('cls') 
    print('ERROR! Digite uma opção!')
    time.sleep(2)
    os.system('cls')
                
while True:
    print('='*30)
    print('[1] - Sacar dinheiro\n' 
          '[2] - Depositar dinheiro\n' 
          '[3] - Consultar Saldo\n' 
          '[4] - Sair')
    print('='*30)

    escolha_menu = input('Opção: ')

    os.system('cls')

    if not escolha_menu.strip():
        ERROR_Opcao()
        continue

    else:
        escolha_menu = int(escolha_menu)

        if escolha_menu >= 1 and escolha_menu <= 4:
            match escolha_menu:
                case 1:
                    Saque = input('Quanto você quer sacar?: R$')

                    if not Saque.strip():
                        ERROR_Opcao()
                        continue
                
                    else:
                        Saque = float(Saque)

                        if Saque > Saldo or Saque > LIMITE_DIARIO:
                            os.system('cls')
                            print('ERROR! Valor indisponível, por favor tente novamente!')
                            time.sleep(2)
                            os.system('cls')
                            continue

                        elif Saque <= 0:
                            os.system('cls')
                            print('ERROR! Valor inválido, por favor tente novamente!')
                            time.sleep(2)
                            os.system('cls')
                            continue

                        else:
                            Saldo -= Saque

                            print(f'Saque de {Saque:.2f} Confirmado!')
                            time.sleep(2)
                            os.system('cls')
                            continue

                case 2:
                    Deposito = input('Quanto que você quer depositar?: R$')

                    if not Deposito.strip():
                        ERROR_Opcao()
                        continue

                    else:
                        if Deposito <= 0:
                            os.system('cls')
                            print('ERROR! Valor inválido, por favor tente novamente!')
                            time.sleep(2)
                            os.system('cls')
                            continue

                        else:
                            Saldo += Deposito

                            print(f'Deposito de {Deposito:.2f} Confirmado!')
                            time.sleep(2)
                            os.system('cls')
                            continue

                case 3:
                    print('='*30)
                    print(f'Saldo: R${Saldo:.2f}')
                    print('=' *30)
                    input('Aperte ENTER para sair')
                    os.system('cls')

                case 4: 
                    print('Saindo...')
                    time.sleep(2)
                    break
    
        else: 
            os.system('cls')
            print('ERROR! Opção inválida, por favor tente novamente!')
            time.sleep(2)
            os.system('cls')
            continue