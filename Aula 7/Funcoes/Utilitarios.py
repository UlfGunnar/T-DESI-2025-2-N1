def salvar_senha(servico, senha):
    linha = f'{servico}:{senha}\n'

    with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula 7\Saves\senhas.txt', 'a') as arquivo:
        arquivo.write(linha + '\n')

def listar_senhas():
    try:
        with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula 7\Saves\senhas.txt', 'r') as arquivo:
             return arquivo.read()
        
    except FileNotFoundError:
        return 'Nenhuma senha cadastrada ainda.'
    
if __name__ == '__main__':
     print('Testando salvamento...')
     salvar_senha('TesteApp', '1234')
     print(listar_senhas())