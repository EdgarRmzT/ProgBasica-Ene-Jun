#Generar numeros aleatorios con distintas distribuciones

import random

#Distribución uniforme entre 0 y 1
uniforme = random.uniform(0, 1)
print("Uniforme:", uniforme)

#Distribución normal (Gaussiana) con media 0 y desviación estándar 1
normal = random.gauss(0, 1)
print("Normal:", normal)

#Distribución exponencial con parámetro lambda = 1.0
exponencial = random.expovariate(1.0)
print("Exponencial:", exponencial)