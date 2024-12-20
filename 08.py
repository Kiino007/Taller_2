#Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima los primeros n números impares utilizando un bucle while.

numer = int(input("Introduce un numero entero y positivo: "))

impar = 1
contador = 0

while contador < numer:
    print(impar)
    impar += 2
    contador += 1