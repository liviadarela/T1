from entidades.caminhao import Caminhao

class ControladorCaminhao():
    def __init__(self):
          self.frota_caminhoes = []

    def incluir_automovel(self, numero_de_eixos: int, placa: str, modelo: str, marca: str, ano:int, valor_por_dia: float, status="Disponível"):
        for caminhao in self.frota_caminhoes:
            if caminhao.placa == placa:
                print("Não foi possível realizar a inclusar, caminhão ja cadastrada")
                return

        novo_caminhao = Caminhao(numero_de_eixos, placa, modelo, marca, ano, valor_por_dia, status)
        self.frota_caminhoes.append(novo_caminhao)
        return self.frota_caminhoes
 

    def listar_disponiveis(self):
        return self.frota_caminhoes      
