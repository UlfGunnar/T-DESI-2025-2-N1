# Programa que solicita 3 nomes de empresa e devolve ele em um Banner (Programação de aplicativos 05/03/2026) 

import os
import time

empresas = []

def Criar_Banner(titulo_empresa):
    # Função que imprime o Banner no terminal

    print("\n"
         f"{"*" * 5} {titulo_empresa} {"*" * 5}\n"
          "")

for c in range(3):
    nome_empresa = str(input(f'Digite o nome da {c+1}° empresa: '))
    empresas.append(nome_empresa)

os.system('cls')

for c in range(3):
    time.sleep(1)
    Criar_Banner(empresas[c])
    
