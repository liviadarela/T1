import PySimpleGUI as sg
from limite.telaAutomovel import TelaAutomovel

class TelaMoto(TelaAutomovel):
    def tela_opcoes(self):
        layout = [
            [sg.Text("\n--------- OPÇÕES MOTOS ---------")],
            [sg.Text("Escolha a opção:")],
            [sg.Button("Cadastrar moto nova"), sg.Button("Excluir moto já cadastrada"), sg.Button("Verificar frota de motos"), sg.Button("Voltar")]
        ]

        window = sg.Window("Opções de Motos", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Voltar"):
                window.close()
                return 0 

            if event == "Cadastrar moto nova":
                window.close()
                return 1

            if event == "Excluir moto já cadastrada":
                window.close()
                return 2

            if event == "Verificar frota de motos":
                window.close()
                return 3

    def pega_informacao_automovel(self):
        dados_comuns = super().pega_informacao_automovel()
        if dados_comuns is None:
            return None

        layout = [
            [sg.Text("Seguro Adicional (R$): "), sg.InputText(key='seguro_adicional')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Moto", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return self.tela_opcoes()

            if event == "Confirmar":
                dados_comuns["seguro_adicional"] = values['seguro_adicional']
                window.close()
                return dados_comuns

    def mostra_automovel(self, dados_automovel):
        layout = [
            [sg.Text("MOTO ---------------------")],
            [sg.Text(f"Placa: {dados_automovel['placa']}")],
            [sg.Text(f"Modelo: {dados_automovel['modelo']}")],
            [sg.Text(f"Marca: {dados_automovel['marca']}")],
            [sg.Text(f"Ano: {dados_automovel['ano']}")],
            [sg.Text(f"Valor por dia: {dados_automovel['valor_por_dia']}")],
            [sg.Text(f"Status: {dados_automovel['status']}")],
            [sg.Text(f"Seguro Adicional: {dados_automovel['seguro_adicional']}")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Detalhes da Moto", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.popup(f"--- {titulo.upper()} ---\n\n{mensagem}\n")

    def listar_motos(self, frota_motos):
        motos_exibicao = [
            [sg.Text(f"MOTO--------------\n\nPlaca: {moto.placa}\n\nModelo: {moto.modelo}\n\nMarca: {moto.marca}\n\nAno: {moto.ano}, "
                    f"\n\nValor por dia: R$ {moto.valor_por_dia:.2f}\n\nSeguro Adicional: {moto.seguro_adicional}\n\nStatus: {moto.status}\n\n")]
            for moto in frota_motos
        ]

        layout = [
            [sg.Text("------ FROTA DE MOTOS ------", font=("Helvetica", 16))],
            [sg.Column(motos_exibicao, size=(600, 300), scrollable=True, vertical_scroll_only=True)],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Frota de Motos", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()
