import re

floatRegex = re.compile(r'^-?\d+(\.\d+)?$')
intRegex = re.compile(r'^-?\d+$')

# Valida que el string ingresado sea un numero entero y este dentro de un rango (opcional)
def isValidIntNumber(number, min = float('-inf'), max = float('inf')):
    isValid = intRegex.match(number)

    if isValid and int(number) >= min and int(number) <= max:
        return True
    else: 
        return False

# Valida que el string ingresado sea un numero real y este dentro de un rango (opcional)   
def isValidNumber(number, min = float('-inf'), max = float('inf')):
    isValid = floatRegex.match(number)

    if isValid and float(number) >= min and float(number) <= max:
        return True
    else: 
        return False
