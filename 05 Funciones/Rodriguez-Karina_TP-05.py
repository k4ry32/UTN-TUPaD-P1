
import sys
sys.path.append('./Utils')

import funciones_ejercicios
import validations

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 5 - Funciones """
# MENU DE OPCIONES
def printMenuOptions():
    print('Elija un ejercicio para ejecutar (numero de opción o 0 para finalizar):')
    print(
        """Ejercicios:
        1. Hola Mundo!
        2. Saludo!
        3. Información personal
        4. Area y perímetro de un circulo
        5. Segundos a Horas
        6. Tabla de multiplicar
        7. Operaciones basicas
        8. Calcular IMC
        9. Convertidor °C a °F
        10. Calcular promedio

        0. Salir!
        """
    )

# EJERCICIOS
def ejercicio1():
    funciones_ejercicios.imprimir_hola_mundo()

def ejercicio2():
    nombre = input('Ingrese su nombre: ')
    funciones_ejercicios.saludar_usuario(nombre)

def ejercicio3():
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = input('Ingrese su edad: ')
    residencia = input('Ingrese lugar de residencia: ')
    
    if not validations.isValidIntNumber(edad, 0, 120):
        print('No es una edad valida.')
    else:    
        funciones_ejercicios.informacion_personal(nombre, apellido, edad, residencia)

def ejercicio4():
    radio = input('Ingrese el radio del circulo: ')
    
    if not validations.isValidNumber(radio):
        print('No es un numero valido.')
    else:    
        radio = float(radio)
        area = funciones_ejercicios.calcular_area_circulo(radio)
        perimetro = funciones_ejercicios.calcular_perimetro_circulo(radio)

        print(f'El area del circulo es: {area:.2f}')
        print(f'El perimetro del circulo es: {perimetro:.2f}')

def ejercicio5():
    segundos = input('Ingrese un numero en segundos para transformarlo a horas: ')
    
    if not validations.isValidIntNumber(segundos, 0, float('inf')):
        print('No es un numero valido.')
    else:
        segundos = int(segundos)
        horas = funciones_ejercicios.segundos_a_horas(segundos)
        print(f'{segundos} segundos son {horas:.2f} horas')

def ejercicio6():
    numero = input('Ingrese un numero para ver su tabla de multiplicar: ')

    if not validations.isValidIntNumber(numero, 0, float('inf')):
        print('No es un numero valido.')
    else:
        numero = int(numero)
        funciones_ejercicios.tabla_multiplicar(numero)

def ejercicio7():
    num1 = input('Ingrese el primer numero: ') 
    num2 = input('Ingrese el segundo numero: ')

    if not (validations.isValidNumber(num1) and validations.isValidNumber(num2)):
        print('Uno o ambos numeros no son validos.')
    else:
        num1 = float(num1)
        num2 = float(num2)
        resultados = funciones_ejercicios.operaciones_basicas(num1, num2)

        print(f'Suma: {num1} + {num2} = {resultados[0]}')
        print(f'Resta: {num1} - {num2} = {resultados[1]}')
        print(f'Multiplicacion: {num1} * {num2} = {resultados[2]}')
        if (resultados[3] == None):
            print('No es posible dividir por 0')
        else:
            print(f'Division: {num1} + {num2} = {resultados[3]}')

def ejercicio8():
    altura = input('Ingrese su altura en metros: ')
    peso = input('Ingrese su peso en kilogramos: ')

    if not (validations.isValidNumber(altura, 0, float('inf')) and validations.isValidNumber(peso, 0, float('inf'))):
        print('Uno o ambos numeros no son validos.')
    else:    
        altura = float(altura)
        peso = float(peso)                    
        imc = funciones_ejercicios.calcular_imc(peso, altura)
        print(f'Su IMC es de {imc:.2f}')

def ejercicio9():
    tempC = input('Ingrese una temperatura en °C: ')

    if not validations.isValidNumber(tempC):
        print('No es un numero valido.')
    else:
        tempC = float(tempC)
        tempF = funciones_ejercicios.celsius_a_fahrenheit(tempC)
        print(f'La temperatura ingresada en °F es = {tempF:.2f}°')

def ejercicio10():
    num1 = input('Ingrese el primer numero: ')
    num2 = input('Ingrese el segundo numero: ')
    num3 = input('Ingrese el tercer numero: ')

    if not (validations.isValidNumber(num1) and validations.isValidNumber(num2) and validations.isValidNumber(num3)):
        print('Uno o mas numeros no son validos.')
    else:
        num1 = float(num1)
        num2 = float(num2)
        num3 = float(num3)
        promedio = funciones_ejercicios.calcular_promedio(num1, num2, num3)
        print(f'El promedio es = {promedio:.2f}')

# FUNCION MAIN
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
                    ejercicio1()                    
                case 2:
                    ejercicio2()
                case 3:
                    ejercicio3()
                case 4:
                    ejercicio4()
                case 5:
                    ejercicio5()               
                case 6:
                    ejercicio6() 
                case 7:
                    ejercicio7()
                case 8:
                    ejercicio8()
                case 9:
                    ejercicio9()
                case 10:
                    ejercicio10()                    
            
    print('Gracias por pasar por aqui! Nos vemos en otro TP!')

main()
