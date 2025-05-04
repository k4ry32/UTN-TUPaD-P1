import sys
sys.path.append('./Utils')

import ejercicios
import validations

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 5.1 - Listas """
# MENU DE OPCIONES
def printMenuOptions():
    print('Elija un ejercicio para ejecutar (numero de opción o 0 para finalizar):')
    print(
        """Ejercicios:
        1. Multiplos de 4
        2. Mostrando el penultimo elemento
        3. Agregando palabras en una lista
        4. Reemplazando elementos de una lista
        5. Explicacion de codigo
        6. Crear lista con numeros del 10 al 30, haciendo saltos de 5 en 5
        7. Reemplazo de valores
        8. Dobles de numeros
        9. Editar la lista de compras
        10. Mostrar lista anidada

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
                case 0:
                    repeat = False
                case 1:
                    numbers = ejercicios.ejercicio1()             
                    print(f'Los multiplos de 4 son: {numbers}')      
                case 2:
                    ejercicios.ejercicio2()
                case 3:
                    ejercicios.ejercicio3()
                case 4:
                    ejercicios.ejercicio4()
                case 5:
                    ejercicios.ejercicio5()               
                case 6:
                    ejercicios.ejercicio6()
                case 7:
                    ejercicios.ejercicio7()
                case 8:
                    ejercicios.ejercicio8()
                case 9:
                    ejercicios.ejercicio9()
                case 10:
                    ejercicios.ejercicio10()                    
            
    print('Gracias por pasar por aqui! Nos vemos en otro TP!')

main()