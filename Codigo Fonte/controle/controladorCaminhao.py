from entidades.caminhao import Caminhao
from limite.telaCaminhao import TelaCaminhao
from controle.controladorAutomovel import ControladorAutomovel
from exception.dadosInvalidosException import DadosInvalidoException

class ControladorCaminhao(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__frota_caminhoes = []
        self.__tela_caminhao = TelaCaminhao()

    def incluir_automovel(self):
        try:
            while True:
                dados_caminhao = self.__tela_caminhao.pega_informacao_automovel()
                if dados_caminhao is None:
                    break

                for campo, valor in dados_caminhao.items():
                    if not valor:  # Verifica se está vazio
                        raise DadosInvalidoException(f"O campo '{campo}' não pode estar vazio.")

                placa = dados_caminhao["placa"]
                if self.pega_caminhao_placa(placa):
                    self.__tela_caminhao.mostra_mensagem("Erro", "Essa placa já está cadastrada no sistema.")
                    break

                numero_de_eixos = int(dados_caminhao["numero_de_eixos"])
                if numero_de_eixos <= 0:
                    raise DadosInvalidoException("Número de eixos deve ser um numero inteiro, maior que zero.")
                
                ano = dados_caminhao["ano"]
                if ano < 1800 or ano > 2026:
                    raise DadosInvalidoException("Ano inválido.")

                caminhao = Caminhao(
                    placa=placa,
                    modelo=dados_caminhao["modelo"],
                    marca=dados_caminhao["marca"],
                    ano=int(dados_caminhao["ano"]),
                    valor_por_dia=float(dados_caminhao["valor_por_dia"]),
                    numero_de_eixos=numero_de_eixos
                )

                self.__frota_caminhoes.append(caminhao)
                self.__tela_caminhao.mostra_mensagem("Sucesso", "Caminhão incluído!")
                break
        except DadosInvalidoException as e:
            self.__tela_caminhao.mostra_mensagem("Erro", e)

    def excluir_automovel(self):
        placa_automovel = self.__tela_caminhao.seleciona_automovel()
        automovel_encontrado = False

        for automovel in self.__frota_caminhoes:
            if automovel.placa == placa_automovel:
                self.__frota_caminhoes.remove(automovel)
                self.__tela_caminhao.mostra_mensagem("Sucesso", "Caminhão excluído!")
                automovel_encontrado = True
                break

        if not automovel_encontrado:
            self.__tela_caminhao.mostra_mensagem("Aviso", "Caminhão não encontrado.")

    def listar(self):
        if not self.__frota_caminhoes:
            self.__tela_caminhao.mostra_mensagem("Aviso", "Frota de caminhões está vazia.")
        else:
            self.__tela_caminhao.listar_caminhoes(self.__frota_caminhoes)

    def retornar(self):
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

    def pega_caminhao_placa(self, placa: str):
        for caminhao in self.__frota_caminhoes:
            if caminhao.placa == placa:
                return caminhao
        return None
