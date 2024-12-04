from entidades.moto import Moto
from limite.telaMoto import TelaMoto
from controle.controladorAutomovel import ControladorAutomovel
from exception.dadosInvalidosException import DadosInvalidoException

class ControladorMoto(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__frota_motos = []
        self.__tela_moto = TelaMoto()

    def incluir_automovel(self):
        try:
            while True:
                dados_moto = self.__tela_moto.pega_informacao_automovel()
                if dados_moto is None:
                    break

                for campo, valor in dados_moto.items():
                    if not valor:  # Verifica se está vazio
                        raise DadosInvalidoException(f"O campo '{campo}' não pode estar vazio.")
                    
                placa = dados_moto["placa"]
                if self.pega_moto_placa(placa):
                    self.__tela_moto.mostra_mensagem("Erro", "Essa placa já está cadastrada no sistema.")
                    break

                seguro_adicional = float(dados_moto["seguro_adicional"])
                if seguro_adicional < 0:
                    raise DadosInvalidoException("Seguro adicional deve ser um valor positivo.")
                
                ano = int(dados_moto["ano"])
                if ano < 1800 or ano >2026:
                    raise DadosInvalidoException("Ano inválido.")
                
                valor_por_dia = float(dados_moto["valor_por_dia"])
                if valor_por_dia < 0:
                    raise DadosInvalidoException("Valor por dia deve ser um valor positivo.")

                moto = Moto(
                    placa=placa,
                    modelo=dados_moto["modelo"],
                    marca=dados_moto["marca"],
                    ano=int(dados_moto["ano"]),
                    valor_por_dia=float(dados_moto["valor_por_dia"]),
                    seguro_adicional=seguro_adicional
                )

                self.__frota_motos.append(moto)
                self.__tela_moto.mostra_mensagem("Sucesso", "Moto incluída!")
                break
        except DadosInvalidoException as e:
            self.__tela_moto.mostra_mensagem("Erro", e)

    def excluir_automovel(self):
        placa_automovel = self.__tela_moto.seleciona_automovel()
        automovel_encontrado = False

        for automovel in self.__frota_motos:
            if automovel.placa == placa_automovel:
                self.__frota_motos.remove(automovel)
                self.__tela_moto.mostra_mensagem("Sucesso", "Moto excluída!")
                automovel_encontrado = True
                break

        if not automovel_encontrado:
            self.__tela_moto.mostra_mensagem("Aviso", "Moto não encontrada.")

    def listar(self):
        if not self.__frota_motos:
            self.__tela_moto.mostra_mensagem("Aviso", "Frota de motos está vazia.")
        else:
            self.__tela_moto.listar_motos(self.__frota_motos)

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
            opcao = self.__tela_moto.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:
                    break

    def pega_moto_placa(self, placa: str):
        for moto in self.__frota_motos:
            if moto.placa == placa:
                return moto
        return None
