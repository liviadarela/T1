from entidades.aluguel import Aluguel
from datetime import date
from entidades.cliente import Cliente
from entidades.carro import Carro
from entidades.moto import Moto
from entidades.caminhao import Caminhao
from entidades.automovel import Automovel


class ControladorAluguel():
    def __init__(self):
        self.alugueis = []

    def categoria_valida(self, cliente: Cliente, automovel: Automovel) -> bool:
        if isinstance(automovel, Caminhao) and cliente.cnh.categoria == "C":
            return True
        elif isinstance(automovel, Moto) and (cliente.cnh.categoria == "A" or cliente.cnh.categoria == "AB"):
            return True
        elif isinstance(automovel, Carro) and (cliente.cnh.categoria == "B" or cliente.cnh.categoria == "AB"):
            return True
        else:
            return False
    
    def realizar_aluguel(self, cliente: Cliente, automovel: Automovel, data_inicio: date, data_final: date):
        if self.categoria_valida(cliente, automovel) and cliente.pode_alugar() and automovel.status == "Disponível":
            self.__automovel.status = "Indisponível"

            novo_aluguel = Aluguel(cliente, automovel, data_inicio, data_final)
            self.alugueis.append(novo_aluguel)

            print(f"Aluguel realizado.")
            return novo_aluguel
        
        else:
            return("Não foi possivel ralizar o aluguel.")

    def devolucao(self, aluguel):
        if aluguel in self.alugueis:
            self.alugueis.remove(aluguel)  
            aluguel.automovel.status = "Disponível" 
            return "Devolução realizada."
        else:
            return "Aluguel não encontrado."

    def listar_alugueis(self):
        return self.alugueis

    def alugueis_por_data(self, data_inicio_intervalo: date, data_final_intervalo: date):
        alugueis_no_intervalo = []
        
        for aluguel in self.alugueis:
            if (aluguel.data_inicio >= data_inicio_intervalo and aluguel.data_final <= data_final_intervalo):
                alugueis_no_intervalo.append(aluguel)
        
        return alugueis_no_intervalo