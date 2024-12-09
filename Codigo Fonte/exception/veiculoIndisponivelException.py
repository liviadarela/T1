class VeiculoIndisponivelException(Exception):
    #Exceção levantada quando o veículo solicitado está indisponível.
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem