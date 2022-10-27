'''
PREGUNTA 7

Crea un Script llamado recorrido.py que realice las siguientes funciones:
Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]
Imprimr el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
'''

lista=[18, 50, 210, 80, 145, 333, 70, 30]
for index in lista:
   if index%10==0 and index<200:
        print('{} es múltiplo de 10 y menor que 200.'.format(index))



