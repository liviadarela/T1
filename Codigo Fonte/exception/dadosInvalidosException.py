

class DadosInvalidoException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem
