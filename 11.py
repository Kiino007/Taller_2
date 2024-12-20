# Escribe un programa que solicite al usuario un número entero positivo y luego 
#calcule la cantidad de dígitos del número utilizando un bucle while.

numer = int(input("Introduce un numero entero y positivo: "))
contador = 0


while numer > 0:
    numer = numer // 10
    contador = contador + 1

print(f"El numero tiene {contador} digitos.")