from entidades.carro import Carro

class ControladorCarro():
    def __init__(self):
        self.frota_carros = []

    def incluir_automovel(self, categoria: str, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        for carro in self.frota_carros:
            if carro.placa == placa:
                print("Não foi possível realizar a inclusar, carro ja cadastrada")
                return

        novo_carro = Carro(categoria, placa, modelo, marca, ano, valor_por_dia, status)
        self.frota_carros.append(novo_carro)
        return self.frota_carros

    def listar_disponiveis(self):
        return self.frota_carros