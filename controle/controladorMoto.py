from entidades.moto import Moto

class ControladorMoto():
    def __init__(self):
          self.frota_motos = []

    def incluir_automovel(self, seguro_adicional: float, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        for moto in self.frota_motos:
            if moto.placa == placa:
                print("Não foi possível realizar a inclusar, moto ja cadastrada")
                return

        nova_moto = Moto(seguro_adicional, placa, modelo, marca, ano, valor_por_dia, status)
        self.frota_motos.append(nova_moto)
        return self.frota_motos

    def listar_disponiveis(self):
        return self.frota_motos
                