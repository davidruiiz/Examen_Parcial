'''
PREGUNTA 4

En este ejercicio se os pide crear un fichero llamado listasCEU.py que realice las siguientes funcionnes
Define una lista que contenga al menos 4 elementos de todos los tipos de valores permitidos en Python.
Selecciona cada dos elementos (uno si otro no) desde el final de la lista.
Cambia solamente la posición del primer elemento con el último elemento de la lista.
Elimina el último elemento de la lista modificada en el paso anterior.
Crea una nueva lista con la repetición de los elementos de la lista guardada en el paso anterior.
'''

valores=[5,3.14,True,'cadena']

print(valores[-1::-2])#cada dos elementos desde el final
(valores[0],valores[3])=(valores[3],valores[0]) #cambiar de posición
print(valores)
valores.pop()#elimina el último elemento
print(valores)
valores_repeticion=[]
for i in valores:
    for j in valores_repeticion:
        if i==j and i not in valores_repeticion:
            valores_repeticion.append(i)


print(valores_repeticion) #En este caso al no haber elementos repetidos la lista es vacía