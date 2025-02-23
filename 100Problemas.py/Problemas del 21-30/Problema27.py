#Crear un conversor de unidades

print("""Elige la unidad de inicial:"
1-. Metros")
2-. Kilómetros")
3-. Millas")
4-. Centímetros""")
    
unidad_origen = int(input("Ingresa el número de la unidad de origen: "))
cantidad = float(input("Ingresa la cantidad a convertir: "))

print("""Elige la unidad de deseada:"
1-. Metros")
2-. Kilómetros")
3-. Millas")
4-. Centímetros""")
    
unidad_destino = int(input("Ingresa el número de la unidad de destino: "))
    
if unidad_origen == 1:  # De metros
    if unidad_destino == 1:
        resultado = cantidad
    elif unidad_destino == 2:
        resultado = cantidad / 1000
    elif unidad_destino == 3:
        resultado = cantidad * 0.000621371
    elif unidad_destino == 4:
        resultado = cantidad * 100
    else:
        print("Opción de unidad destino no válida")
elif unidad_origen == 2:  # De kilómetros
    if unidad_destino == 1:
        resultado = cantidad * 1000
    elif unidad_destino == 2:
        resultado = cantidad
    elif unidad_destino == 3:
        resultado = cantidad * 0.621371
    elif unidad_destino == 4:
        resultado = cantidad * 100000
    else:
        print("Opción de unidad destino no válida")
elif unidad_origen == 3:  # De millas
    if unidad_destino == 1:
        resultado = cantidad / 0.000621371
    elif unidad_destino == 2:
        resultado = cantidad / 0.621371
    elif unidad_destino == 3:
        resultado = cantidad
    elif unidad_destino == 4:
        resultado = cantidad * 160934
    else:
        print("Opción de unidad destino no válida")
elif unidad_origen == 4:  # De centímetros
    if unidad_destino == 1:
        resultado = cantidad / 100
    elif unidad_destino == 2:
        resultado = cantidad / 100000
    elif unidad_destino == 3:
        resultado = cantidad * 0.0000062137
    elif unidad_destino == 4:
        resultado = cantidad
    else:
            print("Opción de unidad destino no válida")
else:
    print("Opción de unidad destino no válida")
    
print("El resultado es:", resultado)
