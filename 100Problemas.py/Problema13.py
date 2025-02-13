#Convertir una temperatura entre distintas escalas

temperatura = float(input("Ingresa la temperatura: "))
escala_original = input("Ingresa la escala original (C, F, K): ")
escala_deseada = input("Ingresa la escala deseada (C, F, K): ")

def convertir_temperatura(temp, escala_original, escala_destino):
    if escala_original == "C" or escala_original== "c":
        celsius = temp
    elif escala_original == "F" or escala_original== "f":
        celsius = (temp - 32) * 5/9
    elif escala_original == "K" or escala_original== "k":
        celsius = temp - 273.15
    else:
        return "Escala original no válida"

    if escala_deseada == "C" or escala_deseada== "c":
        return celsius
    elif escala_deseada == "F" or escala_deseada== "f":
        return (celsius * 9/5) + 32
    elif escala_deseada == "K" or escala_deseada== "k":
        return celsius + 273.15
    else:
        return "Escala deseada no válida"

resultado = convertir_temperatura(temperatura, escala_original, escala_deseada)

if isinstance(resultado, str):  #comprueba si la variable resultado es de tipo str, Si resultado no es una cadena se imprime la temperatura convertida con el formato adecuado.
    print(resultado)  # Mensaje de error
else:
    print("La temperatura convertida es:", resultado, escala_deseada)

