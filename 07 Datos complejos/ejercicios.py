from validations import removePunctuation

def ejercicio1():
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    return precios_frutas

def ejercicio2(frutas):
    frutas['Banana'] = 1330
    frutas['Manzana'] = 1700
    frutas['Melón'] = 2800

    return frutas

def ejercicio3(frutas):
    return list(frutas.keys())

# Ingresar contactos en agenda
def ejercicio4_A():
    cantidad = input('Ingrese la cantidad de contactos a ingresar: ')
    agenda = {}

    for i in range(int(cantidad)):
        print('\n---------------------------------------------------')
        print(f'Contacto {i + 1}')
        name = input('Ingrese el nombre del contacto: ')
        phone = input('Ingrese el telefono del contacto: ')
        agenda[name] = phone

    print('----------------- Contactos Guardados ------------------\n')
    return agenda

# Consultar contactos en agenda
def ejercicio4_B(agenda):
    print('------------------ Agenda Telefonica ------------------')

    while True:
        obtenerContacto = input('Desea consultar un contacto? (si/no): ')

        if obtenerContacto.lower() == 'si':
            name = input('Ingrese el nombre del contacto: ')
            if name in agenda:
                print(f'El contacto {name} tiene el telefono {agenda[name]}')
            else:
                print(f'El contacto {name} no se encuentra en la agenda.')
            print('\n')
        else:
            print('------------ Gracias por usar la agenda ------------\n')
            break

# Obtener lista de palabras sin repetir
def ejercicio5_A(frase):
    copyFrase = removePunctuation(frase)
    palabras_unicas = copyFrase.lower().split()
    palabras_unicas = list(set(palabras_unicas))
    return palabras_unicas

# Obtener diccionario con palabras y repeticiones
def ejercicio5_B(frase):
    copyFrase = removePunctuation(frase)
    lista = copyFrase.lower().split()
    diccionario = {}

    for palabra in lista:
        if diccionario.get(palabra) is None:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1

    return diccionario

# Ingresar alumno
def ejercicio6_A():
    name = input('Ingrese el nombre del alumno: ')
    notas = []

    for i in range(3):
        nota = int(input(f'Ingrese la nota {i + 1}: '))
        notas.append(nota)
 
    return { 'name': name, 'notas': notas }

# Calcular promedio
def ejercicio6_B(notas):
    suma = 0
    for nota in notas:
        suma += nota

    promedio = suma / len(notas)
    return promedio

# Obtener conjuntos
# Interseccion
def ejercicio7_A(conjunto1, conjunto2):
    interseccion = conjunto1.intersection(conjunto2)
    return interseccion

# Diferencia simetrica
def ejercicio7_B(conjunto1, conjunto2):
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)
    return diferencia_simetrica

# Union
def ejercicio7_C(conjunto1, conjunto2):
    union = conjunto1.union(conjunto2)
    return union

# Consultar productos
def ejercicio8_A(productos):
    producto = input('Ingrese el nombre del producto a consultar: ')

    if producto in productos:
        print(f'Hay {productos[producto]} unidades de {producto}.')
    else:
        print(f'El producto {producto} no se encuentra en la lista de productos.')

# Modificar stock de un producto
def ejercicio8_B(productos):
    producto = input('Ingrese el nombre del producto a modificar: ')

    if producto in productos:
        print(f'Hay {productos[producto]} unidades de {producto}.')
        try:
            cantidad = int(input('Ingrese la cantidad a agregar: '))
        except ValueError:
            print('Debe ingresar una cantidad valida.')
            return
        
        productos[producto] += cantidad
        print(f'Ahora hay {productos[producto]} unidades de {producto}.')
    else:
        print(f'El producto {producto} no se encuentra en la lista de productos.')

# Agregar nuevo producto
def ejercicio8_C(productos):
    producto = input('Ingrese el nombre del nuevo producto: ')

    try:
        cantidad = int(input('Ingrese el stock del nuevo producto: '))
    except ValueError:
        print('Debe ingresar una cantidad valida.')
        return

    productos[producto] = cantidad
    print(f'El producto {producto} (con {cantidad} unidades) ha sido agregado a la lista de productos.')
    
# Consultar agenda
def ejercicio9(agenda):
    print('Consultar eventos en agenda')
    dia = input('Ingrese el dia (lunes, martes, etc): ')
    hora = input('Ingrese la hora en formato HH:MM: ')

    if agenda.get((dia, hora)) is None:
        print(f'No hay eventos programados para el dia {dia} - {hora}hs.')
    else:
        print(f'Tiene un evento: {agenda[(dia, hora)]}.')

# Invirtiendo diccionario de paises y capitales
def ejercicio10(paises):
    capitales = {}

    for pais, capital in paises.items():
        capitales[capital] = pais

    return capitales