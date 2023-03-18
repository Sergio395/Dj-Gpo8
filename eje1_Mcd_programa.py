#Escribir una función que calcule el máximo común divisor entre dos números.


            
def mcd(): 
    
    try:
        
        # solicito los numeros al usuario
        a=int(input("ingrese el primer numero: "))
        b=int(input("ingrese el segundo numero: ")) 
        
        # corroboro que sean numero positivos
        if a>0 and b>0:
            # seleccion el valor mas bajo entre ambas opciones ingresadas y lo asigno a la variable menor
            if a>b:
                menor=b
            else:
                menor=a
            # creo una lista vacia       
            lista = []
                # todas aquellos numeros que sean multiplos de ambos se guardan en la lista        
            for i in range(1,menor, + 1): 
                if a % i == 0  and b % i == 0:
                    lista.append(i)
                    # devuelvo el maximo valor de la lista            
                    print(sorted(lista)[-1])
                    
        else:
            print("los numeros ingresados deben ser mayores que cero")
            mcd()
    except:
        print("Ingrese solo numeros enteros")
        mcd()
mcd()   
        