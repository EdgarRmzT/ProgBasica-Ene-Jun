#Calculadora de estadisticas
import math

def calcular_estadisticas(*args):
    numeros = list(args)
    promedio = sum(numeros) / len(numeros)

    numeros_ordenados = sorted(numeros)
    n = len(numeros_ordenados)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        mediana = numeros_ordenados[n//2]

    varianza = sum((x - promedio) ** 2 for x in numeros) / len(numeros)
    desviacion_estandar = math.sqrt(varianza)
    return promedio, mediana, desviacion_estandar

numeros = input("Ingresa una lista de números separados por espacios: ")
numeros = list(map(float, numeros.split()))
promedio, mediana, desviacion_estandar = calcular_estadisticas(*numeros)

print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Desviación Estándar: {desviacion_estandar}")