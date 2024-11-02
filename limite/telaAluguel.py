
class TelaAluguel():
    def tela_opcoes(self):
        print("\n--------- OPÇÕES AlUGUEIS ---------")
        print("Escolha a opção")
        print("1 - Realizar Aluguel")
        print("2 - Devolução do Aluguel")
        print("3 - Registro de Alugueis")
        print("4 - Resgistro de Alugueis por período")
        print("5 - Alterar Aluguel cadastrado")
        print("0 - Retornar ao Menu Principal")

        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao
     
    def pega_dados_aluguel(self):
        print("\n------ DADOS PARA ALUGUEL ------")
        cliente = input("CPF do cliente:")
        automovel = input("Placa do automovel: ")
        data_inicio = input("Digite a data de início (dd/mm/aaaa): ")
        data_final= input("Digite a data de devolução (dd/mm/aaaa): ")

        return {
            "cliente": cliente,
            "automovel": automovel,
            "data_inicio": data_inicio,
            "data_final": data_final
        }
    
    def intervalo(self):
        print("\n------ ALUGUEIS POR PERÍODO ------")
        data_inicio = input("Digite o início do intervalo (dd/mm/aaaa): ")
        data_final= input("Digite o fim do intervalo (dd/mm/aaaa): ")

        return {
            "data_inicio": data_inicio,
            "data_final": data_final
        }

    def mostra_aluguel(self, dados_aluguel):
        print("\n------ ALUGUEL ------")
        print("DADOS CLIENTE -----------")
        print("Nome: ", dados_aluguel["nome"])
        print("CPF: ", dados_aluguel["cpf"])
        print("\nDADOS VEÍCULO -----------")
        print("Placa: ", dados_aluguel["placa"])
        print("Data de Início:", dados_aluguel["data_inicio"])
        print("Data De Devolução: ", dados_aluguel["data_final"])
        print("Valor Pago: ", dados_aluguel["valor_total"] )

    def seleciona_aluguel(self):
        cpf = input("\nDigite o CPF do cliente cadastrado no aluguel: ")
        return cpf