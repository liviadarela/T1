import PySimpleGUI as sg

sg.theme("LightGreen6")

class TelaSistema:
    def tela_opcoes(self):
        layout = [
            [sg.Text("SISTEMA ALUGUEL DE AUTOMÓVEIS", font=("Helvetica", 16))],
            [sg.Button("Automóveis", key=1)],
            [sg.Button("Clientes", key=2)],
            [sg.Button("Aluguéis", key=3)],
            [sg.Button("Encerrar Sistema", key=0)]
        ]

        window = sg.Window("Tela Principal", layout)
        event, _ = window.read()
        window.close()

        return int(event) if event is not None else 0

    def tela_opcoes_automovel(self):
        layout = [
            [sg.Text("OPÇÕES AUTOMÓVEIS", font=("Helvetica", 16))],
            [sg.Button("Gerenciar Frota de Carros", key=1)],
            [sg.Button("Gerenciar Frota de Motos", key=2)],
            [sg.Button("Gerenciar Frota de Caminhões", key=3)],
            [sg.Button("Retornar", key=0)]
        ]

        window = sg.Window("Tela Automóveis", layout)
        event, _ = window.read()
        window.close()

        return int(event) if event is not None else 0
    
    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.popup(f"--- {titulo.upper()} ---\n\n{mensagem}\n")