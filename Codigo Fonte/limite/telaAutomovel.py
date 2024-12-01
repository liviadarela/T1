import PySimpleGUI as sg

class TelaAutomovel():
    
    def pega_informacao_automovel(self):
        # método para coletar informações do veículo do usuário
        layout = [
            [sg.Text("-------- DADOS VEÍCULO ----------")],
            [sg.Text("Placa: "), sg.InputText(key='placa')],
            [sg.Text("Modelo: "), sg.InputText(key='modelo')],
            [sg.Text("Marca: "), sg.InputText(key='marca')],
            [sg.Text("Ano: "), sg.InputText(key='ano')],
            [sg.Text("Valor por dia: "), sg.InputText(key='valor_por_dia')],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Veículo", layout)
        
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.close()
                return None  # Caso o usuário cancele ou feche a janela

            if event == "Confirmar":
                # Coleta os dados inseridos
                placa = values['placa']
                modelo = values['modelo']
                marca = values['marca']
                ano = int(values['ano']) if values['ano'].isdigit() else 0
                valor_por_dia = values['valor_por_dia']

                # Retorna um dicionário com os dados do veículo
                window.close()
                return {
                    "placa": placa,
                    "modelo": modelo,
                    "marca": marca,
                    "ano": ano,
                    "valor_por_dia": valor_por_dia,
                    "status": "disponivel"
                }

    def mostra_automovel(self, dados_automovel):
        # método para exibir os dados do veículo
        layout = [
            [sg.Text(f"Placa: {dados_automovel['placa']}")],
            [sg.Text(f"Modelo: {dados_automovel['modelo']}")],
            [sg.Text(f"Marca: {dados_automovel['marca']}")],
            [sg.Text(f"Ano: {dados_automovel['ano']}")],
            [sg.Text(f"Valor por dia: {dados_automovel['valor_por_dia']}")],
            [sg.Text(f"Status: {dados_automovel['status']}")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Detalhes do Veículo", layout)

        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED or event == "Fechar":
                break
        window.close()

    def seleciona_automovel(self):
        # método para solicitar a placa do automóvel que o usuário deseja buscar
        layout = [
            [sg.Text("Digite a placa do automóvel que deseja buscar:")],
            [sg.InputText(key="placa")],
            [sg.Button("Buscar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Buscar Veículo", layout)

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                window.close()
                return None  # Retorna None se cancelar ou fechar

            if event == "Buscar":
                placa = values['placa']
                window.close()
                return placa  # Retorna a placa inserida

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
                return None  # Se o usuário voltar ou fechar a janela

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
                return None  # Caso o usuário cancele ou feche a janela

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

    def mostra_mensagem(self, mensagem, tipo="info"):
        # Exibe uma mensagem na interface gráfica
        if tipo == "info":
            sg.popup("Informação", mensagem)
        elif tipo == "erro":
            sg.popup_error("Erro", mensagem)
        elif tipo == "aviso":
            sg.popup_notify("Aviso", mensagem)
