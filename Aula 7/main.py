from Funcoes.Utilitarios import *

def iniciar_sistema():
    print('--- GERENCIADOR DE SENHAS ---')
    opcao = input('Digite 1 para salvar ou 2 para listar: ')
    

    if opcao == '1':
        servico = input('Nome do serviço: ')
        senha = input('Digite a senha: ')
        salvar_senha(servico, senha)
        print('Salvo com sucesso!')

    elif opcao == '2':
        print('--- SUAS SENHAS ---')
        print(listar_senhas())

    else: 
        print('Opção invalída.')

if __name__ == "__main__":
    iniciar_sistema()