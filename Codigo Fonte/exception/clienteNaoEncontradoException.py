class ClienteNaoEncontradoException(Exception):
    #exceção levantada quando o cliente não é encontrado no sistema.
    def _init_(self):
        super().__init__(f"Cliente não foi encontrado no sistema.")
        

