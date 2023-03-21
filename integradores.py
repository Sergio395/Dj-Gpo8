"""
** EJERCICIOS INTEGRADORES **
"""

# 1. Escribir una función que calcule el máximo común divisor entre dos números.


def maximo_comun_divisor(x, y):
    comodin = 0
    while y != 0:
        comodin = y
        y = x % y
        x = comodin
    return x


def test_ej1():
    '''
    Esta funcion la usamos para pasarle ejemplos a la funcion maximo_comun_divisor(x, y) que se encarga del cálculo
    '''
    print("Ej1: Cálculo de MCD ")
    print('El máximo común divisor "M.C.D" es el mayor número que divide exactamente a dos o más números.')
    print('La utilidad del M.C.D es simplificar las fracciones.')
    print("Grupo A de 18 personas y Grupo B de 12 personas.")
    print("Armar grupos de igual número de personas para que no haya ventajas.")
    x = int(input("Ingrese un número (puede ser 18): "))
    y = int(input("Ingrese otro número (puede ser 12): "))
    # resultado= maximo_comun_divisor(x,y)
    # print (f"Entre el número {x} y el número {y} el cálculo del  M.C.D es {resultado}")
    print(
        f"Entre el número {x} y el número {y} el cálculo del  M.C.D es {maximo_comun_divisor(x,y)}")
    # print (f"Ahora podemos armar para los grupo A y B grupos iguales de {resultado} personas ")
    print(
        f"Ahora podemos armar para los grupo A y B grupos iguales de {maximo_comun_divisor(x,y)} personas ")


# 2. Escribir una función que calcule el mínimo común múltiplo entre dos números

def mcm(x, y):
    return (x*y)/maximo_comun_divisor(x, y)


def prueba_ej2():
    '''
    Esta función le pasa valores a la función mcm.
    La utilizamos para testear el funcionamiento
    '''
    print("Ej2: Calculo de MCM ")
    x = int(input("Ingrese el primer número para calcular su MCM: "))
    y = int(input("Ingrese el segundo número para calcular su MCM: "))
    respuesta_ej2 = mcm(x, y)
    print(f"El mínimo común múltiplo de {x} y {y} es: {respuesta_ej2}")

# 3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def diccionario(inicio):

    # solicito al usuario una entrada de texto
    lista = str(input("ingese su texto: "))
    # genera una lista donde cada palabra es un elemento
    lista = (lista.split())
    # itera la lista formando un diccionario donde el key es la palabra y el valor su repetición
    diccionario = {i: lista.count(i) for i in lista}
    # imprimo el diccionario

    if inicio == 3:
        print(diccionario)
    else:

        return diccionario


# 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def mas_repetida(dicc):
    """
    La función va a recibir un diccionario.
    Crea las variables keymax y max para guardar la clave del máximo y el valor máximo.
    Itera sobre el diccionario recibido, compara en cada iteración si el valor es el máximo.
    Gerena la tupla y la devuelve
    """
    keymax = ''
    max = 0
    for key in dicc:
        if dicc[key] >= max:
            max = dicc[key]
            keymax = key
        else:
            pass
    tuplamax = (keymax, max)
    print(f'Ej4: La tupla de valores máximos es: {tuplamax}')
    return tuplamax


# 5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int():
    '''
    Inicializa la variable es_int que usaremos para entrar o salir del ciclo while, en donde guardaremos si se pudo realizar la conversión.
    Luego iniciamos un ciclo while, para que pida al usuario ingresar el valor hasta que pueda realizar la conversión (es_int == True sale del ciclo).
    El bloque try intenta convertir el ingreso de datos a int, si no hay errores asigna a es_int == True para que no vuelva a entar al ciclo while, y devuelve la cadena.
    Si se lanza la excepción ValueError, es_int = False para que vuelva al ciclo while y vuelve a pedir al usuario que ingrese un valor.
    '''
    cadena = input('Ej5: Ingrese un número entero: ')
    es_int = False
    while es_int == False:
        try:
            int(cadena)
            es_int = True
            return cadena
        except ValueError:
            es_int = False
            cadena = input('Ej5: Por favor ingrese un número entero: ')


