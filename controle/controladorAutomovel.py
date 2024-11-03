from abc import ABC, abstractmethod
from limite.telaAutomovel import TelaAutomovel

# Classe abstrata ControladorAutomovel define as operações de controle de automóveis
class ControladorAutomovel(ABC):
    def __init__(self):
        self.__tela_automovel = TelaAutomovel
    
    @property
    def tela_automovel(self):
        return self.__tela_automovel
    
    @abstractmethod
    def incluir_automovel(self):
        pass

    @abstractmethod
    def excluir_automovel(self):
        pass

    @abstractmethod
    def retornar(self):
        pass

    @abstractmethod
    def listar(self):
        pass
    