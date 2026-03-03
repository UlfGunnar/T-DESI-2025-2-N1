# Programa que simula uma loja onde você pode adicionar um item nela

import os
import time

def Cadastrar_Produto():
    print('='*30)
    nome = str(input("Qual arma você quer adicionar?: "))
    quant = int(input("Quantos teremos no estoque?: ")) 
    valor = int(input("E quanto custará?: R$"))

    Estoque.setdefault(f"{nome}", [quant, valor, nome])
    Carrinho.setdefault(f"{nome}", [0])

    os.system('cls')
    print('Produto adicionado!')
    time.sleep(1)
    os.system('cls')

Carrinho = {
    "AK-47": 0,
    "M4A1": 0,
    "AWP": 0,
    "Total_Pagar": 0
}

Estoque = {
    "AK-47": [21,2700,"AK-47"],
    "M4A1": [9, 2900,"M4A1"],
    "AWP": [26, 4750,"AWP"]
}

while True:
    os.system('cls')
    print('[1] - Mostrar produtos')
    print('[2] - Cadastrar Produtos')
    print('[3] - Pagar')

    escolha_menu = int(input("Opção: "))
    
    #os.system('cls')
    match escolha_menu:
        
        #========================#
        #====MOSTRAR PRODUTOS====#
        #========================#

        case 1: 
                print("="*30)
                print("O que você quer comprar?")
                for c, produtos in enumerate(Estoque.values()): # Mostra os produtos
                    print(f"[{c+1}] - {produtos[2]}")

                print('[0] - Voltar')
                escolha_produto = int(input('Opção: '))
                
                if escolha_produto == 0: 
                    continue
                
                elif escolha_produto > 0:
                    for c, produtos in enumerate(Estoque.values()): # Checa qual produto o usuário escolheu
                        if (c + 1) == escolha_produto:
                            if produtos[1] > 0: # Verifica se tem item no inventário 
                                print("="*30)
                                print(f'Temos {produtos[2]} cada uma por R${produtos[1]}')
                                Confirmacao = str(input("Você tem certeza? [sim/nao]: ")).lower()

                                if Confirmacao == "sim":
                                    produtos[0] -= 1                        # Diminui a quantidade no estoque
                                    Carrinho[f"{produtos[2]}"] += 1         # Adiciona no historico o item comprado
                                    Carrinho["Total_Pagar"] += produtos[1]  # Adiciona o valor do item no total

                                    os.system('cls')
                                    print(f"Compra confirmada!")
                                    time.sleep(1)
                                    os.system('cls')
                                    continue

                                else:
                                    print("ERROR VALOR INVÁLIDO! Encerrando app >:(")
                                    break
                
                else: 
                    print("ERROR VALOR INVÁLIDO! Encerrando app >:(")
                    break

        #==========================#
        #====CADASTRAR PRODUTOS====#
        #==========================#

        case 2:
            Cadastrar_Produto()
            continue

        #=================#
        #====PAGAMENTO====#
        #=================#

        case 3:
            print('='*30)
            print("Você comprou: ")

            for produtos in Estoque.values():
                if Carrinho[produtos[2]] > 0: 
                    print(f"[{produtos[2]}] {Carrinho[produtos[2]]} vezes")

            print(f"Total a pagar: R${Carrinho['Total_Pagar']}")
            print('='*30)
            escolha_pagamento = str(input('Pagar? [sim/nao]: ')).lower()
            
            if escolha_pagamento == "sim":
                os.system('cls')
                print("Pagamento confirmado! Encerrando o app...")
                time.sleep(1)
                break