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
