from datetime import date

class Cnh():
    def __init__(self, numero, categoria, validade):
        # inicializando todos os atributos como None
        self.__numero = None
        self.__categoria = None
        self.__validade = None

        if isinstance(numero, str):
            self.__numero = numero
        else:
            raise ValueError("Numero da CNH não condiz com o tipo desejado")
        
        if isinstance(categoria, str):
            self.__categoria = categoria
        else:
            raise ValueError("Categoria não condiz com o tipo desejado")
        
        if isinstance(validade, date):
            self.__validade = validade
        else:
            raise ValueError("Data de validade não condiz com o tipo desejado")

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise ValueError("Numero da CNH não condiz com o tipo desejado")

    @property
    def categoria(self): 
        return self.__categoria
        
    @categoria.setter
    def categoria(self, categoria: str) -> None:
        if isinstance(categoria, str):
            self.__categoria = categoria
        else: 
            raise ValueError("Categoria não condiz com o tipo desejado")

    @property
    def validade(self):
        return self.__validade
        
    @validade.setter
    def validade(self, validade: date) -> None:
        if isinstance(validade, date):
            self.__validade = validade
        else:
            raise ValueError("Validade não condiz com o tipo desejado")

        