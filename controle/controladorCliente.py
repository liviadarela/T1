from limite.telaCliente import TelaCliente
from entidades.cliente import Cliente
from entidades.cnh import Cnh
from datetime import datetime

class ControladorCliente():
    def __init__(self, controladorSistema):  
        self.__clientes = []  
        self.__tela_cliente = TelaCliente() 
        self.__controlador_sistema = controladorSistema  

    def pega_cliente_por_cpf(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    # método para incluir um novo cliente 
    def incluir_cliente(self):
        while True:
            try:
                dados_cliente = self.__tela_cliente.pega_dados_cliente()

                nome = dados_cliente["nome"]
                if not nome.replace(" ", "").isalpha():
                    raise ValueError("O nome deve conter apenas letras.")

                cpf = dados_cliente["cpf"]
                for cliente in self.__clientes:
                    if cliente.cpf == cpf:
                        raise ValueError("CPF já cadastrado")
                
                if not cpf.isdigit() or len(cpf) != 11:
                    raise ValueError("O CPF deve conter apenas 11 dígitos numéricos.")

                data_nascimento = self.__converter_data(dados_cliente["data_nascimento"])
                if data_nascimento > datetime.now().date():
                    raise ValueError("A data de nascimento não pode ser uma data futura.")

                validade_cnh = self.__converter_data(dados_cliente["validade_cnh"])

                cnh = Cnh(dados_cliente["numero_cnh"], dados_cliente["categoria_cnh"], validade_cnh)
                cliente = Cliente(nome, cpf, data_nascimento, dados_cliente["endereco"], cnh)

                self.__clientes.append(cliente)

                print("\nCliente incluído com sucesso!")
                break
            except ValueError as e:
                print(f"\nErro: {e}")
                print("Por favor, insira os dados novamente.\n")

    def alterar_cliente(self):
        #alterando so dados armazenados de um cliente
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)

        if cliente is not None:
            while True:
                try:
                    novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()

                    # validação do nome
                    nome = novos_dados_cliente["nome"]
                    if not nome.replace(" ", "").isalpha():
                        raise ValueError("O nome deve conter apenas letras.")
                    cliente.nome = nome

                    # validação e atualização do CPF
                    novo_cpf = novos_dados_cliente["cpf"]
                    if novo_cpf != cliente.cpf:
                        for outro_cliente in self.__clientes:
                            if outro_cliente.cpf == novo_cpf:
                                print("erro")
                                raise ValueError("CPF já cadastrado.")
                        
                    if not novo_cpf.isdigit() or len(novo_cpf) != 11:
                        raise ValueError("O CPF deve conter exatamente 11 dígitos numéricos.")
                    cliente.cpf = novo_cpf

                    # validação da data de nascimento
                    cliente.data_nascimento = self.__converter_data(novos_dados_cliente["data_nascimento"])

                    # atualização do endereço
                    cliente.endereco = novos_dados_cliente["endereco"]

                    # validação e atualização da CNH
                    validade_cnh = self.__converter_data(novos_dados_cliente["validade_cnh"])
                    cliente.cnh = Cnh(novos_dados_cliente["numero_cnh"], novos_dados_cliente["categoria_cnh"], validade_cnh)

                    print("\nCliente alterado com sucesso!")
                    break
                except ValueError as e:
                    print(f"\nErro: {e}")
                    print("Por favor, insira os dados novamente.\n")
        else:
            print("\nATENÇÃO: Cliente não existente")

    def lista_clientes(self):
        if not self.__clientes:
            print("\nLista de clientes está vazia.")
        else:
            for cliente in self.__clientes:
                self.__tela_cliente.mostra_cliente({
                    "nome": cliente.nome,
                    "cpf": cliente.cpf,
                    "data_nascimento": cliente.data_nascimento.strftime("%d/%m/%Y"),
                    "endereco": cliente.endereco,
                    "numero_cnh": cliente.cnh.numero,
                    "categoria_cnh": cliente.cnh.categoria,
                    "validade_cnh": cliente.cnh.validade.strftime("%d/%m/%Y")
                })

    def excluir_cliente(self):
        self.lista_clientes()
        cpf_cliente = self.__tela_cliente.seleciona_cliente()
        cliente = self.pega_cliente_por_cpf(cpf_cliente)
        

        if cliente is not None:
            self.__clientes.remove(cliente)
            print("\nCliente excluído com sucesso!")
            self.lista_clientes()
        else:
            print("\nATENCAO: Cliente não existente")

    def retornar(self):
        print("\nRetornando ao menu principal...")
        return
         
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_cliente,
            2: self.alterar_cliente,
            3: self.lista_clientes,
            4: self.excluir_cliente,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_cliente.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0:  
                    break
            else:
                print("\nOpção inválida. Tente novamente!")

    def __converter_data(self, data_str: str):
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia).date()
