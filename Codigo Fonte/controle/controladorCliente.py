from exception.clienteNaoEncontradoException import ClienteNaoEncontradoException
from exception.dadosInvalidosException import DadosInvalidoException
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

    # método para incluir um novo cliente 
    def incluir_cliente(self):
        while True:
            try:
                dados_cliente = self.__tela_cliente.pega_dados_cliente()

                nome = dados_cliente["nome"]
                if not nome.replace(" ", "").isalpha():
                    raise DadosInvalidoException("O nome deve conter apenas letras.")

                cpf = dados_cliente["cpf"]
                for cliente in self.__clientes:
                    if cliente.cpf == cpf:
                        raise DadosInvalidoException("CPF já cadastrado.")
                
                if not cpf.isdigit() or len(cpf) != 11:
                    raise DadosInvalidoException("O CPF deve conter apenas 11 dígitos numéricos.")

                data_nascimento = self.__converter_data(dados_cliente["data_nascimento"])
                if data_nascimento > datetime.now().date():
                    raise DadosInvalidoException("A data de nascimento não pode ser uma data futura.")

                validade_cnh = self.__converter_data(dados_cliente["validade_cnh"])

                cnh = Cnh(dados_cliente["numero_cnh"], dados_cliente["categoria_cnh"], validade_cnh)
                cliente = Cliente(nome, cpf, data_nascimento, dados_cliente["endereco"], cnh)

                self.__clientes.append(cliente)
                self.__tela_cliente.mostra_mensagem("Sucesso", "Cliente incluído com sucesso!")
                break
            except DadosInvalidoException as e:
                self.__tela_cliente.mostra_mensagem("Erro", str(e))

    def alterar_cliente(self):
        try:
            self.lista_clientes()
            cpf_cliente = self.__tela_cliente.seleciona_cliente()
            cliente = self.pega_cliente_por_cpf(cpf_cliente)

            if cliente is None: 
                raise ClienteNaoEncontradoException("Cliente não encontrado!")

        except ClienteNaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem("Erro", e)

        if cliente is not None:
            while True:
                try:
                    novos_dados_cliente = self.__tela_cliente.pega_dados_cliente()

                    nome = novos_dados_cliente["nome"]
                    if not nome.replace(" ", "").isalpha():
                        raise DadosInvalidoException("O nome deve conter apenas letras.")
                    cliente.nome = nome

                    novo_cpf = novos_dados_cliente["cpf"]
                    if novo_cpf != cliente.cpf:
                        for outro_cliente in self.__clientes:
                            if outro_cliente.cpf == novo_cpf:
                                raise DadosInvalidoException("CPF já cadastrado.")
                        
                    if not novo_cpf.isdigit() or len(novo_cpf) != 11:
                        raise DadosInvalidoException("O CPF deve conter exatamente 11 dígitos numéricos.")
                    cliente.cpf = novo_cpf

                    cliente.data_nascimento = self.__converter_data(novos_dados_cliente["data_nascimento"])

                    cliente.endereco = novos_dados_cliente["endereco"]

                    validade_cnh = self.__converter_data(novos_dados_cliente["validade_cnh"])
                    cliente.cnh = Cnh(novos_dados_cliente["numero_cnh"], novos_dados_cliente["categoria_cnh"], validade_cnh)

                    self.__tela_cliente.mostra_mensagem("Sucesso", "Cliente alterado com sucesso!")
                    break
                except DadosInvalidoException as e:
                    self.__tela_cliente.mostra_mensagem("Erro", e)

    def lista_clientes(self):
        if not self.__clientes:
            self.__tela_cliente.mostra_mensagem("Aviso", "Lista de clientes está vazia.")
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
        try:
            self.lista_clientes()
            cpf_cliente = self.__tela_cliente.seleciona_cliente()
            cliente = self.pega_cliente_por_cpf(cpf_cliente)

            if cliente is None:  # Isso é redundante, mas você pode manter para lógica explícita
                raise ClienteNaoEncontradoException("Cliente não encontrado!")

            self.__clientes.remove(cliente)
            self.__tela_cliente.mostra_mensagem("Sucesso", "Cliente excluído com sucesso!")
        except ClienteNaoEncontradoException as e:
            self.__tela_cliente.mostra_mensagem("Erro", e)
            
    def retornar(self):
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

    def __converter_data(self, data_str: str):
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia).date()
