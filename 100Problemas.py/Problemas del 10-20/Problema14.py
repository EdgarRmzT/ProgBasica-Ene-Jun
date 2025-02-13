#Implementar distintos metodos de ordenamiento

entrada = input("Introduzca varios números separados por espacios:")
numeros = list(map(int, entrada.split()))  # Convertir a lista de enteros

"""
entrada.split(): Divide la cadena de texto en una lista de subcadenas, usando los espacios como separadores.

map(int, entrada.split()): Aplica la función int() a cada elemento de la lista generada por split()

list(map(...)): Convierte el resultado de map() en una lista.                                  
"""

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

"""
n = len(lista):Obtiene la longitud de la lista.

Bucle externo (for i in range(n)):Itera sobre la lista n veces (una vez por cada elemento).

Bucle interno (for j in range(0, n-i-1)):Compara cada par de elementos adyacentes.

Si el elemento actual (lista[j]) es mayor que el siguiente (lista[j+1]), los intercambia.

return devuelve la lista ordenada (aplica para todos, generalizando)
"""

def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i-1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

"""
or i in range(1, len(lista)):Itera sobre la lista desde el segundo elemento hasta el final.

clave = lista[i]:Almacena el valor del elemento actual para compararlo e insertarlo en la posición correcta.

while j >= 0 and clave < lista[j]:Desplaza los elementos mayores que clave una posición a la derecha.

lista[j + 1] = clave:Inserta clave en la posición correcta.
"""


def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

"""
n = len(lista):Obtiene la longitud de la lista.

Bucle externo (for i in range(n)):Itera sobre la lista para encontrar el elemento más pequeño en cada iteración.

Bucle interno (for j in range(i+1, n)):Busca el elemento más pequeño en la parte no ordenada de la lista.

lista[i], lista[min_idx] = lista[min_idx], lista[i]:Intercambia el elemento actual con el más pequeño encontrado.
"""

print("Original:", numeros)
print("Burbuja:", burbuja(numeros.copy()))
print("Inserción:", insercion(numeros.copy()))
print("Selección:", seleccion(numeros.copy()))

#numeros.copy():Crea una copia de la lista original para que los métodos de ordenamiento no modifiquen la lista original.