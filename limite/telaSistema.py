
class TelaSistema():
    def tela_opcoes(self):
        print("-------- Sistema Aluguel de Automoveis ---------")
        print("Escolha sua opção")
        print("1 - Automoveis")
        print("2 - Clientes")
        print("3 - Alugueis")
        print("0 - Encerrar sistema")
        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao

    def tela_opcoes_automovel(self):
        print("\n-------- AUTOMÓVEIS ---------")
        print("Escolha a opção")
        print("1 - Gerenciar Frota de Carros")
        print("2 - Gerenciar Frota de Moto")
        print("3 - Gerenciar Frota de Caminhão")
        print("0 - Retornar")
            
        opcao = int(input("Escolha a opção: "))
        return opcao