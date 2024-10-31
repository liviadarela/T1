from abc import ABC, abstractmethod

class Automovel(ABC):
    @abstractmethod
    def __init__(self, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        self.__placa = None
        self.__modelo = None
        self.__marca = None
        self.__ano = None
        self.__valor_por_dia = None
        
        if isinstance(placa, str):
            self.__placa = placa
        else:
            raise ValueError("Placa não condiz com o tipo desejado")
        
        if isinstance(modelo, str):
            self.__modelo = modelo
        else:
            raise ValueError("Modelo não condiz com o tipo desejado")
    
        if isinstance(marca, str):
            self.__marca = marca
        else:
            raise ValueError("Marca não condiz com o tipo desejado")
    
        if isinstance(ano, int):
            self.__ano = ano
        else:
            raise ValueError("Ano não condiz com o tipo desejado")
        
        if isinstance(valor_por_dia, float):
            self.__valor_por_dia = valor_por_dia
        else:
            raise ValueError("Valor do automovel por dia não condiz com o tipo desejado")
        
        if isinstance(status, str):
            self.__status = status
        else:
        
            raise ValueError("Status não condiz com o tipo desejado")
        
    @property
    def placa(self):
        return self.__placa
        
    @placa.setter
    def placa(self, placa: str) -> None:
        if isinstance(placa, str):
            self.__placa = placa
        else:
            raise ValueError("Placa não condiz com o tipo desejado")

    @property
    def modelo(self):
        return self.__modelo
               
    @modelo.setter  
    def modelo(self, modelo: str) -> None:   
        if isinstance(modelo, str):
            self.__modelo = modelo
        else:
            raise ValueError("Modelo não condiz com o tipo desejado")

    @property
    def marca(self):
        return self.__marca
        
    @marca.setter
    def marca(self, marca: str) -> None:
        if isinstance(marca, str):
            self.__marca = marca
        else:
            raise ValueError("Marca não condiz com o tipo desejado")

    @property
    def ano(self):
        return self.__ano
        
    @ano.setter
    def ano(self, ano) -> None:
        if isinstance(ano, int):
            self.__ano = ano
        else:
            raise ValueError("Ano não condiz com o tipo desejado")
        
    @property
    def valor_por_dia(self):
        return self.__valor_por_dia
        
    @valor_por_dia.setter
    def valor_por_dia(self, valor_por_dia: float) -> None:
        if isinstance(valor_por_dia, float):
            self.__valor_por_dia = valor_por_dia
        else:
            raise ValueError("Valor do automovel por dia não condiz com o tipo desejado")
        
    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, status: str) -> None:
        if isinstance(status, str):
            self.__status = status
        else:
            raise ValueError("Status não condiz com o tipo desejado")