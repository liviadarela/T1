from datetime import date
from entidades.cliente import Cliente
from entidades.carro import Carro
from entidades.moto import Moto
from entidades.caminhao import Caminhao
from entidades.cnh import Cnh
from entidades.aluguel import Aluguel

# Criando instâncias de CNH
cnh_carro = Cnh(123456, "B", date(2025, 12, 31))
cnh_moto = Cnh(654321, "A", date(2025, 12, 31))
cnh_caminhao = Cnh(789012, "C", date(2025, 12, 31))

# Criando clientes
cliente_carro = Cliente("João", 12345678901, date(1990, 5, 15), "Rua 1", cnh_carro)
cliente_moto = Cliente("Maria", 98765432100, date(1995, 8, 20), "Rua 2", cnh_moto)
cliente_caminhao = Cliente("Pedro", 45678912300, date(1985, 3, 10), "Rua 3", cnh_caminhao)

# Criando automóveis
carro = Carro("Popular", "ABC-1234", "Civic", "Honda", 2020, 150.0)
moto = Moto(30.0, "XYZ-5678", "Ninja", "Kawasaki", 2019, 100.0)
caminhao = Caminhao(4, "DEF-9876", "FH", "Volvo", 2018, 200.0)

# Criando lista de clientes
clientes = [cliente_carro, cliente_moto, cliente_caminhao]

# Teste: Listando todos os clientes
print("Lista de Clientes:")
for cliente in clientes:
    print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, CNH: {cliente.cnh.categoria}")

# Criando lista de automóveis
automoveis = [carro, moto, caminhao]

# Teste: Listando todos os automóveis
print("\nLista de Automóveis:")
for automovel in automoveis:
    print(f"Placa: {automovel.placa}, Modelo: {automovel.modelo}, Marca: {automovel.marca}, Ano: {automovel.ano}, Status: {automovel.status}")

# Criando instância de Aluguel para gerenciar os aluguéis
controlador_aluguel = Aluguel(cliente_carro, carro, date(2024, 10, 1), date(2024, 10, 10))

# Criando aluguéis
aluguel_carro = controlador_aluguel.realizar_aluguel(cliente_carro, carro, date(2024, 10, 1), date(2024, 10, 10))
aluguel_moto = controlador_aluguel.realizar_aluguel(cliente_moto, moto, date(2024, 10, 1), date(2024, 10, 5))
aluguel_caminhao = controlador_aluguel.realizar_aluguel(cliente_caminhao, caminhao, date(2024, 10, 1), date(2024, 10, 7))

# Adicionando os aluguéis à lista
controlador_aluguel.alugueis.append(aluguel_carro)
controlador_aluguel.alugueis.append(aluguel_moto)
controlador_aluguel.alugueis.append(aluguel_caminhao)

# Teste: Listando todos os aluguéis
print("\nLista de Aluguéis:")
for aluguel in controlador_aluguel.listar_alugueis():
    print(f"Cliente: {aluguel.cliente.nome}, Veículo: {aluguel.automovel.modelo}, Data Início: {aluguel.data_inicio}, Data Fim: {aluguel.data_final}")

# Teste de falha: Tentativa de adicionar um cliente sem CNH válida para o veículo
cliente_sem_cnh = Cliente("Lucas", 32165498700, date(1980, 6, 25), "Rua 4", cnh_carro)
aluguel_errado = controlador_aluguel.realizar_aluguel(cliente_sem_cnh, caminhao, date(2024, 10, 1), date(2024, 10, 7))
print(f"\nTentativa de aluguel inválido: {aluguel_errado}")

# Teste: Listando aluguéis dentro de um intervalo de datas
print("\nAluguéis no intervalo de 1 de outubro de 2024 até 10 de outubro de 2024:")
alugueis_no_intervalo = controlador_aluguel.alugueis_por_data(date(2024, 10, 1), date(2024, 10, 10))
for aluguel in alugueis_no_intervalo:
    print(f"Cliente: {aluguel.cliente.nome}, Veículo: {aluguel.automovel.modelo}")
