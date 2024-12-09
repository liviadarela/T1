from daos.dao import DAO


class MotoDAO(DAO):
    def __init__(self):
        super().__init__('motos.pkl')  # definindo o arquivo de persistência