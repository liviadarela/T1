from datetime import date

class ControladorCnh():
    def cnh_valida(self) -> bool:
        return self.__validade >= date.today() 
 
