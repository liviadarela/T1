class ControladorAutomoveis:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__controlador_carros = ControladorCarro(controlador_sistema)
        self.__controlador_motos = ControladorMoto(controlador_sistema)
        self.__controlador_caminhoes = ControladorCaminhao(controlador_sistema)

    def abre_tela(self):
        while True:
            print("-------- AUTOMÓVEIS ---------")
            print("Escolha a opção")
            print("1 - Incluir Carro")
            print("2 - Excluir Carro")
            print("3 - Incluir Moto")
            print("4 - Excluir Moto")
            print("5 - Incluir Caminhão")
            print("6 - Excluir Caminhão")
            print("7 - Listar Veículos")
            print("8 - Listar Veículos Disponíveis")
            print("0 - Retornar")

            opcao = int(input("Escolha a opção: "))

            if opcao == 1:
                self.__controlador_carros.incluir_carro()
            elif opcao == 2:
                self.__controlador_carros.excluir_carro()
            elif opcao == 3:
                self.__controlador_motos.incluir_moto()
            elif opcao == 4:
                self.__controlador_motos.excluir_moto()
            elif opcao == 5:
                self.__controlador_caminhoes.incluir_caminhao()
            elif opcao == 6:
                self.__controlador_caminhoes.excluir_caminhao()
            elif opcao == 7:
                self.listar_veiculos()
            elif opcao == 8:
                self.listar_veiculos_disponiveis()
            elif opcao == 0:
                print("Retornando ao menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def listar_veiculos(self):
        print("Lista de todos os veículos:")
        self.__controlador_carros.lista_carros()
        self.__controlador_motos.lista_motos()
        self.__controlador_caminhoes.lista_caminhoes()

    def listar_veiculos_disponiveis(self):
        print("Lista de veículos disponíveis:")
        self.__controlador_carros.lista_carros_disponiveis()
        self.__controlador_motos.lista_motos_disponiveis()
        self.__controlador_caminhoes.lista_caminhoes_disponiveis()
