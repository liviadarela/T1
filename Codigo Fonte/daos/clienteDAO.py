from daos.dao import DAO


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')  # definindo o arquivo de persistência