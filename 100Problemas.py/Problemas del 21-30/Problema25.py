#Generar y analizar un histogramas de datos
"""
pip install --upgrade mathplot numpy
pip install mathplot numpy
"""

import matplotlib.pyplot as plt
import numpy as np

def generar_histograma():
    datos = list(map(int, input("Ingrese los datos separados por espacios: ").split()))
    bins = int(input("Ingrese el número de bins: "))
    
    plt.hist(datos, bins=bins, edgecolor='black')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos')
    plt.show()
    
    print(f"Media: {np.mean(datos)}")
    print(f"Mediana: {np.median(datos)}")
    print(f"Desviación estándar: {np.std(datos)}")

generar_histograma()




import matplotlib.pyplot as plt
import numpy as np

def generar_histograma():
    # Solicitar al usuario que ingrese los datos
    datos_str = input("Ingrese los datos separados por espacios: ")
    try:
        datos = list(map(float, datos_str.split()))  # Convertir a float para manejar decimales
    except ValueError:
        print("Error: Asegúrese de ingresar números válidos separados por espacios.")
        return

    # Solicitar al usuario que ingrese el número de bins
    try:
        bins = int(input("Ingrese el número de bins: "))
    except ValueError:
        print("Error: Asegúrese de ingresar un número entero válido para los bins.")
        return

    # Generar el histograma
    plt.hist(datos, bins=bins, edgecolor='black')
    plt.xlabel('Valores')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Datos')
    plt.show()

    # Calcular y mostrar estadísticas básicas
    print(f"Media: {np.mean(datos)}")
    print(f"Mediana: {np.median(datos)}")
    print(f"Desviación estándar: {np.std(datos)}")

generar_histograma()