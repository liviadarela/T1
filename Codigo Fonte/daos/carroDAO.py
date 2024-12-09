from daos.dao import DAO


class CarroDAO(DAO):
    def __init__(self):
        super().__init__('carros.pkl')  # definindo o arquivo de persistência