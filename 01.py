#Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos los números 
#entre 1 y ese número que sean múltiplos de 5 utilizando un bucle while.

num = int(input("Ingrese un numero entero y positivo"))

n = 1

while n < num:
    if n % 5 == 0:
        print(n)
    n += 1