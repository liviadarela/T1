from entidades.carro import Carro
from limite.telaCarro import TelaCarro
from controle.controladorAutomovel import ControladorAutomovel


#classe ControladorCarro realiza operações específicas para o gerenciamento de carros, 
#incluindo métodos para incluir, excluir e listar veículos da frota de carros, tambem 
# fornece uma interface de interação com o usuário através de uma tela específica e 
# permite busca de carros pela placa.

class ControladorCarro(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__() 
        self.__frota_carros = []
        self.__tela_carro = TelaCarro()
 
    def incluir_automovel(self):
        while True:
            try:
                #pega os dados do carro através da tela 
                dados_carro = self.__tela_carro.pega_infomacao_automovel()
                categoria = dados_carro["categoria"]

                if not categoria.isalpha():
                    raise ValueError("\nA categoria deve conter apenas letras.")
                
                #cria uma instância de Carro com os dados fornecidos
                carro = Carro(
                    placa=dados_carro["placa"],
                    modelo=dados_carro["modelo"],
                    marca=dados_carro["marca"],
                    ano=dados_carro["ano"],
                    valor_por_dia=float(dados_carro["valor_por_dia"]),
                    categoria=categoria
                )

                self.__frota_carros.append(carro)
                print("\nCarro incluído com sucesso!")
                break
            except ValueError as e:
                print(f"Erro: {e}")
                print("Por favor, insira os dados novamente.")

    def excluir_automovel(self):
        # metodo para excluir um carro da frota
        placa_automovel = self.__tela_carro.seleciona_automovel()
        automovel_encontrado = False

        # Busca o carro na frota pelo número da placa
        for automovel in self.__frota_carros:
            if automovel.placa == placa_automovel:
                self.__frota_carros.remove(automovel)
                print("\nCarro excluído com sucesso!")
                automovel_encontrado = True

        if not automovel_encontrado:
            print("\nATENÇÃO: Carro não encontrado")

    def listar(self):
        if not self.__frota_carros:
            print("\nFrota de carros está vazia.")
        else:
             # percorre a frota e exibe as informações de cada carro
            print("\n------ FROTA DE CARROS ------")
            for carro in self.__frota_carros:
                self.__tela_carro.mostra_automovel({
                    "placa": carro.placa,
                    "modelo": carro.modelo,
                    "marca": carro.marca,
                    "ano": carro.ano,
                    "valor_por_dia": carro.valor_por_dia,
                    "categoria": carro.categoria,
                    "status": carro.status
                })
    
    def retornar(self):
        print("\nRetornando ao menu principal...")
        return 
    
    def abre_tela(self):
        # metodo para abrir a tela de opções para o usuário
        lista_opcoes = {
            1: self.incluir_automovel,
            2: self.excluir_automovel,
            3: self.listar,
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
                print("\nOpção inválida. Tente novamente!")

    def pega_carro_placa(self, placa:str):
        for carro in self.__frota_carros:
            if carro.placa == placa:
                return carro
        return None