from abc import ABC, abstractmethod
class TelaAutomovel(ABC):
    
    @abstractmethod
    def pega_infomacao_automovel(self):
        print("\n-------- AUTOMÓVEL----------")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        marca = input("Marca: ")
        ano = input("Ano: ")
        valor_por_dia = input("Valor por dia: ")
    
        return {
            "placa": placa,
            "modelo": modelo,
            "marca": marca,
            "ano": ano,
            "valor_por_dia": valor_por_dia,
        }

    @abstractmethod
    def mostra_automovel(self, dados_automovel):
        print("Placa: ", dados_automovel["placa"])
        print("Modelo: ", dados_automovel["modelo"])
        print("Marca: ", dados_automovel["marca"])
        print("Ano: ", dados_automovel["ano"])
        print("Valor por dia: ", dados_automovel["valor_por_dia"])

    def seleciona_automovel(self):
        placa = input("Placa do automovel que deseja buscar: ")
        return placa