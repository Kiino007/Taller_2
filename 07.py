#Escribe un programa que solicite al usuario un número entero positivo y luego imprima 
#la suma de los primeros n números pares utilizando un bucle while.

numer = int(input("Introduce un numero entero y positivo: "))

suma_pares = 0
num = 2  
contador = 0  


while contador < numer:
    suma_pares += num  
    num += 2  
    contador += 1  

print(f"La suma de los primeros {numer} numeros pares es: {suma_pares}")