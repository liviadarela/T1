from entidades.caminhao import Caminhao
from limite.telaCaminhao import TelaCaminhao
from controle.controladorAutomovel import ControladorAutomovel

class ControladorCaminhao(ControladorAutomovel):
    def __init__(self):
        super().__init__() 
        self.__frota_caminhoes = []
        self.__tela_caminhao = TelaCaminhao()
 
    def incluir_automovel(self):
        while True:
            try:
                dados_caminhao = self.__tela_caminhao.pega_infomacao_automovel()
                numero_de_eixos = dados_caminhao["numero_de_eixos"]

                if not numero_de_eixos.isdigit():   
                    raise ValueError("O numero de eixos deve ser um numero inteiro.")
                
                caminhao = Caminhao(
                    placa = dados_caminhao["placa"],
                    modelo = dados_caminhao["modelo"],
                    marca = dados_caminhao["marca"],
                    ano = int(dados_caminhao["ano"]),
                    valor_por_dia = float(dados_caminhao["valor_por_dia"]),
                    numero_de_eixos = int(numero_de_eixos)
                )

                self.__frota_caminhoes.append(caminhao)
                print("Caminhai incluído com sucesso!")
                break
            except ValueError as e:
                print(f"Erro: {e}")
                print("Por favor, insira os dados novamente.\n")

    def excluir_automovel(self):
        placa_automovel = self.__tela_caminhao.seleciona_automovel()
        automovel_encontrado = False

        for automovel in self.__frota_caminhoes:
            if automovel.placa == placa_automovel:
                self.__frota_caminhoes.remove(automovel)
                print("Caminhao excluído com sucesso!")
                automovel_encontrado = True

        if not automovel_encontrado:
            print("ATENÇÃO: Caminhao não encontrado")

    def listar(self):
        if not self.__frota_caminhoes:
            print("Frota de caminhões está vazia.")
        else:
            for caminhao in self.__frota_caminhoes:
                self.__tela_caminhao.mostra_automovel({
                    "placa": caminhao.placa,
                    "modelo": caminhao.modelo,
                    "marca": caminhao.marca,
                    "ano": caminhao.ano,
                    "valor_por_dia": caminhao.valor_por_dia,
                    "numero_de_eixos": caminhao.numero_de_eixos,
                    "statur": caminhao.status
                })
    
    def retornar(self):
        print("Retornando ao menu principal...")
        return 
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_automovel,
            2: self.excluir_automovel,
            3: self.listar,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_caminhao.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0: 
                    break

            else:
                print("Opção inválida. Tente novamente.")

    def pega_caminhao_placa(self, placa:str):
        for caminhao in self.__frota_caminhoes:
            if caminhao.placa == placa:
                return caminhao
        return None