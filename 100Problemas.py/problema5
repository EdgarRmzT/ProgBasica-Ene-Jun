#Verificar si un numero es primo
numero = int(input("Ingrese un número: "))

def es_primo(n):
    if n<2:                    #numeros menores a 2 no son primos
        return False
    for i in range(2, int(n**0.5)+1): 
        if n % i == 0:
            return False       #si el numero es divisible por cualquier num en ese rango, entonces no es primo
    return True                #si termina sin encontrar divisores entonces el num es primo

if es_primo(numero):              #si este TRUE se imprime si no de lo contrario imprime que no es primo
    print(numero, "es un número primo")
else:
    print(numero, "no es un número primo")