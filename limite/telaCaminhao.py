from limite.telaAutomovel import TelaAutomovel

class TelaCaminhao(TelaAutomovel):

    def tela_opcoes(self):
        print("\n--------- CAMINHÕES ---------")
        print("Escolha a opção")
        print("1 - Cadastrar Caminhão Novo")
        print("2 - Excluir Caminhãojá Cdastrado")
        print("3 - Verificar Frota de Caminhões")
        print("0 - Retornar ao menu principal")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        numero_de_eixos = input("Numero de Eixos: ")
        dados_comuns["numero_de_eixos"] = numero_de_eixos
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\n--------- CAMINHÃO ---------")
        super().mostra_automovel(dados_automovel)
        print("Numero de Eixos: ", dados_automovel["numero_de_eixos"])
    
