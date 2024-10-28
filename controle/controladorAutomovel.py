from abc import ABC, abstractmethod
from limite.telaAutomovel import TelaAutomovel
from entidades.automovel import Automovel
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
    