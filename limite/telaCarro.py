from limite.telaAutomovel import TelaAutomovel

class TelaCarro(TelaAutomovel):

    def tela_opcoes(self):
        # Método para exibir as opções específicas para carros
        print("\n--------- OPÇÕES CARROS ---------")
        print("Escolha a opção:")
        print("1 - Cadastrar carro novo")
        print("2 - Excluir carro já cadastrado")
        print("3 - Verificar frota de carros")
        print("0 - Retornar ao menu principal")

        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        # método para coletar informações do carro, incluindo dados comuns e categoria
        dados_comuns = super().pega_infomacao_automovel() # chama o método da superclasse
        categoria = input("Categoria: ")
        dados_comuns["categoria"] = categoria
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        # metodo para exibir os dados do carro, incluindo dados da superclasse
        print("\nCARRO ---------------------")
        super().mostra_automovel(dados_automovel)
        print("Categoria: ", dados_automovel["categoria"])
    
