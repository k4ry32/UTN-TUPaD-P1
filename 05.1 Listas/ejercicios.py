""" Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
Utilizar la función range. """
def ejercicio1():
    numbers = []

    for num in range(101):
        if (num % 4 == 0):
            numbers.append(num)

    return numbers

""" Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos! """
def ejercicio2():
    lista = ['gato', 'perro', 'conejo', 'raton', 'caballo']
    print('Lista original: ' + str(lista))
    print('Penultimo elemento: ' + str(lista[-2]))

""" Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. """
def ejercicio3():
    lista = []
    lista.append('trabajo')
    lista.append('practico')
    lista.append('5.1')
    print('Lista: ' + str(lista))

""" Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. """
def ejercicio4():
    animales = ["perro", "gato", "conejo", "pez"]
    print('Lista original: ' + str(animales))

    animales[1] = 'loro'
    animales[-1] = 'oso'
    print('Lista modificada: ' + str(animales))

""" Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. """
def ejercicio5():
    print('numeros = [8,15,3,22,7]')
    print('numeros.remove(max(numeros))')
    print('print(numeros)')

    print('En el código mostrado se declara una lista con 5 numeros random desordenados, luego se identifica el mayor con max() y se elimina con remove(). Por ultimo se imprime la lista.')
    numeros = [8,15,3,22,7]
    numeros.remove(max(numeros))
    print('Lista resultante: ' + str(numeros))

""" Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros. """   
def ejercicio6():
    lista = []

    for num in range(10,31,5):
        lista.append(num)

    print('Primeros dos elementos: ' + str(lista[:2]))

""" Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera. """
def ejercicio7():   
    autos = ["sedan", "polo", "suran", "gol"]
    print('Lista original: ' + str(autos))

    autos[1] = 'fiesta'
    autos[2] = 'corsa'
    print('Lista modificada: ' + str(autos))

""" Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla. """
def ejercicio8():
    dobles = [] 
    dobles.append(2*5)
    dobles.append(2*10)
    dobles.append(2*15)

    print('Dobles: ' + str(dobles))

""" Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla
"""
def ejercicio9():
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
    print('Compras sin modificar: ' + str(compras))

    compras[2].append('jugo')
    compras[1][1] = 'tallarines'
    compras[0].remove('pan')

    print('Compras modificadas: ' + str(compras))

""" Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
●​ Posición lista_anidada[0]: 15
●​ Posición lista_anidada[1]: True
●​ Posición lista_anidada[2][0]: 25.5
●​ Posición lista_anidada[2][1]: 57.9
●​ Posición lista_anidada[2][2]: 30.6
●​ Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.
"""
def ejercicio10():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

    print('Lista anidada: ' + str(lista_anidada))
