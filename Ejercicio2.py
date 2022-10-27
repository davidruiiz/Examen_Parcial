'''
PREGUNTA 2

Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen. ¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
Nombre Apellido ha sacado un Nota de nota.
Ayuda
Para voltear una cadena rápidamente utilizando slicing podemos utilizar un tercer índice -1: cadena[::-1]
cadena = "zeréP nauJ,01"
'''
cadena="zeréP nauJ,01"
cadena=cadena[::-1]
print(cadena)

print('{Nombre} {Apellido} ha sacado un {Nota} de nota.'.format(Nota=cadena[0:2],Nombre=cadena[3:7],Apellido=cadena[8:]))
