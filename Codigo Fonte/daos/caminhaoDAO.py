from daos.dao import DAO


class CaminhaoDAO(DAO):
    def __init__(self):
        super().__init__('caminhoes.pkl')  # definindo o arquivo de persistência