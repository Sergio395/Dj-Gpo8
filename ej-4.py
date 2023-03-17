# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(cadena):
    # Dividimos la cadena en palabras y las almacenamos en una lista
    palabras = cadena.split()
    # Creamos un diccionario para almacenar la frecuencia de cada palabra
    frecuencia = {}
    # Recorremos cada palabra de la lista
    for palabra in palabras:
        # Si la palabra ya se encuentra en el diccionario, incrementamos su frecuencia
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        # Si la palabra no se encuentra en el diccionario, la agregamos con frecuencia 1
        else:
            frecuencia[palabra] = 1
    # Devolvemos el diccionario con la frecuencia de cada palabra
    return frecuencia

print(contar_palabras(input("Ingrese una cadena de caracteres: ")))

# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.


def mas_repetida (dicc):
    """
    La función va a recibir un diccionario.
    Crea las variables keymax y max para guardar la clave del máximo y el valor máximo.
    Itera sobre el diccionario recibido, compara en cada iteración si el valor es el máximo.
    Gerena la tupla y la devuelve
    """
    keymax = ''
    max = 0
    for key in dicc:
        # print (dicc[key])
        if dicc[key] >= max:
            max = dicc[key]
            keymax = key
        else:
            pass
    tuplamax = (keymax, max)
    # print (f'Ej4 (print desde mas_repetida): La tupla de valores máximos es: {tuplamax}')
    return tuplamax

print (mas_repetida(contar_palabras(input("Ej4: Ingrese una cadena de caracteres:  " ))))