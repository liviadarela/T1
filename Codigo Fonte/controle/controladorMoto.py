from entidades.moto import Moto
from limite.telaMoto import TelaMoto
from controle.controladorAutomovel import ControladorAutomovel
from exception.dadosInvalidosException import DadosInvalidoException
from daos.motoDAO import MotoDAO


class ControladorMoto(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__()
        self.__moto_dao = MotoDAO()  # instanciando o DAO para gerenciar a persistência
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
                if ano < 1800 or ano > 2026:
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

                self.__moto_dao.add(placa, moto)  # Salvando a moto no DAO
                self.__tela_moto.mostra_mensagem("Sucesso", "Moto incluída!")
                break
        except DadosInvalidoException as e:
            self.__tela_moto.mostra_mensagem("Erro", e)


    def excluir_automovel(self):
        placa_automovel = self.__tela_moto.seleciona_automovel()
        moto_encontrada = self.pega_moto_placa(placa_automovel)
        
        if moto_encontrada:
            self.__moto_dao.excluir(moto_encontrada)  # Excluindo a moto através do DAO
            self.__tela_moto.mostra_mensagem("Sucesso", "Moto excluída!")
        else:
            self.__tela_moto.mostra_mensagem("Aviso", "Moto não encontrada.")

        motos = self.__moto_dao.buscar_todos()  # Buscando todas as motos do DAO
        if not motos:
            self.__tela_moto.mostra_mensagem("Aviso", "Frota de motos está vazia.")
        else:
            self.__tela_moto.listar_motos(motos)  # Listando as motos através da tela

    def listar(self):
        motos = self.__moto_dao.get_all()  # Buscando todas as motos do DAO
        if not motos:
            self.__tela_moto.mostra_mensagem("Aviso", "Frota de motos está vazia.")
        else:
            self.__tela_moto.listar_motos(motos)  # Listando as motos através da tela

    
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
        motos = self.__moto_dao.get_all()  # Buscando todas as motos do DAO
        for moto in motos:
            if moto.placa == placa:
                return moto
        return None
