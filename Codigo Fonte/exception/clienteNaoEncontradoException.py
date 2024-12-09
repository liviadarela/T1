class ClienteNaoEncontradoException(Exception):
    #exceção levantada quando o cliente não é encontrado no sistema.
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem
        

