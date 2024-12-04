from exception.dadosInvalidosException import DadosInvalidoException

class Automovel():
    def __init__(self, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        # inicializando todos os atributos como None
        self.__placa = None
        self.__modelo = None
        self.__marca = None
        self.__ano = None
        self.__valor_por_dia = None

        if isinstance(placa, str):
            self.__placa = placa
        else:
            raise DadosInvalidoException("Placa deve ser uma string.")

        if isinstance(modelo, str):
            self.__modelo = modelo
        else:
            raise DadosInvalidoException("Modelo deve ser uma string.")

        if isinstance(marca, str):
            self.__marca = marca
        else:
            raise DadosInvalidoException("Marca deve ser uma string.")
    
        if isinstance(ano, int):
            self.__ano = ano
        else:
            raise DadosInvalidoException("Ano deve ser um numero inteiro.")
        
        if isinstance(valor_por_dia, float):
            self.__valor_por_dia = valor_por_dia
        else:
            raise DadosInvalidoException("O valor por dia deve ser uma data válida no formato 00/00/0000.")
        
        if isinstance(status, str):
            self.__status = status
        else:
            raise DadosInvalidoException("Status deve ser uma string.")

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa: str) -> None:
        if isinstance(placa, str):
            self.__placa = placa
        else:
            raise DadosInvalidoException("Placa deve ser uma string.")

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter  
    def modelo(self, modelo: str) -> None:   
        if isinstance(modelo, str):
            self.__modelo = modelo
        else:
            raise DadosInvalidoException("Modelo deve ser uma string.")

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca: str) -> None:
        if isinstance(marca, str):
            self.__marca = marca
        else:
            raise DadosInvalidoException("Marca deve ser uma string.")

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano) -> None:
        if isinstance(ano, int):
            self.__ano = ano
        else:
            raise DadosInvalidoException("Ano deve ser um numero inteiro.")

    @property
    def valor_por_dia(self):
        return self.__valor_por_dia

    @valor_por_dia.setter
    def valor_por_dia(self, valor_por_dia: float) -> None:
        if isinstance(valor_por_dia, float):
            self.__valor_por_dia = valor_por_dia
        else:
            raise DadosInvalidoException("O valor por dia deve ser um float.")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str) -> None:
        if isinstance(status, str):
            self.__status = status
        else:
            raise DadosInvalidoException("Status deve ser uma string.")