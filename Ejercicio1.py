'''
PREGUNTA 1

Realiza los siguientes ejercicios en un fichero llamado Ejercicio1.py:
*Convertir la variable "var_1" en todas las letras mayúsculas y en minúsculas (var_1 = "Módulo 1 de Python ")
*Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales
*Realiza una función llamada funcion1  que calcule siguiente operación para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
*Realiza una función llamada funcion2 para que calcule la siguiente operación para que el resultado final sea igual a catorce (14)// 12 - 4 * (2 - 2) + 2
*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no
Adjuntar archivo  
'''


var_1= "Módulo de Python"
print(var_1.upper())
print(var_1.lower())
print('El tamaño o longitud de la variable "var_1" es:',len(var_1))
operacion=len(var_1)/7
print(round(operacion,4))

def funcion1():
    resultado=12 - (4 * 2) - (2 + 2)
    return resultado

def funcion2():
    resultado=12 - 4 * (2 - 2) + 2
    return resultado

def funcion3():
    edad=int(input('Introduce tu edad:\n'))
    if edad<18:
        cadena='El usuario es menor de edad.'
    else:
        cadena='El usuario es mayor de edad.'
    return cadena

print(funcion1())
print(funcion2())
print(funcion3())

'https://github.com/davidruiiz/Examen_Parcial.git'#GitHub


