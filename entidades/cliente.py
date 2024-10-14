from datetime import date
from entidades.cnh import Cnh 

class Cliente:
    def __init__(self, nome: str, cpf: int, data_nascimento: date, endereco: str, cnh: Cnh):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser uma string")

        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            raise ValueError("CPF deve ser um número inteiro")

        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento
        else:
            raise ValueError("Data de nascimento deve ser uma data válida")

        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            raise ValueError("Endereço deve ser uma string")

        if isinstance(cnh, Cnh):
            self.__cnh = cnh
        else:
            raise ValueError("CNH deve ser uma instância da classe Cnh")
    
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser uma string")

    @property
    def cpf(self) -> int:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int) -> None:
        if isinstance(cpf, int):
            self.__cpf = cpf
        else:
            raise ValueError("CPF deve ser um número inteiro")

    @property
    def data_nascimento(self) -> date:
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date) -> None:
        if isinstance(data_nascimento, date):
            self.__data_nascimento = data_nascimento
        else:
            raise ValueError("Data de nascimento deve ser uma data válida")

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str) -> None:
        if isinstance(endereco, str):
            self.__endereco = endereco
        else:
            raise ValueError("Endereço deve ser uma string")

    @property
    def cnh(self) -> Cnh:
        return self.__cnh

    @cnh.setter
    def cnh(self, cnh: Cnh) -> None:
        if isinstance(cnh, Cnh):
            self.__cnh = cnh
        else:
            raise ValueError("CNH deve ser uma instância da classe Cnh")
