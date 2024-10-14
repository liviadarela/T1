from entidades.cliente import Cliente
class ClienteView:
    def exibir_clientes(self, clientes):
        if not clientes:
            print("Nenhum cliente cadastrado.")
        for cliente in clientes:
            print(f'Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereço: {cliente.endereco}')
