'''
PREGUNTA 6

Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
True
Recordatorio
La función sum(lista) devuelve una suma de los elementos de una lista.
'''

def modificar(lista:list):
    lista_1=[]
    lista_2=[]
    for i in lista: 
        if i not in lista_1:
            lista_1.append(i)

    lista_1.sort(reverse=True)

    for i in lista_1:
        if i%2==0:
            lista_2.append(i)

    lista_2.insert(0, sum(lista_2))

    return lista_2

ejemplo=[2,4,67,453,657,42,456,678,32,1,34,23,4,8,5,7,12,28,64] #creamos la lista
nueva_lista=modificar(ejemplo)
print(nueva_lista)
print('\nEJERCICIO 9\n')
print('Esta es la lista original:\n lista={}'.format(lista))
print('Esta es la lista modificada:\n nueva_lista={}'.format(nueva_lista))



    
