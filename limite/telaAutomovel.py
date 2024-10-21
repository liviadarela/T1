from abc import ABC, abstractmethod
class TelaAutomoveis(ABC):
    def tela_opcoes(self):
        print("-------- AUTOMÓVEIS ---------")
        print("Escolha a opção")
        print("1 - Carro")
        print("2 - Moto")
        print("3 - Caminhao")
        print("0 - Retornar")
        
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    @abstractmethod
    def pega_infomacao_automovel(self):
        print("-------- AUTOMÓVEL----------")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        marca = input("Marca: ")
        ano = input("Ano: ")
        valor_por_dia = input("Valor por dia: ")
    
        return {
            "placa": placa,
            "modelo": modelo,
            "marca": marca,
            "ano": ano,
            "valor_por_dia": valor_por_dia,
        }
    
    @abstractmethod
    def mostra_autmovel(self, dados_automovel):
       # print("-------- CLIENTE ----------") 
        print("Placa: ", dados_automovel["placa"])
        print("Modelo: ", dados_automovel["modelo"])
        print("Marca: ", dados_automovel["marca"])
        print("Ano: ", dados_automovel["ano"])
        print("Valor por dia: ", dados_automovel["valor_por_dia"])

    def seleciona_automovel(self):
        placa = input("Placa do automovel que deseja buscar: ")
        return placa