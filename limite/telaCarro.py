from limite.telaAutomovel import TelaAutomovel

class TelaCarro(TelaAutomovel):

    def tela_opcoes(self):
        print("\n--------- Carros ---------")
        print("Escolha a opção")
        print("1 - Cadastrar Carro novo")
        print("2 - Excluir Carro já cadastrado")
        print("3 - Verificar frota de carros")
        print("0 - Retornar")

        
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        categoria = input("Categoria: ")
        dados_comuns["categoria"] = categoria
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\n--------- Carros ---------")
        super().mostra_automovel(dados_automovel)
        print("Categoria: ", dados_automovel["categoria"])
    
