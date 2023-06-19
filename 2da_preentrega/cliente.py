from persona import Persona

class Cliente(Persona):
    
    def __init__(self, nombre, apellido, edad, cuenta, credito):
        super().__init__(nombre, apellido, edad)
        self.cuenta = cuenta
        self.credito = credito