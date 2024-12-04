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
                return 0  # Retornar ao menu anterior

            if event == "Incluir Cliente":
                window.close()
                return 1  # Opção de incluir cliente

            if event == "Alterar Cliente":
                window.close()
                return 2  # Opção de alterar cliente

            if event == "Listar Clientes":
                window.close()
                return 3  # Opção de listar clientes

            if event == "Excluir Cliente":
                window.close()
                return 4  # Opção de excluir cliente

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
                window.close()
                return self.tela_opcoes() # Caso o usuário cancele

            if event == "Confirmar":
                # Verifica se todos os campos estão preenchidos
                if all(values[key].strip() for key in values):
                    window.close()
                    return values  # Retorna os dados inseridos
                else:
                    sg.popup("Erro", "Todos os campos devem ser preenchidos.")

    def mostra_cliente(self, dados_cliente):
        # Layout para exibir os dados do cliente
        layout = [
            [sg.Text("-------- CLIENTE ----------")],
            [sg.Text(f"Nome: {dados_cliente['nome']}")],
            [sg.Text(f"CPF: {dados_cliente['cpf']}")],
            [sg.Text(f"Data de Nascimento: {dados_cliente['data_nascimento']}")],
            [sg.Text(f"Endereço: {dados_cliente['endereco']}")],
            [sg.Text(f"CNH: {dados_cliente['numero_cnh']}")],
            [sg.Text(f"Categoria CNH: {dados_cliente['categoria_cnh']}")],
            [sg.Text(f"Validade CNH: {dados_cliente['validade_cnh']}")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Detalhes do Cliente", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break
        window.close()

    def seleciona_cliente(self):
        # Layout para selecionar cliente pelo CPF
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
                return self.tela_opcoes()  # Caso o usuário cancele

            if event == "Confirmar":
                cpf = values["cpf"]
                if cpf.isdigit() and len(cpf) == 11:
                    window.close()
                    return cpf  # Retorna o CPF informado
                else:
                    sg.popup("Erro", "CPF inválido. Certifique-se de digitar apenas 11 números.")

    def mostra_mensagem(self, titulo: str, mensagem: str):
        """Exibe uma mensagem ao usuário."""
        sg.popup(f"--- {titulo.upper()} ---\n\n{mensagem}\n")