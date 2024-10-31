from limite.telaAutomovel import TelaAutomovel

class TelaCarro(TelaAutomovel):

    def tela_opcoes(self):
        print("\n--------- OPÇÕES CARROS ---------")
        print("Escolha a opção:")
        print("1 - Cadastrar carro novo")
        print("2 - Excluir carro já cadastrado")
        print("3 - Verificar frota de carros")
        print("0 - Retornar ao menu principal")

        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        categoria = input("Categoria: ")
        dados_comuns["categoria"] = categoria
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\nCARRO ---------------------")
        super().mostra_automovel(dados_automovel)
        print("Categoria: ", dados_automovel["categoria"])
    
