from limite.telaAutomovel import TelaAutomovel

class TelaMoto(TelaAutomovel):

    def tela_opcoes(self):
        print("\n---------OPÇÕES MOTOS ---------")
        print("Escolha a opção:")
        print("1 - Cadastrar moto nova")
        print("2 - Excluir moto já cadastrada")
        print("3 - Verificar frota de motos")
        print("0 - Retornar ao menu principal")

        opcao = int(input("\nEscolha a opcão que deseja utilizar: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        seguro_adicional = input("Seguro Adicional: ")
        dados_comuns["seguro_adicional"] = seguro_adicional
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\nMOTO ----------------------")
        super().mostra_automovel(dados_automovel)
        print("Seguro adicional: ", dados_automovel["seguro_adicional"])

