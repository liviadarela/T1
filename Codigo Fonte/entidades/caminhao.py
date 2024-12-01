from entidades.automovel import Automovel

# As classes Moto e carro se comportam da mesma maneira mudando apenas o atributo diferente 
class Caminhao(Automovel): # classe Caminhao herda da classe 'Automovel
    def __init__(self, numero_de_eixos: int, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        # chama o construtor da classe pai (Automovel) com os parâmetros necessários
        super().__init__(placa, modelo, marca, ano, valor_por_dia, status)
        self.__numero_de_eixos = None
        
        if isinstance(numero_de_eixos, int):
            self.__numero_de_eixos = numero_de_eixos
        else: 
            raise ValueError("Numero de eixos não condiz com o tipo desejado")

    @property
    def numero_de_eixos(self):
        return self.__numero_de_eixos 
    
    @numero_de_eixos.setter
    def numero_de_eixosl(self, numero_de_eixos: int):
        if isinstance(numero_de_eixos, int):
            self.__numero_de_eixos = numero_de_eixos
        else: 
            raise ValueError("Numero de eixos não condiz com o tipo desejado")
    