# 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# ● mostrar(): Muestra los datos de la persona.
# ● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre="", edad="", dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getters
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    # Setters
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        if type(edad) == int and edad >= 0:
            self.__edad = edad
        else:
            print("Error: ¡La edad debe ser un número positivo!")

    @dni.setter
    def dni(self, dni):
        if type(dni) == int and 999999 < dni <= 99999999:
            self.__dni = dni
        else:
            print("Error: ¡DNI incorrecto!")

    def mostrar(self):
        print("Nombre: ", self.__nombre)
        print("Edad: ", self.__edad)
        print("DNI: ", self.__dni)

    def es_mayor_de_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False


def clase_persona():
    persona = Persona()
    persona.nombre = "José González"
    persona.mostrar()
    persona.edad = "muchos"
    persona.edad = -1
    persona.edad = 50
    persona.mostrar()
    persona.dni = "no recuerdo"
    persona.dni = 999999
    persona.dni = 2345678
    persona.mostrar()
    print(persona.es_mayor_de_edad())


# 7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
# ● Un constructor, donde los datos pueden estar vacíos.
# ● Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# ● mostrar(): Muestra los datos de la cuenta.
# ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad  introducida es negativa, no se hará nada.
# ● retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    # Constructor
    def __init__(self, titular="", cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad

    # getter (uso de decoradores)
    # getter y setter para el atributo privado nombre
    # El orden es importante: 1ro el getter y luego el setter

    @property
    def cantidad(self):
        # Obtiene (get) el saldo, protege la información
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular  # Obtiene el nomnre

    @titular.setter
    def titular(self, nombre):  # Repetimos el nombre del método y en el decorador
        self.__titular = nombre  # Es el nombre que le paso como parámetro a la función

    def mostrar(self):
        cadena = "Titular: " + self.titular + \
            " Cantidad: " + str(self.cantidad)
        return cadena

    def ingresar(self, monto):
        if monto > 0:
            self.cantidad = self.cantidad + monto
            print(f'El monto actual es {self.cantidad}')
        else:
            print(f'el monto es menor a cero, no se puede ingresar')
        print('Fin de la transacción')

    def retirar(self, monto):
        self.cantidad = self.cantidad - monto
        print(f'El monto actual es {self.cantidad}')


def clase_cuenta():
    cliente1 = Cuenta()
    print(f'Mostrar cliente1: {cliente1.mostrar()}')
    print(cliente1.mostrar())
    cliente1.titular = "Pepe"
    print(f'Mostrar cliente1: {cliente1.mostrar()}')
    cliente1.ingresar(-10)
    print(f'Mostrar cliente1: {cliente1.mostrar()}')
    cliente1.ingresar(50)
    print(f'Mostrar cliente1: {cliente1.mostrar()}')
    cliente1.retirar(20)
    print(f'Mostrar cliente1: {cliente1.mostrar()}')
    cliente1.retirar(50)
    print(f'Mostrar cliente1: {cliente1.mostrar()}')


# 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
# CuentaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
# ● Un constructor.
# ● Los setters y getters para el nuevo atributo.
# ● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# ● Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# ● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

class CuentaJoven(Cuenta):
    """
    Esta clase hereda los atributos y métodos de la clase Cuenta, pero para realizar una extracción, se debe tener entre 18 y 24 años. También cuenta con una bonificación por tratarse de un grupo etario joven
    """

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    # Getter
    @property
    def bonificacion(self):
        return self.__bonificacion

    # Setter
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    # Métodos
    def es_titular_valido(self, edad):
        return edad >= 18 and edad < 25

    def retirar(self, cantidad, edad):
        if self.es_titular_valido(edad):
            super().retirar(cantidad)
        else:
            print("No puedes retirar, ya que no perteneces al grupo joven")

    def mostrar(self):
        print(super().mostrar())
        print("Cuenta Joven")
        print("Bonificación:", self.__bonificacion, "%")


def clase_cuentajoven():
    juan = CuentaJoven("Juan Perez", 1000, 15)
    print(juan.bonificacion)
    print(juan.es_titular_valido(17))
    print(juan.es_titular_valido(24))
    juan.bonificacion = 20
    juan.mostrar()
    juan.retirar(500, 14)
    juan.retirar(200, 22)
    juan.mostrar()


def inicio(eleccion):

    match eleccion:
        case "1":
            test_ej1()
        case "2":
            prueba_ej2()
        case "3":
            diccionario(3)
        case "4":
            mas_repetida(diccionario(4))
        case "5":
            print(get_int())
        case "6":
            clase_persona()
        case "7":
            clase_cuenta()
        case "8":
            clase_cuentajoven()


inicio(input("Elija el número de script (1 al 8) que desea ejecutar:  "))
