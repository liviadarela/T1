
class TelaAutomoveis:
    def tela_opcoes(self):
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
        return opcao
