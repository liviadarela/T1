import PySimpleGUI as sg
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
                dados_carro = self.__tela_carro.pega_informacao_automovel()
                categoria = dados_carro["categoria"]

                if not categoria.isalpha():
                    sg.popup_error("\nA categoria deve conter apenas letras.")
                    return
                
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
                sg.popup("Carro incluído com sucesso!.")

                break
            except ValueError as e:
                sg.popup(f"Erro: {e}")
                sg.popup("Por favor, insira os dados novamente.")

    def excluir_automovel(self):
        # metodo para excluir um carro da frota
        placa_automovel = self.__tela_carro.seleciona_automovel()
        automovel_encontrado = False

        # Busca o carro na frota pelo número da placa
        for automovel in self.__frota_carros:
            if automovel.placa == placa_automovel:
                self.__frota_carros.remove(automovel)
                sg.popup("\nCarro excluído com sucesso!")
                automovel_encontrado = True
                break

        if not automovel_encontrado:
            sg.popup("\nATENÇÃO: Carro não encontrado")

    def listar(self):
        if not self.__frota_carros:
            sg.popup("Frota de carros está vazia.")
            return

        # Cria uma lista de elementos para cada carro
        carros_exibicao = [
            [sg.Text(f"CARRO--------------\nPlaca: {carro.placa}\nModelo: {carro.modelo}\nMarca: {carro.marca}\nAno: {carro.ano}, "
                    f"\nValor por dia: R$ {carro.valor_por_dia:.2f}\nCategoria: {carro.categoria}\nStatus: {carro.status}\n\n")]
            for carro in self.__frota_carros
        ]

        # Define o layout com uma coluna rolável
        layout = [
            [sg.Text("------ FROTA DE CARROS ------", font=("Helvetica", 16))],
            [sg.Column(carros_exibicao, size=(600, 300), scrollable=True, vertical_scroll_only=True)],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Frota de Carros", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()
        
    def retornar(self):
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
                sg.popup("\nOpção inválida. Tente novamente!")

    def pega_carro_placa(self, placa:str):
        for carro in self.__frota_carros:
            if carro.placa == placa:
                return carro
        return None
