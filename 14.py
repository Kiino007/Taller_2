# Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima la suma de los números de Fibonacci hasta ese número utilizando un bucle while.

numero = int(input("Introduce un número entero y positivo: "))

a = 0
b = 1
suma = 0


while a <= numero:
    suma = suma + a
    a, b = b, a + b

print(f"La suma de los números de Fibonacci hasta {numero} es: {suma}")