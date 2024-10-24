from abc import ABC, abstractmethod
from limite.telaAutomovel import TelaAutomovel
from entidades.automovel import Automovel
class ControladorAutomovel(ABC):
    def __init__(self):
        self.__tela_automovel = TelaAutomovel
        self.__frota = []
    
    @property
    def tela_automovel(self):
        return self.__tela_automovel
    
    @abstractmethod
    def incluir_automovel(self):
        while True:
            dados_automovel = self.__tela_automovel.pega_infomacao_automovel(self)

            placa = dados_automovel["placa"]

            modelo = dados_automovel["modelo"]

            marca = dados_automovel["marca"]
                 
            ano = dados_automovel["ano"]

            valor_por_dia = dados_automovel["valor_por_dia"]
                
            automovel = Automovel(placa, modelo, marca, ano, valor_por_dia)
            self.__frota.append(automovel)

            print("Automovel incluído com sucesso!")
            break

    @abstractmethod
    def excluir_automovel(self):
        placa_automovel = self.__tela_automovel.seleciona_automovel(self)
        automovel = self.seleciona_automovel(placa_automovel)

        if automovel is not None:
            self.__frota.remove(automovel)
            print("Automóvel excluído com sucesso!")
        else:
            print("ATENCAO: Automóvel não existente")
    
    def retornar(self):
        print("Retornando ao menu principal...")
        return
    