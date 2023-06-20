#from paquete.persona import Persona
from paquete.cliente import Cliente

num="0123456789"
nom = str(input('Nombre: ')).capitalize()  


for i in range(len(nom)):

  if num.find(nom[i])!=-1:

    nom = str(input('Vuelva a ingresar un nombre: ')).capitalize()  
  else:
    break

while True:
   try:
        eda = int(input('Edad: '))
        break
   except ValueError: print('Ingresar una edad valida')
while True:
   try:
        ncu = int(input('Numero de cuenta: '))
        break
   except ValueError: print('Ingresar un numero de cuenta valido')
while True:
   try:
        cre = float(input('Credito: '))
        break
   except ValueError: print('Ingresar un credito valido')

cliente_1 = Cliente(nom, eda, ncu, cre)

print(cliente_1)

print('El cliente posee un credito de: ', cliente_1.obtener_credito())