# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int (cadena):
    '''
    Inicializa la variable es_int que usaremos para entrar o salir del ciclo while, en donde guardaremos si se pudo realizar la conversión.
    Luego iniciamos un ciclo while, para que pida al usuario ingresar el valor hasta que pueda realizar la conversión (es_int == True sale del ciclo).
    El bloque try intenta convertir el ingreso de datos a int, si no hay errores asigna a es_int == True para que no vuelva a entar al ciclo while, y devuelve la cadena.
    Si se lanza la excepción ValueError, es_int = False para que vuelva al ciclo while y vuelve a pedir al usuario que ingrese un valor.
    '''
    es_int = False
    while es_int == False:
        try:
            int(cadena)
            es_int = True
            return cadena
        except ValueError:
            es_int = False
            cadena = input('Ej5: Ingrese un número entero: ')

# Comprobación de funcionamiento
prueba = input('Ej5: Ingrese un número entero: ')
print(get_int(prueba))