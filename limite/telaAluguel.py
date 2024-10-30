

class TelaAluguel():
    def tela_opcoes(self):
        print("\n--------- AlUGUEL ---------")
        print("Escolha a opção")
        print("1 - Realizar Aluguel")
        print("2 - Devolução do Aluguel")
        print("3 - Registro de Alugueis")
        print("4 - Resgistro de Alugueis por período")
        print("0 - Retornar ao Menu Principal")

        opcao = int(input("Escolha a opção: "))
        return opcao
     
    def pega_dados_aluguel(self):
        print("\n------ DADOS PARA ALUGUEL ------")
        cliente = input("Cpf do Cliente:")
        automovel = input("Placa do automovel: ")
        data_inicio = input("Digite a Data de Início (dd/mm/aaaa): ")
        data_final= input("Digite a Data de Devolução (dd/mm/aaaa): ")

        return {
            "cliente": cliente,
            "automovel": automovel,
            "data_inicio": data_inicio,
            "data_final": data_final
        }
    
    def intervalo(self):
        print("\n------ ALUGUEIS POR PERÍODO ------")
        data_inicio = input("Digite o Início do intervalo (dd/mm/aaaa): ")
        data_final= input("Digite o Fim do Intervalo (dd/mm/aaaa): ")

        return {
            "data_inicio": data_inicio,
            "data_final": data_final
        }

    def mostra_aluguel(self, dados_aluguel):
        print("\n------ ALUGUEL ------")
        print("------ Dados Cliente ------")
        print("Nome: ", dados_aluguel["nome"])
        print("Cpf: ", dados_aluguel["cpf"])
        print("\n------ Dados Automovel------")
        print("Placa: ", dados_aluguel["placa"])
        print("Data de Início:", dados_aluguel["data_inicio"])
        print("Data De Devolução: ", dados_aluguel["data_final"])
        print("Valor Total: ")

    def seleciona_aluguel(self):
        cpf = input("CPF do cliente que está cadastrado no aluguel: ")
        return cpf