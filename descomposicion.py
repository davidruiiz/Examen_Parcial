'''
PREGUNTA 5

Crea un script llamado descomposicion.py que realice las siguientes tareas:
Debe tomar 1 argumento que será un número entero positivo.
En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3287:
python descomposicion.py 3647
El programa deberá devolver una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:
0007
0080
0200
1000
Pista
Que el valor sea un número no significa necesariamente que deba serlo para formatearlo. Necesitarás jugar muy bien con los índices y realizar muchas conversiones entre tipos cadenas, números y viceversa
'''

try:
    numero=int(input("Introduce un número:\n"))
    auxiliar=numero
    contador1=0
    while auxiliar!=0:
        aux=(aux/10)
        contador1+=1

    contador2=0
    while numero!=0:
        descomposicion=(numero%10)*(10**contador2)
        print('{}\n'.format(str(descomposicion.zfill(contador1))))
        numero=int(numero/10)
        contador2+=1
except ValueError:
    

