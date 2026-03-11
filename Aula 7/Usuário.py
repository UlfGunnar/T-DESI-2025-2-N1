anotacao = str(input('Digite algo para salvar: '))

with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula 7\Saves\anotacao.txt', 'a') as arquivo:
    arquivo.write(anotacao + '\n')
    print('Saldo gravado com sucesso!')

with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula 7\Saves\anotacao.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f'Você salvou: {anotacao}')