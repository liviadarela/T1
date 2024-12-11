import PySimpleGUI as sg

class TelaCliente:
    def tela_opcoes(self):
        # Layout das opções
        layout = [
            [sg.Text("-------- OPÇÕES CLIENTES ----------")],
            [sg.Button("Incluir Cliente"), sg.Button("Alterar Cliente")],
            [sg.Button("Listar Clientes"), sg.Button("Excluir Cliente")],
            [sg.Button("Retornar")]
        ]

        window = sg.Window("Opções de Clientes", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Retornar"):
                window.close()
                return 0  # retornar ao menu anterior

            if event == "Incluir Cliente":
                window.close()
                return 1  # incluir cliente

            if event == "Alterar Cliente":
                window.close()
                return 2  # alterar cliente

            if event == "Listar Clientes":
                window.close()
                return 3  # listar clientes

            if event == "Excluir Cliente":
                window.close()
                return 4  #  excluir cliente

    def pega_dados_cliente(self):
        # Layout para entrada dos dados do cliente
        layout = [
            [sg.Text("-------- DADOS CLIENTE ----------")],
            [sg.Text("Nome:"), sg.InputText(key="nome")],
            [sg.Text("CPF (apenas números):"), sg.InputText(key="cpf")],
            [sg.Text("Data de Nascimento (dd/mm/aaaa):"), sg.InputText(key="data_nascimento")],
            [sg.Text("Endereço:"), sg.InputText(key="endereco")],
            [sg.Text("Número da CNH:"), sg.InputText(key="numero_cnh")],
            [sg.Text("Categoria da CNH (A, B, C, etc.):"), sg.InputText(key="categoria_cnh")],
            [sg.Text("Validade da CNH (dd/mm/aaaa):"), sg.InputText(key="validade_cnh")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Cliente", layout)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break

            if event == "Confirmar":
                if all(values[key].strip() for key in values):
                    window.close()
                    return values  
                else:
                    sg.popup("Erro", "Todos os campos devem ser preenchidos.")
        window.close()

    def mostra_cliente(self,dados_clientes):
        cliente_layout = []

        for cliente in dados_clientes:
            cliente_layout.append([sg.Text(f"Nome: {cliente['nome']}")])
            cliente_layout.append([sg.Text(f"CPF: {cliente['cpf']}")])
            cliente_layout.append([sg.Text(f"Data de Nascimento: {cliente['data_nascimento']}")])
            cliente_layout.append([sg.Text(f"Endereço: {cliente['endereco']}")])
            cliente_layout.append([sg.Text(f"CNH: {cliente['numero_cnh']}")])
            cliente_layout.append([sg.Text(f"Categoria CNH: {cliente['categoria_cnh']}")])
            cliente_layout.append([sg.Text(f"Validade CNH: {cliente['validade_cnh']}")])
            cliente_layout.append([sg.HorizontalSeparator()])  # Separador entre os clientes

        layout = [
            [sg.Text("-------- LISTA DE CLIENTES --------",font=("Helvetica", 16))],
            [sg.Column(
                cliente_layout,
                size=(600, 300),  
                scrollable=True,
                vertical_scroll_only=True
            )],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Lista de Clientes", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()

    def seleciona_cliente(self):
        # layout para selecionar cliente pelo CPF
        layout = [
            [sg.Text("Informe o CPF do cliente que deseja selecionar (apenas números):")],
            [sg.InputText(key="cpf")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Selecionar Cliente", layout)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return self.tela_opcoes() 

            if event == "Confirmar":
                cpf = values["cpf"]
                if cpf.isdigit() and len(cpf) == 11:
                    window.close()
                    return cpf  
                else:
                    sg.popup("Erro", "CPF inválido. Certifique-se de digitar apenas 11 números.")

    def mostra_mensagem(self, titulo: str, mensagem: str):
        sg.popup(f"--- {titulo.upper()} ---\n\n{mensagem}\n")