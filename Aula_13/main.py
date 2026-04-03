from Model.cliente import Cliente
from dao.cliente_dao import ClienteDAO

dao = ClienteDAO()
dao.Criar_tabela()

cliente_01 = Cliente('Ulf', 'ulfgunnar6@gmail.com')

dao.Salvar(cliente_01)

    
