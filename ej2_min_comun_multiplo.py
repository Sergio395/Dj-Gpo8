print("El mínimo común multiplo 'mcm' es el número más pequeño de los múltiplos comunes  ")
from ej1_max_comun_divisor import maximo_comun_divisor
def mcm(x,y):
    
    return (x*y)/maximo_comun_divisor(x,y)
x=4
y=6

respuesta_ej2=mcm(x,y)
print(f"El mínimo común múltiplo es: {respuesta_ej2}")
