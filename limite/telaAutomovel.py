

class TelaAutomovel():
    
    def pega_infomacao_automovel(self):
        # metdod para coletar informações do veículo do usuário
        print("\n-------- DADOS VEÍCULO ----------")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        marca = input("Marca: ")
        ano = int(input("Ano: "))
        valor_por_dia = input("Valor por dia: ")
    
        # retorna um dicionário com os dados do veículo
        return {
            "placa": placa,
            "modelo": modelo,
            "marca": marca,
            "ano": ano,
            "valor_por_dia": valor_por_dia,
            "status" : "disponivel"
        }

    def mostra_automovel(self, dados_automovel):
        # método para exibir os dados do veículo
        print("Placa: ", dados_automovel["placa"])
        print("Modelo: ", dados_automovel["modelo"])
        print("Marca: ", dados_automovel["marca"])
        print("Ano: ", dados_automovel["ano"])
        print("Valor por dia: ", dados_automovel["valor_por_dia"])
        print("Status: ", dados_automovel["status"])

    def seleciona_automovel(self):
        # metodo para solicitar a placa do automóvel que o usuário deseja buscar
        placa = input("Digite a placa do automóvel que deseja buscar: ")
        return placa