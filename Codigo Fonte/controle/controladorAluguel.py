from exception.veiculoIndisponivelException import VeiculoIndisponivelException
from exception.dadosInvalidosException import DadosInvalidoException
from exception.clienteNaoEncontradoException import ClienteNaoEncontradoException
from entidades.aluguel import Aluguel
from limite.telaAluguel import TelaAluguel
from datetime import datetime, date
from entidades.cliente import Cliente
from entidades.carro import Carro
from entidades.moto import Moto
from entidades.caminhao import Caminhao
from entidades.automovel import Automovel
from daos.aluguelDAO import AluguelDAO

class ControladorAluguel():
    def __init__(self, controladorSistema):
        # Inicializa o controlador de aluguel, associando o controlador do sistema e as telas e controladores necessários.
        self.__controlador_sistema = controladorSistema 
        self.__tela_aluguel = TelaAluguel()
        self.__controlador_cliente = self.__controlador_sistema.controlador_cliente
        self.__controlador_carros = self.__controlador_sistema.controlador_carros
        self.__controlador_motos = self.__controlador_sistema.controlador_motos
        self.__controlador_caminhoes = self.__controlador_sistema.controlador_caminhoes
        self.__aluguel_dao = AluguelDAO() # sem o uso de lista, agora usando o DAO para persistência de aluguéis
    
    def realizar_aluguel(self):
        while True:
            try:
                # Recebe os dados para o aluguel a partir da tela e busca o cliente pelo CPF.
                dados_aluguel = self.__tela_aluguel.pega_dados_aluguel()
                if not dados_aluguel:
                    return
                cpf_cliente = dados_aluguel["cliente"]
                cliente = self.__controlador_cliente.pega_cliente_por_cpf(cpf_cliente)

                if not cliente:
                    raise ClienteNaoEncontradoException("Cliente não foi encontrado.")
                
                automovel = None  # inicializando automóvel para verificação posterior

                # tenta encontrar o automóvel informado, verificando em cada controlador específico.
                if self.__controlador_carros.pega_carro_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_carros.pega_carro_placa(dados_aluguel["automovel"])
                elif self.__controlador_motos.pega_moto_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_motos.pega_moto_placa(dados_aluguel["automovel"])
                elif self.__controlador_caminhoes.pega_caminhao_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_caminhoes.pega_caminhao_placa(dados_aluguel["automovel"])

                if not automovel:
                    raise VeiculoIndisponivelException("Veículo Indisponível.")
                
                data_inicio = datetime.strptime(dados_aluguel["data_inicio"], "%d/%m/%Y").date()
                data_final = datetime.strptime(dados_aluguel["data_final"], "%d/%m/%Y").date()

                if data_inicio > data_final:
                    raise DadosInvalidoException("A data de início do aluguel não pode ser posterior à data final.")

                # Calcula o número de dias entre as datas
                dias_aluguel = (data_final - data_inicio).days
                if dias_aluguel == 0:
                    dias_aluguel = 1
                valor_total = automovel.valor_por_dia * dias_aluguel

                if isinstance(automovel, Moto):
                    valor_total += automovel.seguro_adicional * dias_aluguel

            except DadosInvalidoException as e:
                self.__tela_aluguel.mostra_mensagem("\nErro:", e)
                continue
            except ClienteNaoEncontradoException as e:
                self.__tela_aluguel.mostra_mensagem("\nErro:", e)
                continue
            except VeiculoIndisponivelException as e:
                self.__tela_aluguel.mostra_mensagem("\nErro:", e)
                continue
            
            # cria uma nova instância de aluguel com os dados coletados.
            novo_aluguel = Aluguel(cliente, automovel, data_inicio, data_final)

            # verifica se o cliente possui a categoria de CNH adequada e se está válida.
            if self.categoria_valida(cliente, automovel):
                if novo_aluguel.cliente.cnh.validade > date.today():
                    try:
                        if automovel.status == "Disponível":

                            # verifica se o cliente já possui um aluguel em andamento.
                            for aluguel in self.__aluguel_dao.get_all():
                                if aluguel.cliente == novo_aluguel.cliente:
                                    self.__tela_aluguel.mostra_mensagem("\nAtenção" ,"Cliente já está alugando outro veículo.")
                                    return
                                
                            automovel.status = "Indisponível"
                            self.__aluguel_dao.add(novo_aluguel.cliente.cpf, novo_aluguel)
                            self.__tela_aluguel.mostra_mensagem(f"\nPagamento" ,f"O valor final totalizou: R${valor_total:.2f}")
                            self.__tela_aluguel.mostra_mensagem("\nPagamento" ,"Realizando pagamento...")       
                            self.__tela_aluguel.mostra_mensagem("\nPagamento" ,"Aluguel realizado com sucesso!")
                            return novo_aluguel
                        else:
                            raise VeiculoIndisponivelException("Veículo Indisponível.")
                        
                    except VeiculoIndisponivelException as e:
                        self.__tela_aluguel.mostra_mensagem("\nErro:", e)
                        continue
                    
                else:
                    self.__tela_aluguel.mostra_mensagem("\nAtenção", "CNH do cliente está fora da validade.\nAluguel não realizado")
                    return
            else:
                self.__tela_aluguel.mostra_mensagem("\nAtenção:", "Categoria da CNH não é compatível com tipo de veículo.\nAluguel não realizado.")
                return

    # Altera os valores do aluguel já registrado, a partir do CPF cadastrado  
    def alterar_datas_aluguel(self):
        cpf_original = self.__tela_aluguel.seleciona_aluguel()
        aluguel_encontrado = None

        # Procura o aluguel correspondente ao CPF informado.
        for aluguel in self.__aluguel_dao.get_all():
            if aluguel.cliente.cpf == cpf_original:
                aluguel_encontrado = aluguel
                break

        # Caso o aluguel seja encontrado, permite a alteração.
        if aluguel_encontrado is not None:
            novos_dados = self.__tela_aluguel.pega_dados_aluguel()

            try:
                #verifica se o CPF e o automóvel foram alterados
                cpf_cliente_novo = novos_dados["cliente"]
                automovel_novo = novos_dados["automovel"]

                if cpf_cliente_novo != cpf_original:
                    raise DadosInvalidoException("O CPF não pode ser alterado. Para fazer isso, faça a devolução e realize um novo aluguel.")

                # se o automóvel for diferente, mostra um aviso de erro
                if automovel_novo != aluguel_encontrado.automovel.placa:
                    raise DadosInvalidoException("O automóvel não pode ser alterado. Para fazer isso, faça a devolução e realize um novo aluguel")

                #Converte e valida as novas datas.
                data_inicio = datetime.strptime(novos_dados["data_inicio"], "%d/%m/%Y").date()
                data_final = datetime.strptime(novos_dados["data_final"], "%d/%m/%Y").date()

                if data_inicio > data_final:
                    raise DadosInvalidoException("A data de início do aluguel não pode ser posterior à data final.")

                # atualiza as datas do aluguel
                aluguel_encontrado.data_inicio = data_inicio
                aluguel_encontrado.data_final = data_final

                self.__tela_aluguel.mostra_mensagem("Sucesso","Datas do aluguel alteradas.")
            
            except DadosInvalidoException as e:
                self.__tela_aluguel.mostra_mensagem(f"Erro", e)
        else:
            self.__tela_aluguel.mostra_mensagem("\nErro", "Não foi encontrado nenhum aluguel para este CPF.")


    # Verifica a categoria da CNH do cliente para garantir que seja compatível com o tipo de automóvel.
    def categoria_valida(self, cliente: Cliente, automovel: Automovel) -> bool:
        if isinstance(automovel, Caminhao) and cliente.cnh.categoria == "C":
            return True
        elif isinstance(automovel, Moto) and (cliente.cnh.categoria == "A" or cliente.cnh.categoria == "AB"):
            return True
        elif isinstance(automovel, Carro) and (cliente.cnh.categoria == "B" or cliente.cnh.categoria == "AB"):
            return True
        else:
            return False

    # Faz a devolução do veículo, a partir do CPF cadastrado
    def devolucao(self):
        cpf = self.__tela_aluguel.seleciona_aluguel()
        aluguel_encontrado = None
        
        for aluguel in self.__aluguel_dao.get_all():
            if aluguel.cliente.cpf == cpf:
                aluguel_encontrado = aluguel
                break
        
        if aluguel_encontrado is not None:
            self.__aluguel_dao.remove(cpf)
            aluguel_encontrado.automovel.status = "Disponível"
            self.__tela_aluguel.mostra_mensagem("\nSucesso:","Devolução realizada")
        else:
            self.__tela_aluguel.mostra_mensagem("\nErro:","Não foi encontrado nenhum aluguel para este CPF.")

    #Lista os alugueis cadastrados
    def alugueis(self):
        alugueis = self.__aluguel_dao.get_all()
        if not alugueis:
            self.__tela_aluguel.mostra_mensagem("Atenção", "Nenhum aluguel cadastrado.")
            return
        self.__tela_aluguel.listar_alugueis(alugueis)

    # Lista os registros de aluguéis que foram registrados em determinado intervalo de tempo
    def alugueis_por_data(self):
        alugueis_no_intervalo = []
        dados_intervalo = self.__tela_aluguel.intervalo()
        data_inicio_intervalo = datetime.strptime(dados_intervalo["data_inicio"], "%d/%m/%Y").date()
        data_final_intervalo = datetime.strptime(dados_intervalo["data_final"], "%d/%m/%Y").date()
        
        if data_inicio_intervalo > data_final_intervalo:
            self.__tela_aluguel.mostra_mensagem("Erro", "A data de início do intervalo não pode ser posterior à data final.")
            return []
         
        for aluguel in self.__aluguel_dao.get_all():
            if (aluguel.data_inicio >= data_inicio_intervalo and aluguel.data_inicio < data_final_intervalo ) or (aluguel.data_final < data_final_intervalo and aluguel.data_final > data_inicio_intervalo):
                # Calcula o valor total para cada aluguel no intervalo
                dias_aluguel = (aluguel.data_final - aluguel.data_inicio).days
                valor_total = aluguel.automovel.valor_por_dia * dias_aluguel

                if isinstance(aluguel.automovel, Moto):
                    valor_total += aluguel.automovel.seguro_adicional * dias_aluguel
                alugueis_no_intervalo.append(aluguel)

        self.__tela_aluguel.listar_alugueis(alugueis_no_intervalo)

        if len(alugueis_no_intervalo) == 0:
            self.__tela_aluguel.mostra_mensagem("Atenção", "Não há aluguéis nesse intervalo.")
            return 

    # Retornar ao menu principal
    def retornar(self):
        return

    # Mostra o menu de opções para o usuário e chama a função correspondente com base na escolha
    def abre_tela(self):
        lista_opcoes = {
            1: self.realizar_aluguel,
            2: self.devolucao,
            3: self.alugueis,
            4: self.alugueis_por_data,
            5: self.alterar_datas_aluguel,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_aluguel.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0: 
                    break

    def converter_data(self, data_str: str):
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia).date()
