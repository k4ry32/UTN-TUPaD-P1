""" Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario. """
def e1_factorial(n):
    if n < 0:
        print('No se puede calcular el factorial de un n° negativo')
        return 0
    if n == 0:
        return 1
    else:
        return n * e1_factorial(n-1)
    
""" Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique. """
def e2_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return e2_fibonacci(n-1) + e2_fibonacci(n-2)

""" Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula n^m = n * n^(m-1) . Prueba esta función en un
algoritmo general. """
def e3_potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * e3_potencia(n, m-1)

""" Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto. """
def e4_decimal_a_binario(n):
    if n == 0:
        return ''
    else:
        return e4_decimal_a_binario(n//2) + str(n%2)
    
""" Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es. """
def e5_es_palindromo(palabra, inicio, fin):
    if inicio >= fin:
        return True
    else:
        return palabra[inicio] == palabra[fin] and e5_es_palindromo(palabra, inicio+1, fin-1)
    
""" Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos. """
def e6_suma_digitos(n):
    if n < 10:
        return n
    else:
        return n%10 + e6_suma_digitos(n//10)
    
""" Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide. """
def e7_piramide(n):
    if n <= 0 :
        print('Con que piensas armar la piramide?')
        return 'mas'
    elif n == 1:
        return 1
    else:
        return n + e7_piramide(n-1)
    
""" Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número. """
def e8_contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero%10 == digito:
            return 1 + e8_contar_digito(numero//10, digito)
        else:
            return e8_contar_digito(numero//10, digito)
