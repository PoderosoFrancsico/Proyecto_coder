from paquete.persona import Persona
from paquete.cliente import Cliente


nom = str(input('Nombre: ')).capitalize()
eda = int(input('Edad: '))
ncu = int(input('Numero de cuenta: '))
cre = float(input('Credito: '))

cliente_1 = Cliente(nom, eda, ncu, cre)

print(cliente_1)

print('El cliente posee un credito de: ', cliente_1.obtener_credito())