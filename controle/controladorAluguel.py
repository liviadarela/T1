
from entidades.aluguel import Aluguel
from limite.telaAluguel import TelaAluguel
from datetime import datetime, date
from entidades.cliente import Cliente
from entidades.carro import Carro
from entidades.moto import Moto
from entidades.caminhao import Caminhao
from entidades.automovel import Automovel

class ControladorAluguel():
    def __init__(self, controladorSistema,):
        self.__controlador_sistema = controladorSistema 
        self.__tela_aluguel = TelaAluguel()
        self.__controlador_cliente = self.__controlador_sistema.controlador_cliente
        self.__controlador_carros = self.__controlador_sistema.controlador_carros
        self.__controlador_motos = self.__controlador_sistema.controlador_motos
        self.__controlador_caminhoes = self.__controlador_sistema.controlador_caminhoes
        self.__alugueis = []

    
    def realizar_aluguel(self):
        while True:
            try:
                dados_aluguel = self.__tela_aluguel.pega_dados_aluguel()
                cpf_cliente = dados_aluguel["cliente"]

                # Busca o cliente pelo CPF usando o controlador de clientes
                cliente = self.__controlador_cliente.pega_cliente_por_cpf(cpf_cliente)

                if not cliente:
                    raise ValueError("Cliente não encontrado.")
                
                automovel = None  # Inicializando automóvel para verificação posterior

                if self.__controlador_carros.pega_carro_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_carros.pega_carro_placa(dados_aluguel["automovel"])
                elif self.__controlador_motos.pega_moto_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_motos.pega_moto_placa(dados_aluguel["automovel"])
                elif self.__controlador_caminhoes.pega_caminhao_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_caminhoes.pega_caminhao_placa(dados_aluguel["automovel"])

                if not automovel:
                    raise ValueError("Automóvel não encontrado.")
                
                data_inicio = datetime.strptime(dados_aluguel["data_inicio"], "%d/%m/%Y").date()
                data_final = datetime.strptime(dados_aluguel["data_final"], "%d/%m/%Y").date()

                if data_inicio > data_final:
                    raise ValueError("A data de início do aluguel não pode ser posterior à data final.")

                # Calcula o número de dias entre as datas
                dias_aluguel = (data_final - data_inicio).days
                valor_total = automovel.valor_por_dia * dias_aluguel

                if isinstance(automovel, Moto):
                    valor_total += automovel.seguro_adicional * dias_aluguel

            except ValueError as e:
                print(f"\nErro: {e}")
                print("Por favor, tente novamente.\n")
                continue

            novo_aluguel = Aluguel(cliente, automovel, data_inicio, data_final)

            if self.categoria_valida(cliente, automovel) and novo_aluguel.cliente.cnh.validade > date.today() and automovel.status == "Disponível":
                automovel.status = "Indisponível"
                self.__alugueis.append(novo_aluguel)
                print(f"O valor final ficou: R${valor_total:.2f}")
                print("Realizando pagamento")       
                print("\nAluguel registrado com sucesso!")
                return novo_aluguel
            else:
                print("\nNão foi possível realizar o aluguel.")
                return
            
    def categoria_valida(self, cliente: Cliente, automovel: Automovel) -> bool:
        if isinstance(automovel, Caminhao) and cliente.cnh.categoria == "C":
            return True
        elif isinstance(automovel, Moto) and (cliente.cnh.categoria == "A" or cliente.cnh.categoria == "AB"):
            return True
        elif isinstance(automovel, Carro) and (cliente.cnh.categoria == "B" or cliente.cnh.categoria == "AB"):
            return True
        else:
            print("Atenção:Categoria não condiz com o tipo de veíuclo.")
            return False

    def devolucao(self):
        cpf = self.__tela_aluguel.seleciona_aluguel()
        aluguel_encontrado = None
        
        for aluguel in self.__alugueis:
            if aluguel.cliente.cpf == cpf:
                aluguel_encontrado = aluguel
                break
        
        if aluguel_encontrado is not None:
            self.__alugueis.remove(aluguel_encontrado)
            aluguel_encontrado.automovel.status = "Disponível"
            print("\nDevolução realizada com sucesso")
        else:
            print("\nATENÇÃO: Não foi encontrado nenhum aluguel para este CPF.")

    def alugueis(self):
        if not self.__alugueis:
            print("\nNão há aluguéis cadastrados.")
        else:
            for aluguel in self.__alugueis:
                self.__tela_aluguel.mostra_aluguel({
                    "nome": aluguel.cliente.nome,  
                    "cpf": aluguel.cliente.cpf,     
                    "placa": aluguel.automovel.placa,  
                    "data_inicio": aluguel.data_inicio.strftime("%d/%m/%Y"),
                    "data_final": aluguel.data_final.strftime("%d/%m/%Y"),
                    "valor_total": aluguel.automovel.valor_por_dia * (aluguel.data_final - aluguel.data_inicio).days
                })
            print("\nTodos os aluguéis foram exibidos.")

    def alugueis_por_data(self):
        alugueis_no_intervalo = []
        dados_intervalo = self.__tela_aluguel.intervalo()
        data_inicio_intervalo = datetime.strptime(dados_intervalo["data_inicio"], "%d/%m/%Y").date()
        data_final_intervalo = datetime.strptime(dados_intervalo["data_final"], "%d/%m/%Y").date()
        
        if data_inicio_intervalo > data_final_intervalo:
            print("\nErro: A data de início do intervalo não pode ser posterior à data final.")
            return []
    
        for aluguel in self.__alugueis:
            if aluguel.data_inicio >= data_inicio_intervalo or aluguel.data_final <= data_final_intervalo:
                alugueis_no_intervalo.append(aluguel)
                self.__tela_aluguel.mostra_aluguel({
                    "nome": aluguel.cliente.nome,
                    "cpf": aluguel.cliente.cpf,
                    "placa": aluguel.automovel.placa,
                    "data_inicio": aluguel.data_inicio.strftime("%d/%m/%Y"),
                    "data_final": aluguel.data_final.strftime("%d/%m/%Y"),
                    "valor_total": aluguel.automovel.valor_por_dia * (aluguel.data_final - aluguel.data_inicio).days
                })

        if len(alugueis_no_intervalo) == 0:
            print("\nNao há alugueis nesse intervalo.")
            return 
    
    def retornar(self):
        print("\nRetornando ao menu principal...")
        return

    def abre_tela(self):
        lista_opcoes = {
            1: self.realizar_aluguel,
            2: self.devolucao,
            3: self.alugueis,
            4: self.alugueis_por_data,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_aluguel.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0: 
                    break

            else:
                print("\nOpção inválida. Tente novamente.")

    def converter_data(self, data_str: str):
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia).date()