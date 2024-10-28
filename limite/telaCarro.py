from limite.telaAutomovel import TelaAutomovel

class TelaCarro(TelaAutomovel):

    def tela_opcoes(self):
        print("\n--------- CARROS ---------")
        print("Escolha a opção")
        print("1 - Cadastrar Carro Novo")
        print("2 - Excluir Carro já cCdastrado")
        print("3 - Verificar Frota de Carros")
        print("0 - Retornar ao menu principal")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        categoria = input("Categoria: ")
        dados_comuns["categoria"] = categoria
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\n--------- CARRO ---------")
        super().mostra_automovel(dados_automovel)
        print("Categoria: ", dados_automovel["categoria"])
    
