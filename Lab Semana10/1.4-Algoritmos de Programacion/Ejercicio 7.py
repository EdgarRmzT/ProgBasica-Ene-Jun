#Ordenamiento y busqueda
import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    derecha = [x for x in lista if x > pivot]
    return quicksort(izquierda) + medio + quicksort(derecha)

def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

n=int(input("Ingrese de cuantos numeros quiere la lista"))
numeros = [random.randint(1, n) for _ in range(n)]
print("Lista original:", numeros)
numeros_ordenados = quicksort(numeros)
print("Lista ordenada:", numeros_ordenados)
num_buscar = int(input("Ingrese un número a buscar: "))
indice = busqueda_binaria(numeros_ordenados, num_buscar)
if indice != -1:
    print(f"El número {num_buscar} se encuentra en la posición {indice}.")
else:
    print(f"El número {num_buscar} no está en la lista.")