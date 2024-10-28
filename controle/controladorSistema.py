from limite.telaSistema import TelaSistema
from controle.controladorCliente import ControladorCliente
from controle.controladorCarro import ControladorCarro
from limite.telaCarro import TelaCarro

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_clientes = ControladorCliente(self)
        self.__controlador_carros = ControladorCarro(self)
        self.__tela_carro = TelaCarro()

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes
  
    @property
    def controlador_carros(self):
        return self.__controlador_carros

    def inicia_sistema(self):
        self.abre_tela() 

    def abre_tela(self):
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
                else:
                    print("Opção inválida, tente novamente")
                continue  # Isso garante que o loop vol
            elif opcao == 2:
                self.__controlador_clientes.abre_tela()
            elif opcao == 3:
                self.__controlador_alugueis.abre_tela()
            elif opcao == 0:
                print("Sistema encerrado")
                break
            else:
                print("Opção inválida, tente novamente")