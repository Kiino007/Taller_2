# Escribe un programa que solicite al usuario un número entero positivo y luego 
#imprima el promedio de todos los números desde 1 hasta ese número utilizando un bucle while.

numero = int(input("Introduce un número entero positivo: "))

suma = 0
contador = 1


while contador <= numero:
    suma = suma + contador  
    contador = contador + 1  

promedio = suma / numero


print(f"El promedio de los números desde 1 hasta {numero} es: {promedio}")