from entidades.moto import Moto
from limite.telaMoto import TelaMoto
from controle.controladorAutomovel import ControladorAutomovel

class ControladorMoto(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__() 
        self.__frota_motos = []
        self.__tela_moto = TelaMoto()
 
    def incluir_automovel(self):
        while True:
            dados_moto = self.__tela_moto.pega_infomacao_automovel()
            seguro_adicional = dados_moto["seguro_adicional"]

            moto = Moto(
                placa=dados_moto["placa"],
                modelo=dados_moto["modelo"],
                marca=dados_moto["marca"],
                ano=int(dados_moto["ano"]),
                valor_por_dia=float(dados_moto["valor_por_dia"]),
                seguro_adicional=float(seguro_adicional)
            )

            self.__frota_motos.append(moto)
            print("\nMoto incluída com sucesso!")
            break

    def excluir_automovel(self):
        placa_automovel = self.__tela_moto.seleciona_automovel()
        automovel_encontrado = False

        for automovel in self.__frota_motos:
            if automovel.placa == placa_automovel:
                self.__frota_motos.remove(automovel)
                print("\nMoto excluída com sucesso!")
                automovel_encontrado = True

        if not automovel_encontrado:
            print("\nATENÇÃO: Moto não encontrada")

    def listar(self):
        if not self.__frota_motos:
            print("\nFrota de motos está vazia.")
        else:
            print("\n------ FROTA DE MOTOS ------")
            for moto in self.__frota_motos:
                self.__tela_moto.mostra_automovel({
                    "placa": moto.placa,
                    "modelo": moto.modelo,
                    "marca": moto.marca,
                    "ano": moto.ano,
                    "valor_por_dia": moto.valor_por_dia,
                    "seguro_adicional": moto.seguro_adicional,
                    "status": moto.status
                })
    
    def retornar(self):
        print("\nRetornando ao menu principal...")
        return 
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_automovel,
            2: self.excluir_automovel,
            3: self.listar,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_moto.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0: 
                    break

            else:
                print("\nOpção inválida. Tente novamente!")

    def pega_moto_placa(self, placa:str):
        for moto in self.__frota_motos:
            if moto.placa == placa:
                return moto
        return None