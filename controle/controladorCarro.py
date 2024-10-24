from entidades.carro import Carro
from limite.telaCarro import TelaCarro
from controle.controladorAutomovel import ControladorAutomovel
class ControladorCarro(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__() 
        self.__frota_carros = []
        self.__tela_carro = TelaCarro()

    def incluir_automovel(self):
        super().incluir_automovel()

        while True:
            try:
                dados_carro = self.__tela_carro.pega_infomacao_automovel()
                categoria = dados_carro["categoria"]

                if not categoria.isalpha():
                    raise ValueError("A categoria deve conter apenas letras.")
                
                carro = Carro(
                    placa=dados_carro["placa"],
                    modelo=dados_carro["modelo"],
                    marca=dados_carro["marca"],
                    ano=int(dados_carro["ano"]),
                    valor_por_dia=float(dados_carro["valor_por_dia"]),
                    categoria=categoria
                )

                #self._ControladorAutomoveis__frota.append(carro)
                self.__frota_carros.append(carro)
                print("Carro incluído com sucesso!")
                break
            except ValueError as e:
                print(f"Erro: {e}")
                print("Por favor, insira os dados novamente.\n")

    def excluir_automovel(self):
        super().excluir_automovel()
        
    def listar_disponiveis(self):
        return self.__frota_carros
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_automovel,
            2: self.excluir_automovel,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_carro.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:  
                    break
            else:
                print("Opção inválida. Tente novamente.")
    