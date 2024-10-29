
from entidades.aluguel import Aluguel
from limite.telaAluguel import TelaAluguel
from controle.controladorCliente import ControladorCliente
from controle.controladorCarro import ControladorCarro
from controle.controladorMoto import ControladorMoto
from controle.controladorCaminhao import ControladorCaminhao
from datetime import datetime
from entidades.cliente import Cliente
from entidades.carro import Carro
from entidades.moto import Moto
from entidades.caminhao import Caminhao
from entidades.automovel import Automovel

class ControladorAluguel():
    def __init__(self, controladorSistema):
        self.__controlador_sistema = controladorSistema 
        self.__tela_aluguel = TelaAluguel()
        self.__controlador_cliente = ControladorCliente(controladorSistema)
        self.__controlador_carro = ControladorCarro(controladorSistema)
        self.__controlador_moto = ControladorMoto(controladorSistema)
        self.__controlador_caminhao = ControladorCaminhao()
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

                if self.__controlador_carro.pega_carro_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_carro.pega_carro_placa(dados_aluguel["automovel"])
                elif self.__controlador_moto.pega_moto_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_moto.pega_moto_placa(dados_aluguel["automovel"])
                elif self.__controlador_caminhao.pega_caminhao_placa(dados_aluguel["automovel"]):
                    automovel = self.__controlador_caminhao.pega_caminhao_placa(dados_aluguel["automovel"])

                if not automovel:
                    raise ValueError("Automóvel não encontrado.")
                
                dias_aluguel = (dados_aluguel["data_final"] - dados_aluguel["data_inicio"]).days
                valor_total = automovel.valor_por_dia * dias_aluguel

                if isinstance(automovel, Moto):
                    valor_total += automovel.seguro_adicional * dias_aluguel

            except ValueError as e:
                print(f"Erro: {e}")
                print("Por favor, tente novamente.\n")
                continue
                
            if self.categoria_valida(cliente, automovel) and self.__controlador_cliente.pode_alugar() and automovel.status == "Disponível":
                automovel.status = "Indisponível"

                novo_aluguel = Aluguel(cliente, automovel, dados_aluguel["data_inicio"], dados_aluguel["data_final"])
                self.__alugueis.append(novo_aluguel)


                print(f"O valor final ficou: R${valor_total}")
                print("Relizando pagamento")       
                print("\nAluguel registrado com sucesso!")
                return novo_aluguel
            else:
                return("Não foi possivel ralizar o aluguel.")


    def categoria_valida(self, cliente: Cliente, automovel: Automovel) -> bool:
        if isinstance(automovel, Caminhao) and cliente.cnh.categoria == "C":
            return True
        elif isinstance(automovel, Moto) and (cliente.cnh.categoria == "A" or cliente.cnh.categoria == "AB"):
            return True
        elif isinstance(automovel, Carro) and (cliente.cnh.categoria == "B" or cliente.cnh.categoria == "AB"):
            return True
        else:
            print("Aluguel não realizado. Categoria não condiz com o tipo de veíuclo.")
            return False

    def devolucao(self):
        cpf = self.__tela_aluguel.seleciona_aluguel()
        aluguel = self.__controlador_cliente.pega_cliente_por_cpf(cpf)

        if aluguel is not None:
            self.__alugueis.remove(aluguel)
            print("Devolução realizada com sucesso")
        else:
            print("ATENCAO: Não foi encontrado nenhum aluguel nesse CPF.")

    def alugueis(self):
        if not self.__alugueis:
            print("\nNão há aluguéis cadastrados.")
        else:
            for aluguel in self.__alugueis:
                self.__tela_aluguel.mostra_cliente({
                    "cliente": aluguel.cliente,
                    "automovel": aluguel.automovel,
                    "data_inicio": aluguel.data_inicio.strftime("%d/%m/%Y"),
                    "data_final": aluguel.data_final.strftime("%d/%m/%Y"),
                })
            print("\nTodos os aluguéis foram exibidos.")

    def alugueis_por_data(self):
        alugueis_no_intervalo = []
        dados_intervalo = self.__tela_aluguel.intervalo()
        data_inicio_intervalo = datetime.strptime(dados_intervalo["data_inicio"], "%d/%m/%Y").date()
        data_final_intervalo = datetime.strptime(dados_intervalo["data_final"], "%d/%m/%Y").date()
        
        if data_inicio_intervalo > data_final_intervalo:
            print("Erro: A data de início do intervalo não pode ser posterior à data final.")
            return []
    
        for aluguel in self.__alugueis:
            if aluguel.data_inicio >= data_inicio_intervalo and aluguel.data_final <= data_final_intervalo:
                alugueis_no_intervalo.append(aluguel)
                self.__tela_aluguel.mostra_aluguel(aluguel)

        if len(alugueis_no_intervalo) == 0:
            print("\nNao há alugueis nesse intervalo.")
            return 
    
    def retornar(self):
        print("Retornando ao menu principal...")
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
                print("Opção inválida. Tente novamente.")

    def converter_data(self, data_str: str):
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia).date()