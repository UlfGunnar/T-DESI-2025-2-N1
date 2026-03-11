saldo = '1500'

with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula 7\Saves\saldo.txt', 'w') as arquivo:
    arquivo.write(saldo)
    print('Saldo gravado com sucesso!')

with open(r'C:\Users\ulf_pettersson\T-DESI-2025-2-N1\Aula 7\Saves\saldo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f'Saldo recuperado {conteudo}')