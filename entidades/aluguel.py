from datetime import date
from entidades.cliente import Cliente
from entidades.carro import Carro
from entidades.moto import Moto
from entidades.caminhao import Caminhao
from entidades.automovel import Automovel

class Aluguel():
    def __init__(self, cliente: Cliente, automovel: Automovel, data_inicio: date, data_final: date):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(automovel, Automovel):
            self.__automovel = automovel
        if isinstance(data_inicio, date):
            self.__data_inicio = data_inicio
        if isinstance(data_final, date):
            self.__data_final = data_final

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente

    @property
    def automovel(self):
        return self.__automovel
    
    @automovel.setter
    def automovel(self, automovel: Automovel):
        if isinstance(automovel, Automovel):
            self.__automovel = automovel 

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        if isinstance(data_inicio, date):
            self.__data_inicio  = data_inicio
    
    @property
    def data_final(self):
        return self.__data_final

    @data_final.setter
    def data_final(self, data_final: date):
        if isinstance(data_final, date):
            self.__data_final  = data_final

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




            