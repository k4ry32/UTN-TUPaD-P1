import random
import re
from statistics import mode, median, mean

""" Alumna: Rodriguez Karina """

""" Trabajo Práctico n° 3 """

""" Ejercicio 1 """
""" Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

print('Ejercicio 1')
edad = int(input('Ingrese su edad: '))

if edad > 18:
    print('Es mayor de edad')


""" Ejercicio 2 """
""" Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”. """

print('Ejercicio 2')
nota = int(input('Ingrese su calificación: '))

if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')


""" Ejercicio 3 """
""" Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar. """

print('Ejercicio 3')
num = int(input('Ingrese un número par: '))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


""" Ejercicio 4 """
""" Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
●​ Niño/a: menor de 12 años.
●​ Adolescente: mayor o igual que 12 años y menor que 18 años.
●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
●​ Adulto/a: mayor o igual que 30 años. """

print('Ejercicio 4')
edad = int(input('Ingrese su edad: '))

if edad > 0 and edad < 12:
    print('Eres un niñ@')
elif edad >= 12 and edad < 18:
    print('Eres adolescente')
elif edad >= 18 and edad < 30:
    print('Eres un adult@ joven')
elif edad >= 30:
    print('Eres un adult@')


""" Ejercicio 5 """
""" Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. """

print('Ejercicio 5')
password = input('Ingrese una contraseña: ')

if len(password) >= 8 and len(password) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres')


""" Ejercicio 6 """
""" El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números.
Escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
"""

print('Ejercicio 6')
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print('Numeros aleatorios: ' + str(numeros_aleatorios))
print('Media: ' + str(media))
print('Mediana: ' + str(mediana))
print('Moda: ' + str(moda))

if media > mediana and mediana > moda:
    print('Resultado: Hay sesgo positivo')
elif media < mediana and mediana < moda:
    print('Resultado: Hay sesgo negativo')
else:
    print('Resultado: No hay sesgo')


""" Ejercicio 7 """
""" Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. """

print('Ejercicio 7')
frase = input('Ingrese una palabra o frase: ')
match = re.search(r'[aeiou]$', frase)

if match is not None:
    print(frase + '!')
else:
    print(frase)


""" Ejercicio 8 """
""" Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1.Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2.Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3.Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. """

print('Ejercicio 8')
nombre = input('Ingrese su  nombre: ')
print('Elija una de las siguientes opciones para transformar su nombre:')
print('1.Su nombre en mayúsculas. Por ejemplo: PEDRO.')
print('2.Su nombre en minúsculas. Por ejemplo: pedro.')
print('3.Su nombre con la primera letra mayúscula. Por ejemplo: Pedro.')
opcion = int(input('Opcion: '))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    firstLetter = nombre[0:1]
    nombre2 = nombre.replace(firstLetter, firstLetter.upper())
    print(nombre2)
else:
    print('No es una opción valida')


""" Ejercicio 9 """
""" Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
●​ Menor que 3: "Muy leve" (imperceptible).
●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). """

print('Ejercicio 9')
magnitud = float(input('Ingrese la magnitud del terremoto: '))
print('De acuerdo a la escala de Richter, la magnitud del terremoto es: ')

if magnitud < 3:
    print('Muy leve (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('Leve (ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print('Moderado (sentido por personas, pero generalmente no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('Fuerte (puede causar daños en estructuras debiles)')
elif magnitud >= 6 and magnitud < 7:
    print('Muy Fuerte (puede causar daños significativos)')
else:
    print('Extremo (puede causar graves daños a gran escala)')


""" Ejercicio 10 """
""" Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano. """

print('Ejercicio 10')
hemisferio = input('Ingrese el hemisferio en el que se encuentra (N o S): ')
mes = input('Ingrese el mes: ').lower()
dia = int(input('Ingrese el dia: '))

if dia < 1 or dia > 31:
    print('Uno o mas de los datos ingresados no son validos')

elif hemisferio == 'N':
    if (mes == 'diciembre' and dia >= 21) or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
        print('Se encuentra en Invierno')
    elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
        print('Se encuentra en Primavera')
    elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
        print('Se encuentra en Verano')
    elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
        print('Se encuentra en Otoño')
    else:
        print('Uno o mas de los datos ingresados no son validos')
        
elif hemisferio == 'S': 
    if (mes == 'diciembre' and dia >= 21) or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
        print('Se encuentra en Verano')
    elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
        print('Se encuentra en Otoño')
    elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
        print('Se encuentra en Invierno')
    elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
        print('Se encuentra en Primavera')
    else:
        print('Uno o mas de los datos ingresados no son validos')

else:
    print('Uno o mas de los datos ingresados no son validos')