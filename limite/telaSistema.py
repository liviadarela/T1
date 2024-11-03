
class TelaSistema():
    def tela_opcoes(self):
        # exibi as opções principais do sistema
        print("\n-------- SISTEMA ALUGUEL DE AUTOMÓVEIS ---------")
        print("\nEscolha sua opção:")
        print("1 - Automoveis")
        print("2 - Clientes")
        print("3 - Alugueis")
        print("0 - Encerrar sistema")

        #pega a escolha do usuário e converte para inteiro
        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao # retorna a opção escolhida para uso posterior

    def tela_opcoes_automovel(self):
        # metodo para exibir as opções específicas de automóveis
        print("\n-------- OPÇÕES AUTOMÓVEIS ---------")
        print("\nEscolha a opção:")
        print("1 - Gerenciar Frota de Carros")
        print("2 - Gerenciar Frota de Moto")
        print("3 - Gerenciar Frota de Caminhão")
        print("0 - Retornar")
            
        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao