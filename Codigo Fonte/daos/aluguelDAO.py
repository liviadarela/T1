from daos.dao import DAO


class AluguelDAO(DAO):
    def __init__(self):
        super().__init__('alugueis.pkl')  # definindo o arquivo de persistência