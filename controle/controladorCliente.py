from entidades.cliente import Cliente
from datetime import date
from entidades.cnh import Cnh

class ControladoCliente():
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, nome: str, cpf: int, data_nascimento: date, endereco: str, cnh: Cnh):
        for cliente in self.clientes:
            if cliente.nome == nome:
                print("Cliente já possui cadastro")
                return
        
        novo_cliente = Cliente(nome, cpf, data_nascimento, endereco, cnh)
        self.clientes.append(novo_cliente)
        print(f"Cliente {novo_cliente.nome} registrado")
        return novo_cliente
    
    def pode_alugar(self) -> bool:
        if self.cnh.cnh_valida():
            return True
        return False
                
    def listar_clientes(self):
        return self.clientes
