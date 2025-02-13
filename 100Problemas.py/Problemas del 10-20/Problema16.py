#Contar numero de Vocales y consonantes en una cadena

cadena = input("Ingrese una palabra/oracion: ") 

def contar_vocales_consonantes(cadena):
    vocales = "aeiouAEIOU"           #Se crean dos cadenas con todas las vocales y consonantes en mayúsculas y minúsculas.
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    num_vocales = sum(1 for c in cadena if c in vocales)
    num_consonantes = sum(1 for c in cadena if c in consonantes)
    return num_vocales, num_consonantes

"""
num_vocales = sum(1 for c in cadena if c in vocales): Se recorre la cadena y se cuenta cada caracter (c) que esté en la cadena de vocales.
la función sum(1 for c in cadena if c in vocales): suma 1 por cada vocal encontrada.

num_consonantes = sum(1 for c in cadena if c in consonantes): hace lo mismo pero con las consonantes
"""

vocales, consonantes = contar_vocales_consonantes(cadena)
print("Número de vocales: ",vocales)
print("Número de consonantes: ",consonantes)


#Juan comia pan cerca de una panaderia dentro de un pan comiendo otro pan el cual estaba cociendo un pan para hacer otro pan y comerce ese pan.
