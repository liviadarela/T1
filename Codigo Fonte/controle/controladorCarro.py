import PySimpleGUI as sg
from exception.dadosInvalidosException import DadosInvalidoException
from entidades.carro import Carro
from limite.telaCarro import TelaCarro
from controle.controladorAutomovel import ControladorAutomovel


#classe ControladorCarro realiza operações específicas para o gerenciamento de carros, 
#incluindo métodos para incluir, excluir e listar veículos da frota de carros, tambem 
# fornece uma interface de interação com o usuário através de uma tela específica e 
# permite busca de carros pela placa.

class ControladorCarro(ControladorAutomovel):
    def __init__(self, controlador_sistema):
        super().__init__() 
        self.__frota_carros = []
        self.__tela_carro = TelaCarro()

    def incluir_automovel(self):
        try:
            while True:
                #pega os dados do carro através da tela 
                dados_carro = self.__tela_carro.pega_informacao_automovel()
                if dados_carro == None:
                    break

                for campo, valor in dados_carro.items():
                    if not valor:  # Verifica se está vazio
                        raise DadosInvalidoException(f"O campo '{campo}' não pode estar vazio.")

                categoria = dados_carro["categoria"]
                
                if not categoria.isalpha():
                    raise DadosInvalidoException("A categoria deve conter apenas letras.")

                    # Verifica se a placa já existe na frota
                placa = dados_carro["placa"]
                if self.pega_carro_placa(placa):
                    self.__tela_carro.mostra_mensagem("Erro", "Essa placa já está cadastrada no sistema.")
                    break

                    # Verifica se o ano é válido (exemplo: entre 1900 e 2025)
                ano = int(dados_carro["ano"])
                if ano < 1800 or ano > 2026:
                    raise DadosInvalidoException("Ano inválido.")

                    # Verifica se o valor por dia é um número positivo
                valor_por_dia = float(dados_carro["valor_por_dia"])
                if valor_por_dia <= 0:
                    raise DadosInvalidoException("O valor por dia deve ser positivo.")

                    # Cria a instância do Carro com os dados fornecidos
                carro = Carro(
                    placa=placa,
                    modelo=dados_carro["modelo"],
                    marca=dados_carro["marca"],
                    ano=dados_carro["ano"],
                    valor_por_dia=valor_por_dia,
                    categoria=categoria                
                )

                # Adiciona o carro à frota
                self.__frota_carros.append(carro)
                self.__tela_carro.mostra_mensagem("Sucesso", "Carro incluído!")
                break
        except DadosInvalidoException as e:
            self.__tela_carro.mostra_mensagem("Erro", e)

    def excluir_automovel(self):
        # metodo para excluir um carro da frota
        placa_automovel = self.__tela_carro.seleciona_automovel()
        automovel_encontrado = False

        # Busca o carro na frota pelo número da placa
        for automovel in self.__frota_carros:
            if automovel.placa == placa_automovel:
                self.__frota_carros.remove(automovel)
                self.__tela_carro.mostra_mensagem("Sucesso", "Carro excluído!")
                automovel_encontrado = True
                break

        if not automovel_encontrado:
            self.__tela_carro.mostra_mensagem("Aviso", "Carro não encontrado")

    def listar(self):
        if not self.__frota_carros:
            self.__tela_carro.mostra_mensagem("Aviso", "Frota de carros está vazia")
        self.__tela_carro.listarcarros(self.__frota_carros)

    def retornar(self):
        return 
    
    def abre_tela(self):
        # metodo para abrir a tela de opções para o usuário
        lista_opcoes = {
            1: self.incluir_automovel,
            2: self.excluir_automovel,
            3: self.listar,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_carro.tela_opcoes()
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
                if opcao == 0: 
                    break

    def pega_carro_placa(self, placa:str):
        for carro in self.__frota_carros:
            if carro.placa == placa:
                return carro
        return None
