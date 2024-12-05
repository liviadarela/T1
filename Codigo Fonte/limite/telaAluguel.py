import PySimpleGUI as sg
from entidades.moto import Moto


class TelaAluguel:
    def tela_opcoes(self):
    # Layout das opções
        layout = [
            [sg.Text("-------- OPÇÕES DE ALUGUEL --------")],
            [sg.Button("Realizar Aluguel", key=1), sg.Button("Devolução", key=2)],
            [sg.Button("Listar Aluguéis", key=3), sg.Button("Listar Aluguéis por Data", key=4)],
            [sg.Button("Alterar Data do Aluguel", key=5), sg.Button("Sair", key=0)]
        ]

        window = sg.Window("Tela de Aluguel", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, 0):  # Verifica se a janela foi fechada ou se o botão 'Sair' foi pressionado
                window.close()
                return 0  

            if event == 1:  # Realizar Aluguel
                window.close()
                return 1  

            if event == 2:  # Devolução
                window.close()
                return 2  

            if event == 3:  # Listar Aluguéis
                window.close()
                return 3  

            if event == 4:  # Listar Aluguéis por Data
                window.close()
                return 4  

            if event == 5:  # Alterar Data do Aluguel
                window.close()
                return 5


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
                return 0
            
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
            [sg.Text("------ ALUGUÉIS CADASTRADOS ------")],
        ]
        
        for aluguel in alugueis:
            dias_aluguel = (aluguel.data_final - aluguel.data_inicio).days
            if dias_aluguel == 0:
                dias_aluguel = 1  # Garantir que o aluguel de 1 dia seja contabilizado
            valor_total = aluguel.automovel.valor_por_dia * dias_aluguel
            
            if isinstance(aluguel.automovel, Moto):
                valor_total += aluguel.automovel.seguro_adicional * dias_aluguel
            
            # Adicionando os detalhes do aluguel ao layout
            layout.append([sg.Text(f"Nome: {aluguel.cliente.nome}")])
            layout.append([sg.Text(f"CPF: {aluguel.cliente.cpf}")])
            layout.append([sg.Text(f"Placa: {aluguel.automovel.placa}")])
            layout.append([sg.Text(f"Data Início: {aluguel.data_inicio.strftime('%d/%m/%Y')}")])
            layout.append([sg.Text(f"Data Final: {aluguel.data_final.strftime('%d/%m/%Y')}")])
            layout.append([sg.Text(f"Valor Total: R${valor_total:.2f}")])
            
            layout.append([sg.HorizontalSeparator()])  # Separador entre os aluguéis
        
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
            [sg.Button("Confirmar")]
        ]

        janela = sg.Window("Intervalo de Datas", layout)

        while True:
            evento, valores = janela.read()
            
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
                return self.tela_opcoes
            if event == 'Confirmar':  # Quando o CPF for inserido e o botão 'Confirmar' for pressionado
                cpf = values['cpf']
                window.close()
                return cpf