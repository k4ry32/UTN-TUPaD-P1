import funciones_ejercicios

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 4 - Estructuras Repetitivas """

def isValidOption(option):
    isValid = option.isdecimal()
    if isValid:
        return int(option)
    else: 
        return -1

print('Elija un ejercicio para ejecutar (numero de opción o 0 para finalizar):')
print(
    """Ejercicios:
    1. Ver numeros del 0 al 100, en forma creciente, uno por linea
    2. Cuantos digitos tiene el numero ingresado?
    3. Sumar enteros comprendidos entre dos numeros (estos excluidos).
    4. Sumar numeros hasta que se ingrese 0.
    5. Adivina el numero!
    6. N° pares de 100 a 0.
    7. Sumatoria de numeros desde 0 al n° ingresado.
    8. Clasifiquemos los numeros ingresados.
    9. Promedio de valores ingresados.
    10. Inverso de un numero.

    0. Salir!
    """
)
opcion = isValidOption(input('Opcion: '))

while opcion != 0:
    match opcion:
        case 1:
            funciones_ejercicios.ejercicio1()
        case 2:
            funciones_ejercicios.ejercicio2()
        case 3:
            funciones_ejercicios.ejercicio3()
        case 4:
            funciones_ejercicios.ejercicio4()
        case 5:
            funciones_ejercicios.ejercicio5()            
        case 6:
            funciones_ejercicios.ejercicio6() 
        case 7:
            funciones_ejercicios.ejercicio7() 
        case 8:
            funciones_ejercicios.ejercicio8()
        case 9:
            funciones_ejercicios.ejercicio9()
        case 10:
            funciones_ejercicios.ejercicio10()
        case _:
            print('No es una opción válida, ingrese nuevamente:')

    print('Que ejercicio desea ejecutar? (0 para salir)')
    opcion = isValidOption(input('Opcion: '))
        
print('Gracias por pasar por aqui! Nos vemos en otro TP!')

