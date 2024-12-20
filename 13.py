# Escribe un programa que solicite al usuario dos números enteros positivos y luego 
#imprima la tabla de multiplicar del primer número hasta el segundo número utilizando un bucle while.

numer1 = int(input("Introduce el primer numero entero y positivo: "))
numer2 = int(input("Introduce el segundo numero entero y positivo: "))

contador = 1


while contador <= numer2:
    resultado = numer1 * contador
    print(f"{numer1} x {contador} = {resultado}")
    contador = contador + 1