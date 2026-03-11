def potencializar(x, y):
    return x ** y

def dobrar(x):
    return x * 2

def verificar_Primo(x):
    if x == 2:
        return 'NÃO É PRIMO'

    for c in range(x):   
        if c <= 1:
            continue
        else:
            if x % c == 0:
                return 'NÃO É PRIMO'
            
    return 'É PRIMO'

def fatorial(x):
    fat = 1

    for c  in range(x):
        fat *= (c + 1)

    return fat

def verificar_parimpar(x):
    if x % 2 == 0:
        return 'PAR'
    else: 
        return 'IMPAR'
    

