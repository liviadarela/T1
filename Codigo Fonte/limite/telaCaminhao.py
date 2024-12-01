from limite.telaAutomovel import TelaAutomovel

class TelaCaminhao(TelaAutomovel):

    def tela_opcoes(self):
        print("\n--------- OPÇÕES CAMINHÕES ---------")
        print("\nEscolha a opção:")
        print("1 - Cadastrar caminhão novo")
        print("2 - Excluir caminhão já cadastrado")
        print("3 - Verificar frota de caminhões")
        print("0 - Retornar ao menu principal")

        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        numero_de_eixos = input("Numero de Eixos: ")
        dados_comuns["numero_de_eixos"] = numero_de_eixos
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\nCAMINHÃO ------------------")
        super().mostra_automovel(dados_automovel)
        print("Numero de Eixos: ", dados_automovel["numero_de_eixos"])
    
