class paciente:
    def __init__(self, nome, diagnostico, cor_pulseira, contato):
        self.nome = nome
        self.diagnostico = diagnostico
        self.cor_pulseira = cor_pulseira
        self.contato = contato

    def cadastro(self):
        print(f'{self.nome}\n{self.diagnostico}\n{self.cor_pulseira}\n{self.contato}')

paciente_01 = paciente("Lucas", 'Gravido', 'Vermelho', 4740028922)
paciente.cadastro(paciente_01)