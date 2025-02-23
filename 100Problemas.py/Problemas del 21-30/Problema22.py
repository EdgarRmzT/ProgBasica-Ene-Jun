#Simular el lanzamiento de una moneda y un dado

import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    return resultado

def lanzar_dado():
    resultado = random.randint(1, 6)
    return resultado

print("""elija una opcion:
1-.Lanzar una moneda
2-.Tirar un dado
""")

opcion = int(input("Introduzca su opcion (1 o 2): "))
if (opcion>2) or (opcion<1):
    print("Opcion invalida, intente de nuevo")
elif opcion == 1:
    resultado = lanzar_moneda()
    print("Resultado del lanzamiento de la moneda:", resultado)
elif opcion == 2:
    resultado = lanzar_dado()
    print("Resultado del lanzamiento del dado", resultado)
