#Verificar si una cadena es un palindromo

cadena = input("Ingrese una cadena para verificar si es un palíndromo: ")

def es_palindromo(cadena):
    cadena = ''.join(c.lower() for c in cadena if c.isalnum())  # Eliminar espacios y caracteres no alfanuméricos
    return cadena == cadena[::-1]

if es_palindromo(cadena):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")


"""
c.lower(): Convierte cada caracter a minúscula para que la comparación sea insensible a mayúsculas y minúsculas.

if c.isalnum(): Filtra solo caracteres alfanuméricos (letras y números), eliminando espacios, puntuación y caracteres especiales.

''.join(...): Une los caracteres filtrados en una nueva cadena sin espacios ni símbolos.

cadena[::-1] genera la cadena invertida, si la cadena original es igual a su versión invertida, significa que es un palíndromo 
y la función devuelve True; en caso contrario, devuelve False.
"""