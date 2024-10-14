from datetime import date

class Cnh():
    def __init__(self, numero: int, categoria: str, vencimento: date):
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise ValueError("Não condiz com o tipo desejado")

        if isinstance(categoria, str):
            self.__categoria = categoria
        else:
            raise ValueError("Não condiz com o tipo desejado")

        if isinstance(vencimento, date):
            self.__vencimento = vencimento
        else:
            raise ValueError("Não condiz com o tipo desejado")

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero: int) -> None:
        if isinstance(numero, int):
            self.__numero = numero
        else:
            raise ValueError("Não condiz com o tipo desejado")

    @property
    def categoria(self): 
        return self.__categoria
        
    @categoria.setter
    def categoria(self, categoria: str) -> None:
        if isinstance(categoria, str):
            self.__categoria = categoria
        else: 
            raise ValueError("Não condiz com o tipo desejado")

    @property
    def vencimento(self):
        return self.__vencimento
        
    @vencimento.setter
    def vencimento(self, vencimento: date) -> None:
        if isinstance(vencimento, date):
            self.__vencimento = vencimento
        else:
            raise ValueError("Não condiz com o tipo desejado")

        
