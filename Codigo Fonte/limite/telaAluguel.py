import PySimpleGUI as sg

class TelaAluguel:
    def tela_opcoes(self):
        # Layout das opções
        layout = [
            [sg.Text("-------- OPÇÕES DE ALUGUEL --------")],
            [sg.Button("Realizar Aluguel", key=1), sg.Button("Devolução", key=2)],
            [sg.Button("Listar Aluguéis", key=3), sg.Button("Listar Aluguéis por Data", key=4)],
            [sg.Button("Alterar Data do Aluguel", key=5), sg.Button("Sair", key=0)]
        ]

        janela = sg.Window("Tela de Aluguel", layout)

        while True:
            evento, _ = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 0:
                janela.close()
                break
            return evento

    def pega_dados_aluguel(self):
        # Layout para pegar os dados do aluguel
        layout = [
            [sg.Text("Informe o CPF do cliente:")],
            [sg.InputText("", key="cliente")],
            [sg.Text("Informe a placa do automóvel:")],
            [sg.InputText("", key="automovel")],
            [sg.Text("Informe a data de início (dd/mm/aaaa):")],
            [sg.InputText("", key="data_inicio")],
            [sg.Text("Informe a data final (dd/mm/aaaa):")],
            [sg.InputText("", key="data_final")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Dados do Aluguel", layout)

        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Cancelar":
                janela.close()
                return {}
            if evento == "Confirmar":
                janela.close()
                return valores

    def mostra_mensagem(self, titulo, mensagem):
        layout = [
            [sg.Text(titulo)],
            [sg.Text(mensagem)],
            [sg.Button("OK")]
        ]
        janela = sg.Window("Mensagem", layout)

        while True:
            evento, _ = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "OK":
                janela.close()
                break

    def listar_alugueis(self, alugueis):
        layout = [
            [sg.Text("------ Aluguéis Cadastrados ------")],
            [sg.Text("Nome Cliente | CPF | Placa | Data Início | Data Final | Valor Total")],
        ]
        
        for aluguel in alugueis:
            valor_total = aluguel.automovel.valor_por_dia * (aluguel.data_final - aluguel.data_inicio).days
            if isinstance(aluguel.automovel, Moto):
                valor_total += aluguel.automovel.seguro_adicional * (aluguel.data_final - aluguel.data_inicio).days

            layout.append([sg.Text(f"{aluguel.cliente.nome} | {aluguel.cliente.cpf} | {aluguel.automovel.placa} | {aluguel.data_inicio.strftime('%d/%m/%Y')} | {aluguel.data_final.strftime('%d/%m/%Y')} | R${valor_total:.2f}")])

        layout.append([sg.Button("OK")])
        janela = sg.Window("Lista de Aluguéis", layout)

        while True:
            evento, _ = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "OK":
                janela.close()
                break

    def intervalo(self):
        # Layout para pegar o intervalo de datas
        layout = [
            [sg.Text("Informe a data de início do intervalo (dd/mm/aaaa):")],
            [sg.InputText("", key="data_inicio")],
            [sg.Text("Informe a data final do intervalo (dd/mm/aaaa):")],
            [sg.InputText("", key="data_final")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        janela = sg.Window("Intervalo de Datas", layout)

        while True:
            evento, valores = janela.read()
            if evento == sg.WINDOW_CLOSED or evento == "Cancelar":
                janela.close()
                return {}
            if evento == "Confirmar":
                janela.close()
                return valores



    def seleciona_aluguel(self):
        # Layout da janela para coletar o CPF
        layout = [
            [sg.Text('Digite o CPF do cliente:')],
            [sg.InputText('', key='cpf')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        
        # Criar a janela
        window = sg.Window('Coletar CPF', layout)
        
        # Loop para interação com o usuário
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':  # Fechar a janela ou cancelar
                window.close()
                return None
            if event == 'Confirmar':  # Quando o CPF for inserido e o botão 'Confirmar' for pressionado
                cpf = values['cpf']
                window.close()
                return cpf