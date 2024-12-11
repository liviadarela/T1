import PySimpleGUI as sg
from limite.telaAutomovel import TelaAutomovel

class TelaCaminhao(TelaAutomovel):
    def tela_opcoes(self):
        # Método para exibir as opções específicas para caminhões
        layout = [
            [sg.Text("\n--------- OPÇÕES CAMINHÕES ---------")],
            [sg.Text("Escolha a opção:")],
            [sg.Button("Cadastrar caminhão novo"), sg.Button("Excluir caminhão já cadastrado"), sg.Button("Verificar frota de caminhões"), sg.Button("Voltar")]
        ]

        window = sg.Window("Opções de Caminhões", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Voltar"):
                window.close()
                return 0  # Retorna ao menu principal

            if event == "Cadastrar caminhão novo":
                window.close()
                return 1

            if event == "Excluir caminhão já cadastrado":
                window.close()
                return 2

            if event == "Verificar frota de caminhões":
                window.close()
                return 3

    def pega_informacao_automovel(self):
        # Método para coletar informações do caminhão
        dados_comuns = super().pega_informacao_automovel()
        if dados_comuns is None:
            return None

        layout = [
            [sg.Text("Número de Eixos: "), sg.InputText(key='numero_de_eixos')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Caminhão", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return self.tela_opcoes()  # Retorna ao menu principal

            if event == "Confirmar":
                dados_comuns["numero_de_eixos"] = values['numero_de_eixos']
                window.close()
                return dados_comuns

    def mostra_automovel(self, dados_automovel):
        # Método para exibir os detalhes do caminhão
        layout = [
            [sg.Text("CAMINHÃO ---------------------")],
            [sg.Text(f"Placa: {dados_automovel['placa']}")],
            [sg.Text(f"Modelo: {dados_automovel['modelo']}")],
            [sg.Text(f"Marca: {dados_automovel['marca']}")],
            [sg.Text(f"Ano: {dados_automovel['ano']}")],
            [sg.Text(f"Valor por dia: {dados_automovel['valor_por_dia']}")],
            [sg.Text(f"Status: {dados_automovel['status']}")],
            [sg.Text(f"Número de Eixos: {dados_automovel['numero_de_eixos']}")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Detalhes do Caminhão", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.popup(f"--- {titulo.upper()} ---\n\n{mensagem}\n")

    def listar_caminhoes(self, frota_caminhoes):
        caminhoes_exibicao = [
            [sg.Text(f"CAMINHÃO--------------\n\nPlaca: {caminhao.placa}\n\nModelo: {caminhao.modelo}\n\nMarca: {caminhao.marca}\n\nAno: {caminhao.ano}, "
                    f"\n\nValor por dia: R$ {caminhao.valor_por_dia:.2f}\n\nNumero de Eixos: {caminhao.numero_de_eixos}\n\nStatus: {caminhao.status}\n\n")]
            for caminhao in frota_caminhoes
        ]

        # Define o layout com uma coluna rolável
        layout = [
            [sg.Text("------ FROTA DE CAMINHÕES ------", font=("Helvetica", 16))],
            [sg.Column(caminhoes_exibicao, size=(600, 300), scrollable=True, vertical_scroll_only=True)],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Frota de Caminhões", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()

