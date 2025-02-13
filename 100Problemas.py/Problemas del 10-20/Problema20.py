#Implementar busqueda binaria y lineal

from random import randint

elementos = int(input("Introduce la cantidad de elementos: ")) # Solicitar la cantidad de elementos
lista = [randint(1, 100) for _ in range(elementos)] #Generar una lista con números aleatorios
print("Lista generada:", lista)
num = int(input("Introduce un número a buscar: ")) #Pedir un número a buscar


#Busqueda Binaria
lista_ordenada = sorted(lista)  # Ordenar la lista para la búsqueda binaria
print("Lista ordenada:", lista_ordenada)

encontrado_binario = False
inicio = 0
fin = len(lista_ordenada) - 1

while inicio <= fin:
    medio = (inicio + fin) // 2
    if lista_ordenada[medio] == num:
        print("El número:", num, "se encuentra en la posición:", medio, "en la lista ordenada.")
        encontrado_binario = True
        break
    elif lista_ordenada[medio] < num:
        inicio = medio + 1
    else:
        fin = medio - 1

if not encontrado_binario:
    print("El número no está en la lista ordenada.")

#Búsqueda lineal
encontrado = False
for i, itm in enumerate(lista):
    if itm == num:
        print("El número:", (num), "se encuentra en la posición:", (i), "en la lista ordenada.")
        encontrado = True
        break  # Terminar búsqueda al encontrar el primer resultado

if not encontrado:
    print("El número no está en la lista.")