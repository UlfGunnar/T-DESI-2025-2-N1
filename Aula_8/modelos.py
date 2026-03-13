class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def Buzinar(self):
        print(f'{self.modelo}: BIBIIIIiiii')

carro_01 = Carro('Renault','Kwid')
carro_02 = Carro('Chevrolet','Camaro amarelo')

print(f'{carro_01.modelo} da {carro_01.marca}')
print(f'{carro_02.modelo} da {carro_02.marca}')
print()
carro_01.Buzinar()
print()

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def Vender(self):
        self.estoque -= 1
        print(f'Venda concluida do {self.nome} sobrou {self.estoque} no estoque')

produto_01 = Produto('Batata doce', 67, 20)
produto_02 = Produto('Frango', 69, 21)

print('Marmita Fit do mercado:\n'
     f'{produto_01.nome} = {produto_01.estoque} no estoque\n'
     f'{produto_02.nome} = {produto_02.estoque} no estoque')
print()
produto_01.Vender()
print()

class Pessoa:
    def __init__(self, nome):
        self.nome = nome
    
    def Falar(self):
        print(f'Olá meu nome é {self.nome}')

class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome) # Super() = Chama o atributo da classe pai
        self.disciplina = disciplina

    def Dar_aula(self):
        print(f'Vamos começar a aula de {self.disciplina}')

func_01 = Professor('Anderson', 'Matemática')
func_01.Falar()
func_01.Dar_aula()

