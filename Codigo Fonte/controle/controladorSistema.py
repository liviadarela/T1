from limite.telaSistema import TelaSistema
from controle.controladorCliente import ControladorCliente
from controle.controladorCarro import ControladorCarro
from controle.controladorMoto import ControladorMoto
from controle.controladorCaminhao import ControladorCaminhao
from controle.controladorAluguel import ControladorAluguel

class ControladorSistema:
    def __init__(self):
        # inicializa a tela do sistema e os controladores para diferentes entidades
        self.__tela_sistema = TelaSistema()
        self.__controlador_cliente = ControladorCliente(self)
        self.__controlador_carros = ControladorCarro(self)
        self.__controlador_motos = ControladorMoto(self)
        self.__controlador_caminhoes = ControladorCaminhao(self)
        self.__controlador_alugueis = ControladorAluguel(self)

    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
  
    @property
    def controlador_carros(self):
        return self.__controlador_carros
    
    @property
    def controlador_motos(self):
        return self.__controlador_motos

    @property
    def controlador_caminhoes(self):
        return self.__controlador_caminhoes
    
    @property
    def controlador_alugueis(self):
        return self.__controlador_alugueis

    def inicia_sistema(self):
        # inicia o sistema, e chama a tela principal
        self.abre_tela() 

    def abre_tela(self):

        # metodo para abrir a tela do sistema e gerenciar as opções
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            if opcao == 1:
                opcao = self.__tela_sistema.tela_opcoes_automovel()
                if opcao == 1:
                    self.__controlador_carros.abre_tela()
                elif opcao == 2:
                    self.__controlador_motos.abre_tela()
                elif opcao == 3:
                    self.__controlador_caminhoes.abre_tela()
                elif opcao == 0:
                    continue
            elif opcao == 2:
                self.__controlador_cliente.abre_tela()
            elif opcao == 3:
                self.__controlador_alugueis.abre_tela()
            elif opcao == 0:
                self.__tela_sistema.mostra_mensagem("Encerrando", "Sistema encerrado")
                break
            