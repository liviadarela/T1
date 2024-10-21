from datetime import date

class Cnh():
    def __init__(self, numero, categoria, validade):
        if not isinstance(numero, str) or not isinstance(categoria, str) or not isinstance(validade, date):
            raise ValueError("Não condiz com o tipo desejado")
        self.__numero = numero
        self.__categoria = categoria
        self.__validade = validade

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
    def validade(self):
        return self.__validade
        
    @validade.setter
    def validade(self, validade: date) -> None:
        if isinstance(validade, date):
            self.__validade = validade
        else:
            raise ValueError("Não condiz com o tipo desejado")

        