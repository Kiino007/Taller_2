#Escribe un programa que solicite al usuario un número entero positivo y luego calcule 
#la suma de todos los números divisibles por 3 desde 1 hasta ese número utilizando un bucle while.

num = int(input("Ingrese un numero entero y positivo: "))
ini = 1
suma = 0

while ini <= num :
    if ini % 3 == 0:
      suma += ini
    ini += 1
print("La suma de los numeros multiplos de 3 es de es de: ", suma)