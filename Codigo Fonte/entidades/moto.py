from entidades.automovel import Automovel

class Moto(Automovel):
    def __init__(self, seguro_adicional: float, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        super().__init__(placa, modelo, marca, ano, valor_por_dia, status)
        self.__seguro_adicional = None
        if isinstance(seguro_adicional, float):
            self.__seguro_adicional = seguro_adicional
        else:
            raise ValueError("\nSeguro adicional não condiz com o tipo desejado")
    
    @property
    def seguro_adicional(self):
        return self.__seguro_adicional 
    
    @seguro_adicional.setter
    def seguro_adicional(self, seguro_adicional: float):
        if isinstance(seguro_adicional, float):
            self.__seguro_adicional = seguro_adicional 
        else:
            raise ValueError("\nSeguro adicional não condiz com o tipo desejado")
    
    