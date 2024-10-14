from entidades.automovel import Automovel

class Carro(Automovel):
    def __init__(self, categoria: str, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        super().__init__(placa, modelo, marca, ano, valor_por_dia, status)
        if isinstance(categoria, str):
            self.__categoria = categoria
        self.frota_carros = []

    @property
    def categoria(self):
        return self.__categoria 
    
    @categoria.setter
    def categoria(self, categoria: str):
        if isinstance(categoria, str):
            self.__categoria = categoria 

    