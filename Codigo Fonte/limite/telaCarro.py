import PySimpleGUI as sg
from limite.telaAutomovel import TelaAutomovel

class TelaCarro(TelaAutomovel):

    def tela_opcoes(self):
        # Método para exibir as opções específicas para carros
        layout = [
            [sg.Text("\n--------- OPÇÕES CARROS ---------")],
            [sg.Text("Escolha a opção:")],
            [sg.Button("Cadastrar carro novo"), sg.Button("Excluir carro já cadastrado"), sg.Button("Verificar frota de carros"), sg.Button("Voltar")]
        ]

        window = sg.Window("Opções de Carros", layout)
        
        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED or event == "Voltar":
                window.close()
                return 0  # Se o usuário voltar ou fechar a janela

            if event == "Cadastrar carro novo":
                window.close()
                return 1  # Retorna a opção de cadastrar carro

            if event == "Excluir carro já cadastrado":
                window.close()
                return 2  # Retorna a opção de excluir carro

            if event == "Verificar frota de carros":
                window.close()
                return 3  # Retorna a opção de verificar frota

    def pega_informacao_automovel(self):
        # método para coletar informações do carro, incluindo dados comuns e categoria
        dados_comuns = super().pega_informacao_automovel()  # chama o método da superclasse
        if dados_comuns is None:
            return None  # Caso o usuário cancele

        layout = [
            [sg.Text("Categoria: "), sg.InputText(key='categoria')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Carro", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.close()
                return self.tela_opcoes()  # Caso o usuário cancele ou feche a janela

            if event == "Confirmar":
                categoria = values['categoria']
                dados_comuns["categoria"] = categoria
                window.close()
                return dados_comuns  # Retorna os dados do carro com a categoria adicionada

    def mostra_automovel(self, dados_automovel):
        # método para exibir os dados do carro, incluindo dados da superclasse
        layout = [
            [sg.Text("CARRO ---------------------")],
            [sg.Text(f"Placa: {dados_automovel['placa']}")],
            [sg.Text(f"Modelo: {dados_automovel['modelo']}")],
            [sg.Text(f"Marca: {dados_automovel['marca']}")],
            [sg.Text(f"Ano: {dados_automovel['ano']}")],
            [sg.Text(f"Valor por dia: {dados_automovel['valor_por_dia']}")],
            [sg.Text(f"Status: {dados_automovel['status']}")],
            [sg.Text(f"Categoria: {dados_automovel['categoria']}")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Detalhes do Carro", layout)

        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED or event == "Fechar":
                break
        window.close()
    
    #exibe uma mensagem ao usuário
    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.popup(f"--- {titulo.upper()} ---\n\n{mensagem}\n")

    def listarcarros(self, frota_carros):
        carros_exibicao = [
            [sg.Text(f"CARRO--------------\n\nPlaca: {carro.placa}\n\nModelo: {carro.modelo}\n\nMarca: {carro.marca}\n\nAno: {carro.ano}, "
                    f"\n\nValor por dia: R$ {carro.valor_por_dia:.2f}\n\nCategoria: {carro.categoria}\n\nStatus: {carro.status}\n\n")]
            for carro in frota_carros
        ]

        # define o layout com uma coluna rolável
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