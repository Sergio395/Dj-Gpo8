print('El máximo común divisor "M.C.D" es el mayor número que divide exactamente a dos o más números')
'''La utilidad del M.C.D es simplificar las fracciones.'''
print("Grupo A de 18 personas y Grupo B de 12 personas")
print("Armar grupos de igual número de personas para que no haya ventajas")
def maximo_comun_divisor(x, y):
    comodin = 0
    while y != 0:
        comodin = y
        y = x % y
        x = comodin
    return x
x= int(input("Ingrese un número: "))
y= int(input("Ingrese otro número: "))
resultado=maximo_comun_divisor(x,y)

print (f"Entre el número {x} y el número {y} el cálculo del  M.C.D es {resultado}")
print (f"Ahora podemos armar para los grupo A y B grupos iguales de {resultado} personas ")
