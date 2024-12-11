class DadosInvalidoException(Exception):
    #execção para quando o dado inserido nao é do tipo desejado
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem
