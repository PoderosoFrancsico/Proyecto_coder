class Persona:

    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return 'Nombre: ' + self.nombre