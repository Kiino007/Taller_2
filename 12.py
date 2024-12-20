# Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima todos los números entre 1 y ese número que sean múltiplos de 7 utilizando un bucle while.

numer = int(input("Introduce un numero entero y positivo: "))
contador = 1


while contador <= numer:
    if contador % 7 == 0:
        print(contador)
    contador = contador + 1 