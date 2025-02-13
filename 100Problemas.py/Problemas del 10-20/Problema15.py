#Determinar si un año es bisiesto

Año = int(input("Ingrese un año: "))

def es_bisiesto(Año):
    return (Año % 4 == 0 and Año % 100 !=0) or (Año % 400 == 0)
 
if es_bisiesto(Año):
    print(Año,"es un año bisiesto.")
else:
    print(Año, "no es un año bisiesto.")
