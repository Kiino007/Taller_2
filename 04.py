#Escribe un programa que solicite al usuario un número entero positivo y luego imprima
#si el número es un número de Armstrong utilizando un bucle while.

numer = int(input("Ingrese un numero entero y positivo: "))
num = numer
digi = 0

while numer > 0:
    numer //= 10
    digi += 1

numer = num
suma = 0

while numer > 0:
    digito = numer % 10
    suma += digito ** digi
    numer //= 10

if suma == num:
    print(f"{num} es un numero Armstrong")

else:
    print(f"{num} no es un numero de Armstrong")
