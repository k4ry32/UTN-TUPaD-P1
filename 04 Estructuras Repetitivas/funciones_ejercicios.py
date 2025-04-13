import random

""" ------------------------------ Funciones auxiliares ------------------------------ """
def isValidIntNumber(number):
    try:
        number = int(number)
        return { 'error': False, 'num': number }
    except:
        return { 'error': True }

""" ------------------------------ Ejercicios: ------------------------------ """

""" Ejercicio 1 """
""" Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. """
def ejercicio1():
    print('Ejercicio 1:')
    for i in range(101):
        print(i)


""" Ejercicio 2 """
""" Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene. """
def ejercicio2():
    print('Ejercicio 2:')
    num = isValidIntNumber(input('Ingrese un numero entero: '))

    if(num['error'] == False):        
        num = abs(num['num'])
        contador = 0

        while num > 1:
            num = num / 10
            contador += 1

        print(f'El numero tiene {contador} digitos!')
    else:
        print('No es un numero válido.')


""" Ejercicio 3 """
""" Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores. """
def ejercicio3():
    print('Ejercicio 3:')
    num1 = isValidIntNumber(input('Ingrese el primer numero entero: '))
    num2 = isValidIntNumber(input('Ingrese el segundo numero entero: '))

    sumatoria = 0

    if (num1['error'] == False and num2['error'] == False):
        num1 = num1['num']
        num2 = num2['num']

        for i in range(num1+1, num2):
            sumatoria += i

        print(f'La sumatoria final es: {sumatoria}')
    else:
        print('Se ingresaron numeros no validos')


""" Ejercicio 4 """
""" Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0. """
def ejercicio4():
    print('Ejercicio 4:')
    print('Ingrese numeros para sumarlos. Para finalizar ingrese 0.')

    num = isValidIntNumber(input('Numero: '))
    sumatoria = 0

    while num['error'] == False and num['num'] != 0:
        sumatoria += num['num']
        num = isValidIntNumber(input('Numero: '))

    if num['error'] == True:
        print('Se ingreso un numero no valido.')
    else:
        print(f'La sumatoria final es: {sumatoria}')


""" Ejercicio 5 """
""" Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número. """
def ejercicio5():
    print('Ejercicio 5:')
    print('Adivina que numero estoy pensando del 0 al 9.')

    aleatorio = random.randint(1, 9)
    intentos = 0
    
    while True:
        num = input('Ingresa un n°: ')
        intentos += 1
        if str(aleatorio) == num:
            break
    
    print(f'Excelente! Has adivinado en {intentos} intentos!')


""" Ejercicio 6 """
""" Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente. """
def ejercicio6():
    print('Ejercicio 6:')
    num = 100

    while num > 0:
        if(num % 2 == 0):
            print(num)
        num -= 1


""" Ejercicio 7 """
""" Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario. """
def ejercicio7():
    print('Ejercicio 7:')
    num = isValidIntNumber(input('Ingresa un n° entero: '))

    if num['error']:
        print('Debe ingresar un numero entero válido')
        return
    else:
        num = num['num']

    sumatoria = 0

    for i in range(num+1):
        sumatoria += i

    print(f'La suma total es (incluido el n° ingresado): {sumatoria}')


""" Ejercicio 8 """
""" Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio). """
def ejercicio8():
    print('Ejercicio 8:')
    cantidad = 100
    print(f'Debe ingresar {cantidad} numeros enteros, luego obtendra una clasificación de estos.')

    clasificacion = {
        'positivos': 0,
        'negativos': 0,
        'pares': 0,
        'impares': 0
    }
    allValidNumbers = True

    for i in range(cantidad):
        """ num = {
            'error': False,
            'num': random.randint(-999, 999)
        } """
        num = isValidIntNumber(input('Ingrese un numero: '))

        if num['error']:
            print('Debe ingresar un numero entero válido')
            allValidNumbers = False
            break
        else:
            num = num['num']

            if num > 0:
                clasificacion['positivos'] += 1
            elif num < 0:
                clasificacion['negativos'] += 1
            
            if num % 2 == 0:
                clasificacion['pares'] += 1
            else:
                clasificacion['impares'] += 1

    if allValidNumbers:
        print(f'Cantidad de numeros positivos: {clasificacion['positivos']}')
        print(f'Cantidad de numeros negativos: {clasificacion['negativos']}')
        print(f'Cantidad de numeros pares: {clasificacion['pares']}')
        print(f'Cantidad de numeros impares: {clasificacion['impares']}')


""" Ejercicio 9 """
""" Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor). """
def ejercicio9():
    print('Ejercicio 9:')
    cantidad = 100
    print(f'Debe ingresar {cantidad} numeros enteros, luego obtendra el promedio de estos.')

    sumatoria = 0
    allValidNumbers = True

    for i in range(cantidad):
        """ num = {
            'error': False,
            'num': random.randint(-999, 999)
        } """
        num = isValidIntNumber(input('Ingrese un numero: '))

        if num['error']:
            print('Debe ingresar un numero entero válido')
            allValidNumbers = False
            break
        else:
            num = num['num']
            sumatoria += num

    if allValidNumbers:
        print(f'La media es: {sumatoria / cantidad}')

    
""" Ejercicio 10 """
""" Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. """
def ejercicio10():
    print('Ejercicio 10:')
    num = input('Ingrese un numero entero: ')
    invertido = ''

    for i in range(len(num), 0, -1):
        invertido += num[i-1]

    print(f'El numero invertido es: {invertido}')

