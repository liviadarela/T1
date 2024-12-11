from daos.dao import DAO

#importando da classe Dao
class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')  # definindo o arquivo de persistência