#Escribe un programa que solicite al usuario un número entero positivo y luego imprima todos 
#los números primos menores o iguales a ese número utilizando un bucle while.

numer = int(input("Introduce un número entero y positivo: "))
primo = 2  


while primo <= numer:
    es_primo = True  
    divisor = 2

    while divisor <= primo // 2:
        if primo % divisor == 0:
            es_primo = False  
            break
        divisor += 1

    
    if es_primo:
        print(primo)