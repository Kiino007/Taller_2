# Escribe un programa que solicite al usuario dos números enteros positivos y luego 
#imprima la suma de todos los números entre ellos (inclusive) utilizando un bucle while.

numer1 = int(input("Introduce el numero menor que sea entero y positivo: "))
numer2 = int(input("Introduce el numero mayor que sea entero y positivo: "))


suma = 0
contador = numer1


while contador <= numer2:
    suma = suma + contador
    contador = contador + 1


print(f"La suma de los numeros entre {numer1} y {numer2} es: {suma}")