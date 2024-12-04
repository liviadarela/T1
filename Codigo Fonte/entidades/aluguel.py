from datetime import date
from entidades.cliente import Cliente
from entidades.automovel import Automovel
from exception.dadosInvalidosException import DadosInvalidoException


class Aluguel():
    def __init__(self, cliente: Cliente, automovel: Automovel, data_inicio: date, data_final: date):
        # inicializando todos os atributos como None
        self.__cliente = None
        self.__automovel = None
        self.__data_inicio = None
        self.__data_final  = None

        # Validações 
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            raise DadosInvalidoException("Cliente não condiz com o tipo desejado")
        
        if isinstance(automovel, Automovel):
            self.__automovel = automovel
        else:
            raise DadosInvalidoException("Automóvel não condiz com o tipo desejado")
        
        if isinstance(data_inicio, date):
            self.__data_inicio = data_inicio
        else:
            raise DadosInvalidoException("Data de Início não condiz com o tipo desejado")
        
        if isinstance(data_final, date):
            self.__data_final = data_final
        else:
            raise DadosInvalidoException("Data de final não condiz com o tipo desejado")

    # Getters e Setters
    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        else:
            raise DadosInvalidoException("Cliente não condiz com o tipo desejado")

    @property
    def automovel(self):
        return self.__automovel
    
    @automovel.setter
    def automovel(self, automovel: Automovel):
        if isinstance(automovel, Automovel):
            self.__automovel = automovel
        else:
            raise DadosInvalidoException("Automóvel não condiz com o tipo desejado")

    @property
    def data_inicio(self):
        return self.__data_inicio

    @data_inicio.setter
    def data_inicio(self, data_inicio: date):
        if isinstance(data_inicio, date):
            self.__data_inicio  = data_inicio
        else:
            raise DadosInvalidoException("Data de início não condiz com o tipo desejado")
    
    @property
    def data_final(self):
        return self.__data_final

    @data_final.setter
    def data_final(self, data_final: date):
        if isinstance(data_final, date):
            self.__data_final  = data_final
        else:
            raise DadosInvalidoException("Data de final não condiz com o tipo desejado")
