from entidades.cnh import Cnh
from datetime import date

class controladorCnh():
    def cnh_valida(self) -> bool:
        return self.__vencimento >= date.today() 
