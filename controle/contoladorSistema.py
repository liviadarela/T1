from limite.telaSistema import TelaSistema
from controle.controladorCliente import ControladorCliente
from controle.controladorAluguel import ControladorAluguel
from controle.controladorCarro import ControladorCarro
from controle.controladorMoto import ControladorMoto
from controle.controladorCaminhao import ControladorCaminhao


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clientes = ControladorCliente(self)
        #self.__controlador_carros = ControladorCarro(self)
        #self.__controlador_motos = ControladorMoto(self)
        #self.__controlador_alugueis = ControladorAluguel(self)
        #self.__controlador_caminhoes = ControladorCaminhao(self)

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes
        
    #@property
    #def controlador_carros(self):
        #return self.__controlador_carros

    #@property
    #def controlador_motos(self):
       # return self.__controlador_motos

   # @property
   # def controlador_alugueis(self):
        #return self.__controlador_alugueis

    #@property
    #def controlador_caminhoes(self):
       # return self.__controlador_caminhoes

    def inicia_sistema(self):
        self.abre_tela() 

    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            if opcao == 1:
                self.__controlador_automoveis.abre_tela()
            elif opcao == 2:
                self.controlador_clientes.abre_tela()
            elif opcao == 3:
                self.controlador_alugueis.abre_tela()
            elif opcao == 0:
                print("Sistema encerrado")
                break
            else:
                print("Opção inválida, tente novamente")
        return