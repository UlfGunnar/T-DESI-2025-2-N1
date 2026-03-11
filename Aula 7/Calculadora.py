from Funcoes.Matematica import *
from Funcoes.Utils import *
import os

while True:
    os.system('cls')
    print('[1] - Somar\n'
          '[2] - Subtrair\n' 
          '[3] - Multiplicar\n' 
          '[4] - Divisão\n' 
          '[5] - Potência\n' 
          '[6] - Dobrar\n' 
          '[7] - N° Primo\n' 
          '[8] - Par ou Impar\n' 
          '[9] - Fatorial\n' \
          '[0] - Sair')

    opcao = int(input('Opcao: '))

    os.system('cls')
    match opcao:
        case 1:
            num1 = int(input('Digite o 1° valor: '))
            num2 = int(input('Digite o 2° valor: '))
            print(f'Resultado: {somar(num1, num2)}')
            input('ENTER para continuar')

        case 2:
            num1 = int(input('Digite o 1° valor: '))
            num2 = int(input('Digite o 2° valor: '))
            print(f'Resultado: {subtrair(num1, num2)}')
            input('ENTER para continuar')

        case 3:
            num1 = int(input('Digite o 1° valor: '))
            num2 = int(input('Digite o 2° valor: '))
            print(f'Resultado: {multiplicar(num1, num2)}')
            input('ENTER para continuar')

        case 4:
            num1 = int(input('Digite o 1° valor: '))
            num2 = int(input('Digite o 2° valor: '))
            print(f'Resultado: {dividir(num1, num2)}')
            input('ENTER para continuar')

        case 5:
            num1 = int(input('Digite o valor base: '))
            num2 = int(input('Digite o valor potência: '))
            print(f'Resultado: {potencializar(num1, num2)}')
            input('ENTER para continuar')

        case 6:
            num1 = int(input('Digite algum valor: '))
            print(f'Resultado: {dobrar(num1)}')
            input('ENTER para continuar')

        case 7:
            num1 = int(input('Digite algum valor: '))
            print(f'Resultado: {verificar_Primo(num1)}')
            input('ENTER para continuar')

        case 8:
            num1 = int(input('Digite algum valor: '))
            print(f'Resultado: {verificar_parimpar(num1)}')
            input('ENTER para continuar')

        case 9:
            num1 = int(input('Digite algum valor: '))
            print(f'Resultado: {fatorial(num1)}')
            input('ENTER para continuar')

        case 0:
            break
