
class TelaCliente:
    def tela_opcoes(self):
        print("-------- CLIENTES ----------")
        print("Escolha a opção")
        print("1 - Incluir Cliente")
        print("2 - Alterar Cliente")
        print("3 - Listar Clientes")
        print("4 - Excluir Cliente")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_cliente(self):
        print("-------- DADOS CLIENTE ----------")
        nome = input("Nome: ")
        cpf = input("CPF (apenas números): ")
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        endereco = input("Endereço: ")
        numero_cnh = input("Número da CNH: ")
        categoria_cnh = input("Categoria da CNH (A, B, C, etc.): ")
        validade_cnh = input("Validade da CNH (dd/mm/aaaa): ")
    
        return {
            "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
            "numero_cnh": numero_cnh,
            "categoria_cnh": categoria_cnh,
            "validade_cnh": validade_cnh
        }

    def mostra_cliente(self, dados_cliente):
        print("-------- CLIENTE ----------")
        print("Nome: ", dados_cliente["nome"])
        print("CPF: ", dados_cliente["cpf"])
        print("Data de Nascimento: ", dados_cliente["data_nascimento"])
        print("Endereço: ", dados_cliente["endereco"])
        print("CNH: ", dados_cliente["numero_cnh"])
        print("Categoria CNH: ", dados_cliente["categoria_cnh"])
        print("Validade CNH: ", dados_cliente["validade_cnh"])
        print("\n")

    def seleciona_cliente(self):
        cpf = input("CPF do cliente que deseja selecionar: ")
        return cpf

