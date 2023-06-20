from persona import Persona

class Cliente(Persona):
    
    def __init__(self, nombre, edad, cuenta, credito):
        super().__init__(nombre, edad)
        self.__cuenta = cuenta
        self.__credito = credito

    def obtener_cuenta(self):
        return ' cuenta nro.: ' + str(self.__cuenta)
    
    def obtener_credito(self):
        return 'credito: ' + str(self.__credito)
    
    def __str__(self):
        return super().__str__() + 'Cuenta Nro.: ' + str(self.__cuenta)