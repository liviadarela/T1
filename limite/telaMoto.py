from limite.telaAutomovel import TelaAutomovel

class TelaMoto(TelaAutomovel):

    def tela_opcoes(self):
        print("\n--------- MOTOS ---------")
        print("Escolha a opção")
        print("1 - Cadastrar Moto Nova")
        print("2 - Excluir Moto já Cadastrada")
        print("3 - Verificar Frota de Motos")
        print("0 - Retornar ao menu principal")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pega_infomacao_automovel(self):
        dados_comuns = super().pega_infomacao_automovel()
        seguro_adicional = input("Seguro Adicional: ")
        dados_comuns["seguro_adicional"] = seguro_adicional
        return dados_comuns
    
    def mostra_automovel(self, dados_automovel):
        print("\n--------- MOTO ---------")
        super().mostra_automovel(dados_automovel)
        print("Seguro adicional: ", dados_automovel["seguro_adicional"])
    
