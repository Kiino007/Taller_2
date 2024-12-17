#Escribe un programa que solicite al usuario dos números enteros positivos y luego imprima 
#todos los números entre ellos (inclusive) utilizando un bucle while.

print("Ingrese dos numero enteros positivos en el orden indicado")

num1 = int(input("Ingrese el numero mayor: "))
num2 = int(input("Ingrese el numero menor: "))
dif = num1 + 1

while dif > num2:
    if num2 != dif:
        print(num2)
    num2 += 1
    
    
