from entidades.automovel import Automovel
import PySimpleGUI as sg

class Carro(Automovel):
    def __init__(self, categoria: str, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        super().__init__(placa, modelo, marca, ano, valor_por_dia, status)
        self.__categoria = None

        if isinstance(categoria, str):
            self.__categoria = categoria
        else:
            sg.popup_error("Categoria não condiz com o tipo desejado")

    @property
    def categoria(self):
        return self.__categoria 
    
    @categoria.setter
    def categoria(self, categoria: str):
        if isinstance(categoria, str):
            self.__categoria = categoria 
        else:
            sg.popup_error("Categoria não condiz com o tipo desejado")

    