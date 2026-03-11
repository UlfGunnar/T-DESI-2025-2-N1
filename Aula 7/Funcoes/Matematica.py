def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print('Não é possivel dividir por 0')

if __name__ == '__main__':
    print('Matemática importada com sucesso!')

