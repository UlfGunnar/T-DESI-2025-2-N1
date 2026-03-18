from builtins import print, input, int, ValueError, ZeroDivisionError
import os

while True:
    try:
        num_1 = int(input('Digite o primeiro valor: '))
        num_2 = int(input('Digite o segundo valor: '))

        print(f'Divisão {num_1} / {num_2} = {num_1 / num_2}')
        break
    except ValueError:
        os.system('cls')
        print('Digite um valor númerico!')
    except ZeroDivisionError:
        os.system('cls')
        print('É impossivel dividir por zero!')
