class VeiculoIndisponivelException(Exception):
    #exceção pra quando o veículo solicitado está indisponível.
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem