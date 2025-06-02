import sys
import math
sys.path.append('./Utils')

import ejercicios
import validations

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 6 - Recursividad """
# MENU DE OPCIONES
def printMenuOptions():
    print('**********************************************************************')
    print('Elija un ejercicio para ejecutar (numero de opción o 0 para finalizar):')
    print(
        """Ejercicios:
        1. Factorial de un n°
        2. Serie de Fibonacci
        3. Area de un circulo
        4. Decimal a binario
        5. Es palindromo
        6. Suma recursiva
        7. Piramide
        8. Cuantas veces se repite?

        0. Salir!
        """
    )

def main():
    printMenuOptions()
    repeat = True

    while repeat:
        print('Que ejercicio desea ejecutar? (0 para salir)')
        option = input('Opcion: ')
        isValidOption = validations.isValidIntNumber(option, 0, 10)

        if not isValidOption:
            print('No es una opcion valida, ingrese nuevamente.')
        else:
            option = int(option)
            match option:
                # Salir
                case 0:
                    repeat = False
                # Factorial
                case 1:
                    print('Ingrese un n° para calcular el factorial desde 1 hasta el n° ingresado.')
                    try:
                        n = int(input('N°: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue
                
                    for i in range(1, n+1):
                        print(f'Factorial de {i} = {ejercicios.e1_factorial(i)}')
                # Fibonacci
                case 2:
                    print('Ingrese un n° para calcular la serie de Fibonacci desde 1 hasta la posición ingresada.')
                    try:
                        n = int(input('N°: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue

                    for i in range(1, n+1):
                        print(f'Posicion {i} = {ejercicios.e2_fibonacci(i)}')
                # Potencia
                case 3:
                    print('Ingrese el radio de un circulo para calcular su area.')
                    try:
                        radio = int(input('Radio: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue

                    if radio < 0:
                        print('Debe ser un n° positivo.')
                        continue

                    area =  math.pi * ejercicios.e3_potencia(radio, 2)

                    print(f'El area del circulo es: {area:.2f}')
                # Decimal a binario
                case 4:
                    print('Ingrese un n° para convertirlo a binario.')
                    try:
                        n = int(input('N°: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue

                    print(f'{n} en binario = {ejercicios.e4_decimal_a_binario(n)}')
                # Palindromo
                case 5:
                    print('Ingrese una palabra para saber si es palindromo.')
                    palabra = input('Palabra: ')
                    palabra = palabra.lower().replace(' ', '')
                    palabra = validations.replaceSpecialCharacters(palabra)
                    
                    inicio = 0
                    fin = len(palabra) - 1

                    if ejercicios.e5_es_palindromo(palabra, inicio, fin):
                        print(f'La palabra {palabra} es palindromo.')
                    else:
                        print(f'La palabra {palabra} no es palindromo.')
                # Suma recursiva
                case 6:
                    print('Ingrese un n° entero positivo para calcular la suma de sus dígitos.')
                    try:
                        n = int(input('N°: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue

                    if n <= 0:
                        print('El numero debe ser positivo')
                        continue

                    print(f'Suma de los dígitos de {n} = {ejercicios.e6_suma_digitos(n)}')
                # Piramide
                case 7:
                    print('Ingrese la cantidad de bloques para la base.')
                    try:
                        n = int(input('Bloques: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue

                    print(f'Necesitaras {ejercicios.e7_piramide(n)} bloques para armar la piramide.')
                case 8:
                    try:
                        numero = int(input('Ingresa un numero entero positivo: '))  
                        digito = int(input('Ingresa un digito (0-9) para saber cuantas veces se repite en el anterior: '))
                    except:
                        print('No es un n° valido, ingrese nuevamente.')
                        continue

                    if numero <= 0:
                        print('El numero debe ser positivo')
                        continue
                    elif digito < 0 and digito > 9:
                        print('Debe ser un numero entre 0 y 9')
                        continue

                    print(f'El digito {digito} se repite {ejercicios.e8_contar_digito(numero, digito)} veces.')
            
    print('Gracias por pasar por aqui! Nos vemos en otro TP!')


main()