import math

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 1 - Secuenciales """

""" Ejercicio 1 """
""" Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. """

print("Hola Mundo!")

""" Ejercicio 2 """
""" Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado """

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

""" Ejercicio 3 """
""" Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. """

print("Por favor complete los siguientes datos:")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
lugar_residencia = input("Lugar de residencia: ")
print(f"Tu nombre y apellido es {nombre} {apellido}, tienes {edad} años y vives en {lugar_residencia}. Es correcto?")

""" Ejercicio 4 """
""" Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro. """

radio = int(input("Ingrese el radio de un circulo (calcularemos su area y perimetro): "))
pi = math.pi
perimetro = 2 * pi * radio
area = pi * radio**2
print(f"El perimetro es {perimetro} y el area es {area}")

""" Ejercicio 5 """
""" Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale. """

segundos = input("Ingrese un numero en segundos para transformarlo a horas: ")
horas = int(segundos) / 3600
print(f"{segundos} segundos son {horas} horas")

""" Ejercicio 6 """
""" Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número """

num = input("Ingrese un numero para ver su tabla de multiplicar: ")
num = int(num)
for i in range(1, 11):
   print(f"{num} x {i} = {num * i}")

""" Ejercicio 7 """
""" Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

print("Ingrese dos numeros para operar con ellos:")
num1 = int(input("Primer numero: "))
num2 = int(input("Segundo numero: "))
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")

""" Ejercicio 8 """
""" Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. """

print("Vamos a calcular tu indice de masa corporal. Para esto necesitamos:")
altura = float(input("Altura en m: "))
peso = float(input("Peso en kg: "))
imc = peso / altura**2
print(f"Tu IMC es: {imc}")

""" Ejercicio 9 """
""" Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. """

tempC = float(input("Ingrese una temperatura en °C: "))
tempF = (9/5) * tempC + 32
print(f"La temperatura ingresada en °F es = {tempF}°")

""" Ejercicio 10 """
""" Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

print("Ingrese 3 numeros para clacular el promedio:")
num1 = float(input("Primer numero: "))
num2 = float(input("Segundo numero: "))
num3 = float(input("Tercer numero: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es = {promedio}")