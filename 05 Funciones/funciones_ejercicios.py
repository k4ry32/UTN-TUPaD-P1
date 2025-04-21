import math

def imprimir_hola_mundo():
    print('Hola Mundo!')

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = None
    
    if b != 0:
        division = a / b

    return (suma, resta, producto, division)

def calcular_imc(peso, altura):
    return peso / pow(altura, 2)

def celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32

def calcular_promedio(a, b, c):
    return (a + b + c) / 3