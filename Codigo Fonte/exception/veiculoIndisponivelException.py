class VeiculoIndisponivelException(Exception):
    #Exceção levantada quando o veículo solicitado está indisponível.
    def _init_(self):
        super().__init__(f"Veículo, nao encontrado ou está indisponível para aluguel.")