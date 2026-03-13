class Conta:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def Depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(self.saldo)
        else:
            print('Valor Inválido')

    def Sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(self.saldo)
        else: 
            print('Saldo insuficiente')

class Conta_Especial(Conta):
    def __init__(self, numero_conta, titular, saldo, limite):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite

    def Sacar(self, valor):
        if not self.saldo - valor < -500:
            self.saldo -= valor
            print(self.saldo)
        else: 
            print('Saldo insuficiente')      

conta_01 = Conta('001', 'Ulf', 1000)
conta_02 = Conta_Especial('002', 'Larissa', 1000, 500)
conta_01.Depositar(0)
conta_01.Sacar(10000)
conta_02.Sacar(600)