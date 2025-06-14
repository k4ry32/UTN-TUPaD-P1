import sys
sys.path.append('./Utils')

import ejercicios
from validations import isValidIntNumber

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 7 - Datos Complejos """
# MENU DE OPCIONES
def printMenuOptions():
    print('**********************************************************************')
    print('Elija un ejercicio para ejecutar (numero de opción o 0 para finalizar):')
    print(
        """Ejercicios:
        1. Agregando frutas al diccionario
        2. Modificando frutas del diccionario
        3. Solo dame las frutas!
        4. Agenda telefonica
        5. Frases y repetidos
        6. Calificacion de alumnos
        7. Quienes aprobaron?
        8. Almacen
        9. Agenda de eventos
        10. Paises y capitales

        0. Salir!
        """
    )

def main():
    printMenuOptions()
    repeat = True

    while repeat:
        print('************************************************')
        print('Que ejercicio desea ejecutar? (0 para salir)')
        option = input('Opcion: ')
        isValidOption = isValidIntNumber(option, 0, 10)

        if not isValidOption:
            print('No es una opcion valida, ingrese nuevamente.')
        else:
            option = int(option)
            match option:
                # Salir
                case 0:
                    repeat = False
                case 1:
                    print('\nEjercicio 1: Frutas!')
                    frutas = ejercicios.ejercicio1()
                    print(frutas)
                case 2:
                    print('\nEjercicio 2: Modicando Frutas!')
                    frutas = ejercicios.ejercicio1()
                    frutas = ejercicios.ejercicio2(frutas)
                    print(frutas)
                case 3:
                    print('\nEjercicio 3: Solo dame las frutas!')
                    frutas = ejercicios.ejercicio1()
                    frutas = ejercicios.ejercicio2(frutas)
                    frutas = ejercicios.ejercicio3(frutas)
                    print(frutas)
                case 4:
                    print('\nEjercicio 4: Agenda Telefonica')
                    agenda = ejercicios.ejercicio4_A()
                    print(agenda)
                    ejercicios.ejercicio4_B(agenda)
                case 5:
                    print('\nEjercicio 5: Frases y palabras repetidas o no')
                    frase = input('Ingrese una frase (con o sin palabras repetidas): ')
                    palabras_unicas = ejercicios.ejercicio5_A(frase)
                    print('Palabras unicas: ' + str(palabras_unicas))
                    recuento = ejercicios.ejercicio5_B(frase)
                    print(recuento)                    
                case 6:
                    print('\nEjercicio 6: Calificaciones de alumnos')
                    alumnos = {}
                    for i in range(3):
                        alumno = ejercicios.ejercicio6_A()
                        alumnos[alumno['name']] = tuple(alumno['notas'])

                    for alumno in alumnos:
                        promedio = ejercicios.ejercicio6_B(alumnos[alumno])
                        print(f'El alumno {alumno} tiene un promedio de {promedio}')
                case 7:
                    print('\nEjercicio 7: Conjuntos de aprobados')
                    ids_aprobados_parcial1 = {101, 102, 105, 110, 112, 115, 120}
                    ids_aprobados_parcial2 = {101, 106, 108, 112, 118, 120, 125, 127}
                    print(f'IDs de alumnos aprobados en el parcial 1: {ids_aprobados_parcial1}')
                    print(f'IDs de alumnos aprobados en el parcial 2: {ids_aprobados_parcial2}')
                    print('')
                    # Aprobados en ambos parciales => Interseccion
                    interseccion = ejercicios.ejercicio7_A(ids_aprobados_parcial1, ids_aprobados_parcial2)
                    print(f'Alumnos aprobados en ambos parciales: {interseccion}')
                    # Aprobaron solo uno de los dos parciales => Diferencia Simetrica
                    diferencia_simetrica = ejercicios.ejercicio7_B(ids_aprobados_parcial1, ids_aprobados_parcial2)
                    print(f'Alumnos aprobados en solo un parcial: {diferencia_simetrica}')
                    # Aprobaron al menos un parcial (sin repetir) => Union
                    union = ejercicios.ejercicio7_C(ids_aprobados_parcial1, ids_aprobados_parcial2)
                    print(f'Alumnos aprobados en al menos un parcial (puede ser ambos): {union}')
                    
                case 8:
                    print('\nEjercicio 8: Control de stock')
                    productos = {
                        'Coca-Cola': 10,
                        'Coca-Cola Zero': 10,
                        'Pepsi': 15,
                        'Fanta': 12,
                        'Sprite': 8,
                        'Agua': 20,
                        'Cerveza Corona': 10,
                        'Cerveza Andes': 15,
                        'Cerveza Quilmes': 18
                    }
                    print(f'Productos disponibles: {', '.join(productos.keys())}')
                    
                    while True:
                        print('\nQue desea hacer?')
                        print('1. Consultar stock')
                        print('2. Agregar unidades a un producto')
                        print('3. Ingresar nuevo producto')
                        print('0. Salir')

                        try:
                            opcion = int(input('\nIngrese una opcion: '))
                        except ValueError:
                            print('No es una opcion valida, ingrese nuevamente.')
                            continue

                        match opcion:
                            case 0:
                                print('Gracias! Vuelva prontos!')
                                break
                            case 1:
                                ejercicios.ejercicio8_A(productos)
                            case 2:
                                ejercicios.ejercicio8_B(productos)
                            case 3:
                                ejercicios.ejercicio8_C(productos)
                            case _:
                                print('No es una opcion valida, ingrese nuevamente.')
                                continue                    

                case 9:
                    print('\nEjercicio 9: Que haremos hoy?')
                    agenda = {
                        ('sabado', '20:00'): 'Parcial de Programacion',
                        ('domingo', '12:00'): 'Ir a casa papa (día del padre)',
                        ('jueves', '17:00'): 'Entrega Integrador OE'
                    }
                    ejercicios.ejercicio9(agenda)

                case 10:
                    print('\nEjercicio 10: Paises y capitales del mundo')
                    paises = {
                        'Argentina': 'Buenos Aires',
                        'Brasil': 'Brasilia',
                        'Chile': 'Santiago',
                        'Colombia': 'Bogota',
                        'Ecuador': 'Quito',
                        'Paraguay': 'Asuncion',
                        'Peru': 'Lima',
                        'Uruguay': 'Montevideo',
                        'Venezuela': 'Caracas'
                    }
                    print(f'\nPaises y capitales: {paises}')

                    capitales = ejercicios.ejercicio10(paises)
                    print(f'\nCapitales y paises: {capitales}')
                case _:
                    print('No es una opcion valida, ingrese nuevamente.')
                    

    print('Gracias por pasar por aqui! Nos vemos en otro TP!')


main()