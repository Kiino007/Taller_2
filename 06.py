#Escribe un programa que solicite al usuario un número entero positivo y luego imprima la suma de los 
#cuadrados de todos los números desde 1 hasta ese número utilizando un bucle while.

numer = int(input("Introduce un numero entero y positivo: "))
suma = 0
rang = 1


while rang <= numer:
    suma+= rang ** 2
    rang += 1

print(f"La suma de cuadrados del numero {numer} es: {suma}")

    


        

    
    
    
