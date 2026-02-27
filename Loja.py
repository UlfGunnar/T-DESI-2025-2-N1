# Programa que simula uma loja onde você pode adicionar um item nela

import os

def Cadastrar():
    nome = str(input("Qual arma você quer adicionar?: "))
    quant = int(input("Quantos teremos no estoque?: ")) 
    valor = int(input("E quanto custará?: R$"))

    Estoque.setdefault(f"{nome}", [quant, valor, nome])

Carrinho = {
    "AK-47": 0,
    "M4A1": 0,
    "AWP": 0,
    "Total_Pagar": 0
}

Estoque = {
    "AK-47": [21,2700,"AK47"],
    "M4A1": [9, 2900,"M4A1"],
    "AWP": [26, 4750,"AWP"]
}

while True:
    #os.system('cls')
    print('[1] - Mostrar produtos')
    print('[2] - Cadastrar Produtos')
    print('[3] - Pagar')
    print('SAIR para desligar o app')
    
    escolha_menu = input("Opção: ")
    
    #os.system('cls')
    match escolha_menu:
        
        case "1":
                for c, produtos in enumerate(Estoque.values()):
                    print(f"[{c+1}] - {produtos[2]}")

                print('VOLTAR para ir ao menu')
                escolha_produto = input('Opção: ')

                
                if type(escolha_produto) == str:
                    print('thau')
                    continue    
                
                else:
                    print('oieeeeeeee')
                    for c, produtos in enumerate(Estoque.values()):
                        if (c + 1) == escolha_produto :
                            print('oi')
                            input()

                            """
                            if produtos[1] > 0:
                                print(f'Temos {produtos[2]} Ak-47 cada uma por R${produtos[1]}')
                                Confirmacao = str(input("Você tem certeza? [sim/nao]: ")).lower()

                            if Confirmacao == "sim":
                                produtos[0] -= 1
                                Carrinho[f"{produtos[2]}"] += 1
                                Carrinho["Total_Pagar"] += produtos[1]

                                #os.system('cls')
                                print(f"Aqui já embrulhamos sua {produtos[2]}!")
                                continue

                            elif Confirmacao == "nao":
                                #os.system('cls')
                                continue
                
                            else:
                                print("ERROR VALOR INVÁLIDO! >:(")
                                break
                            """
"""

print('Você comprou: \n' \
     f'{Carrinho["AK-47"]} - AK47\n'
     f'{Carrinho["M4A1"]} - M4A1\n'
     f'{Carrinho["AWP"]} - AWP\n'
     f'Total a Pagar: R${Carrinho["Total_Pagar"]}')
"""